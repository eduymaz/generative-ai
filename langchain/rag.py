import streamlit as st
import raghelper

st.set_page_config(page_title="LangChain ile Bellek Genişletme", layout="wide")
st.title("LangChain ile Bellek Genişletme: URL")
st.divider()


col_input, col_rag, col_normal = st.columns([1,2,2])

with col_input:
    target_url = st.text_input(label="İşlenecek Web Adresini Giriniz:")
    st.divider()
    prompt = st.text_input(label="Sorunuzu Giriniz: ", key="url_prompt")
    st.divider()
    submit_btn = st.button(label="Sor", key="url_button")
    st.divider

    if submit_btn:
        with col_rag:
            with st.spinner("Yanıt Hazırlanıyor..."):
                st.success("YANIT - Bellek GEnişletme Devrede")
                st.markdown(raghelper.ask_gemini(prompt=prompt))
                st.divider()

st.title("LangChain ile Bellek Genişletme: PDF")
st.divider()

col_input, col_rag, col_normal = st.columns([1,2,2])

with col_input:
    target_url = st.text_input(label="İşlenecek Dosyayı seçiniz", type=["pdf"])
    st.divider()
    prompt = st.text_input(label="Sorunuzu Giriniz: ", key="pdf_prompt")
    st.divider()
    submit_btn = st.button(label="Sor", key="pdf_button")
    st.divider
    

if submit_btn:

    with col_rag:
        with st.spinner("Yanıt Hazırlanıyor..."):
            st.succes("YANIT - Bellek Genişletme Devrede")
            AI_Response, relevant_documents = raghelper.rag_with_pdf(filepath=f"./data/{selected_file.name}", prompt=prompt)
            st.markdown(AI_Response)
            st.divider()

            for doc in relevant_documents:
                st.caption(doc.page_content)
                st.markdown(f"Kaynak: {doc.metadata}")
                st.divider()

        with col_normal:
            with st.spinner("Yanıt Hazırlanıyor..."):
                st.succes("YANIT - Bellek Genişletme Devre Dışı")
                AI_Response, relevant_documents = raghelper.rag_with_pdf(filepath=f"./data/{selected_file.name}", prompt=prompt)
                st.markdown(AI_Response)
                st.divider()
