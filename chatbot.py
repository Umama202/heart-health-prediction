import streamlit as st
from streamlit_chat import message

st.title("💬 Heart Health Chatbot")


faq = {
    "hey": "Hi! How can I help you!!!",
    "i am having chest pain, shortness of breath, palpitation,sweating,jaw pain,pain in left hand what should i do":
        "These are symptoms of a heart attack. Quickly chew one Tab Aspirin directly, swallow Tab Atorva Statin with water, "
        "and place Tab Nitroglycerin under your tongue for pain. Don't worry, you will be relieved in a few minutes, but go to "
        "the hospital immediately after taking these medications for further consultation with a doctor.",
    "what is heart attack prevention":
        "Heart attack prevention includes regular exercise, healthy eating, controlling blood pressure, and no smoking.",
    "how to prevent heart disease":
        "To prevent heart disease: exercise, eat healthy, manage stress, and avoid tobacco use including quit smoking.",
    "medication to help prevent heart attacks":
        "Common medications: Tab Atorva Statin 80mg (cholesterol-lowering drug). If your age is 80-90, take 40mg. "
        "Tab Aspirin (blood thinner), Tab Nitroglycerin. Always consult a doctor.",
    "medicine for high blood pressure": "Tab Telmikind AM.",
    "medicine for diabetes": "Tab Gluconorm G1.",
    "how to take these medicine":
        "Chew one Tab Aspirin directly, swallow Atorva Statin with water, and place Tab Nitroglycerin under your tongue for pain. "
        "Don't worry, you will be relieved in a few minutes, but go to the hospital immediately for further consultation with the doctor.",
    "what is a statin": "Statins are medicines that lower cholesterol and help prevent heart attacks and strokes.",
    "tips for heart health":
        "Eat lots of fruits and vegetables, exercise 30 minutes daily, maintain a healthy weight, and limit salt and sugar intake."
}

default_response = "I'm sorry, I don't have information about that. Please consult a healthcare professional."

def get_bot_response(user_question):
    user_question = user_question.lower()
    for question in faq:
        if question in user_question:
            return faq[question]
    return default_response


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


user_input = st.text_input("You:", key="chat_input")

if user_input:
    response = get_bot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for i, (sender, text) in enumerate(st.session_state.chat_history):
    message(text, is_user=(sender == "You"), key=f"{sender}_{i}")
