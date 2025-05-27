import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

my_key = os.getenv("anthropic_apikey")

client = anthropic.Anthropic(
    api_key=my_key
)

def generate_response(prompt):

    AI_Response = client.beta.messages.create(
        model = "claude-2.1",
        temperature=0,
        max_tokens=256,
        messages=[
            {"role":"user", "content":prompt}
        ]
    )

    return AI_Response.content[0].text

import streamlit as st

st.header("Claude ile İletişim Kurun")
st.divider()

prompt = st.text_input("Mesajınızı Giriniz:")
submit_btn = st.button("Gönder")

if submit_btn:
    response = generate_response(prompt)
    st.markdown(response)
