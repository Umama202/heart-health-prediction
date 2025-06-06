from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("new.html")  # Make sure new.html is inside a /templates folder

@app.route("/symptom-check", methods=["POST"])
def symptom_check():
    data = request.get_json()
    user_input = data.get("symptom", "").lower()

    symptoms = ["chest pain", "palpitations", "nausea", "dizziness"]
    meds = ["Aspirin", "Nitroglycerin", "Atorvastatin"]

    if any(symptom in user_input for symptom in symptoms):
        reply = f"⚠️ Possible heart issue. Recommended meds: {', '.join(meds)}. Please consult a doctor."
    else:
        reply = "✅ No critical symptoms detected. Still, monitor and consult a doctor if needed."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
