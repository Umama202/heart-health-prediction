from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# Heart attack symptoms
heart_attack_symptoms = [
    "chest pain", "shortness of breath", "palpitations",
    "nausea", "dizziness", "sweating", "jaw pain", "shoulder pain"
]

# Medications to suggest
medications = ["Aspirin", "Nitroglycerin", "Atorvastatin"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/symptom-check", methods=["POST"])
def symptom_check():
    data = request.get_json()
    user_input = data.get("symptom", "").lower()

    matched = any(symptom in user_input for symptom in heart_attack_symptoms)

    if matched:
        reply = f"Your symptoms may indicate a heart issue. Recommended medications: {', '.join(medications)}. Please consult a doctor urgently."
    else:
        reply = "Your symptom doesn't appear to match common heart attack signs. Still, it's best to consult a healthcare professional."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
