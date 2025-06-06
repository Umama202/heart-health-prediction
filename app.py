from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    risk_label = None
    confidence = None

    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            gender = float(request.form['gender'])
            heart_rate = float(request.form['heart_rate'])
            systolic_bp = float(request.form['systolic_bp'])
            diastolic_bp = float(request.form['diastolic_bp'])
            blood_sugar = float(request.form['blood_sugar'])
            ckmb = float(request.form['ckmb'])
            troponin = float(request.form['troponin'])

            features = np.array([[age, gender, heart_rate, systolic_bp, diastolic_bp, blood_sugar, ckmb, troponin]])
            features_scaled = scaler.transform(features)

            prediction = model.predict(features_scaled)[0]
            proba = model.predict_proba(features_scaled)[0][prediction]

            risk_label = label_encoder.inverse_transform([prediction])[0]
            confidence = round(proba * 100, 2)

        except Exception as e:
            risk_label = f"Error: {e}"

    return render_template('index.html', risk_label=risk_label, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
