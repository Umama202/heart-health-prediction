import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv("heart.csv")

features = [
    'Age',
    'Gender',
    'Heart rate', 
    'Systolic blood pressure',
    'Diastolic blood pressure',
    'Blood sugar',
    'CK-MB',
    'Troponin'
]
target = 'Risk_Level'

label_encoder = LabelEncoder()
df['Risk_Level_Encoded'] = label_encoder.fit_transform(df[target])

scaler = StandardScaler()
X = scaler.fit_transform(df[features])
y = df['Risk_Level_Encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))


with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("Training complete. Files saved: model.pkl, scaler.pkl, label_encoder.pkl")
