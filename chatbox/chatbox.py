import streamlit as st
import os
from dotenv import load_dotenv
import cohere


load_dotenv()
api_key = os.getenv("cohere_apikey")


co = cohere.Client(api_key)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "user", "content": "Merhaba! Sana nasıl yardımcı olabilirim?"}
    ]

st.title("Cohere Chatbox")
st.divider()


for i, message in enumerate(st.session_state.messages):
    with st.chat_message("user" if message["role"] == "User" else "assistant"):
        st.markdown(message["content"])


if prompt := st.chat_input("Mesajınızı yazın..."):
    st.session_state.messages.append({"role": "User", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = co.chat(
            message=prompt,
            chat_history=[
                {"role": m["role"], "message": m["content"]}
                for m in st.session_state.messages[:-1]
            ],
            model="command-r-plus",
            temperature=0.7,
            max_tokens=300
        )
        assistant_reply = response.text
    except Exception as e:
        assistant_reply = f"Bir hata oluştu: {e}"

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
    st.session_state.messages.append({"role": "Chatbot", "content": assistant_reply})