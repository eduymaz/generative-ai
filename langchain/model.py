import streamlit as streamlit
import modelhelper
import time

load_dotenv()

st.set_page_config(page_title="LangChain: Model Karşılaştırma", layout="wide")
st.title("LangChain: Model Karşılaştırma")
st.divider()


col_prompt, col_settings = st.columns([2,3])

with col_prompt:
    prompt = st.text_input(label="Sorunuzu giriniz.")
    st.divider()
    sumbit_btn = st.button("Sor")


with col_settings:
    temperature = st.slider(labels="Temperature", min_value=0.0, max_value=1.0, value=0.7)
    max_tokens = st.slider(labels="Maximum Tokens", min_value=100, max_value=500, value=200, step=100)

    st.divider()

col_gtp, col_gemini, col_claude, col_command = st.columns(4)

#FOR GTP
with col_gtp:
    if submit_btn:
        with st.spinner("GTP Yanıtlıyor..."):
            st.success("GTP-4 Turbo")
            start_time = time.perf_counter() # başlangıç saati
            st.write(modelhelper.ask_gtp(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter() #bitiş saati
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} saniye")


#FOR GEMINI
with col_gemini:
    if submit_btn:
        with st.spinner("Gemini Yanıtlıyor..."):
            st.info("Gemini Pro")
            start_time = time.perf_counter() # başlangıç saati
            st.write(modelhelper.ask_gemini(prompt=prompt, temperature=temperature))
            end_time = time.perf_counter() #bitiş saati
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} saniye")


#FOR ANTHROPIC
with col_claude:
    if submit_btn:
        with st.spinner("Claude Yanıtlıyor..."):
            st.error("Claude 2.1")
            start_time = time.perf_counter() # başlangıç saati
            st.write(modelhelper.ask_claude(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter() #bitiş saati
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} saniye")



#FOR Command
with col_command:
    if submit_btn:
        with st.spinner("Command Yanıtlıyor..."):
            st.warning("Command")
            start_time = time.perf_counter() # başlangıç saati
            st.write(modelhelper.ask_command(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter() #bitiş saati
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} saniye")