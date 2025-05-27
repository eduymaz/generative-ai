import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

my_key = os.getenv("google_apikey")

genai.configure(
    api_key=my_key
)

client = genai.GenerativeModel(
    model_name="gemini-pro"
)


def generate_response(prompt):

    chat = client.start_chat(history=[])

    AI_Response = chat.send_message(
        "Mevsimler neden oluşur?",
        generation_config=genai.GenerationConfig(
            temperature=0,
            max_output_tokens=256
        )
    )

    return AI_Response.text


import streamlit as st

st.header("Gemini ile İletişim Kurun")
st.divider()

prompt = st.text_input("Mesajınızı Giriniz:")
submit_btn = st.button("Gönder")

if submit_btn:
    response = generate_response(prompt)
    st.markdown(response)


















# AI_Response = client.generate_content(
#     "Mevsimler neden oluşur?",
#     generation_config=genai.GenerationConfig(
#         temperature=0,
#         max_output_tokens=256
#         )
# )

# print(AI_Response.text)