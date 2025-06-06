import streamlit as st
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt


with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

log_file = "prediction_logs.csv"


st.title("🫀 Heart Risk Monitoring Dashboard")


st.sidebar.header("Enter Patient Info")
age = st.sidebar.slider("Age", 1, 100, 30)
gender = st.sidebar.radio("Gender", ["Male", "Female"])
heart_rate = st.sidebar.slider("Heart Rate", 40, 200, 80)
systolic = st.sidebar.slider("Systolic BP", 90, 200, 120)
diastolic = st.sidebar.slider("Diastolic BP", 60, 150, 80)
blood_sugar = st.sidebar.slider("Blood Sugar", 50, 500, 100)
ckmb = st.sidebar.slider("CK-MB", 0, 100, 5)
troponin = st.sidebar.slider("Troponin", 0.0, 50.0, 0.1)

if st.sidebar.button("Predict Risk"):
    gender_val = 1 if gender == "Male" else 0
    input_data = pd.DataFrame([{
        'Age': age,
        'Gender': gender_val,
        'Heart rate': heart_rate,
        'Systolic blood pressure': systolic,
        'Diastolic blood pressure': diastolic,
        'Blood sugar': blood_sugar,
        'CK-MB': ckmb,
        'Troponin': troponin
    }])

    scaled = scaler.transform(input_data)
    pred = model.predict(scaled)[0]
    risk_label = label_encoder.inverse_transform([pred])[0]

    st.success(f"Predicted Risk Level: **{risk_label}**")

    input_data["Predicted Risk"] = risk_label
    if os.path.exists(log_file):
        log_df = pd.read_csv(log_file)
        log_df = pd.concat([log_df, input_data], ignore_index=True)
    else:
        log_df = input_data
    log_df.to_csv(log_file, index=False)


st.header("📊 Prediction Monitoring & Analysis")

if os.path.exists(log_file):
    df = pd.read_csv(log_file)
    st.subheader("Prediction Log")
    st.dataframe(df)

    
    st.subheader("Risk Level Distribution (Bar Chart)")
    dist = df["Predicted Risk"].value_counts().reindex(["Low", "Medium", "High"], fill_value=0)
    st.bar_chart(dist)

    st.subheader("Risk Level Distribution (Pie Chart)")
    fig, ax = plt.subplots()
    ax.pie(dist, labels=dist.index, autopct="%1.1f%%", colors=["green", "orange", "red"])
    ax.axis("equal")
    st.pyplot(fig)

    
    st.subheader("Feature Impact on Risk (Group Averages)")
    for col in ['Age', 'Heart rate', 'Systolic blood pressure', 'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin']:
        st.markdown(f"**{col} vs Risk**")
        avg = df.groupby("Predicted Risk")[col].mean().reindex(["Low", "Medium", "High"])
        st.bar_chart(avg)

else:
    st.info("No predictions logged yet.")
