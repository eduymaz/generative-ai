from langchain_goole_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import CohereEmbeddings # FOR EMBEDDING
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings #for hugging face
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")
my_key_google = os.getenv("google_apikey")
my_key_cohere = os.getenv("cohere_apikey")
my_key_hf = os.getenv("huggingface_access_token") # repo to be "read"

llm_gemini = ChatGoogleGenerativeAI(goole_api_key=my_key_google, model = "gemini-pro")
# embedding = OpenAIEmbedding(api_key=my_key_openai)
# embeddings = CohereEmbeddings(cohere_api_key=my_key_cohere, model="embed-multilingual") # dile göre model değişmeli örn. Eng için -> embed-english-v3.0
embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=my_key_hf,
    model_name="sentence-transformers/all-MiniLM-16-v2"
)



def ask_gemini(prompt):
    AI_Response = llm_gemini.invoke(prompt)
    return AI_Response.content

def rag_with_url(target_url, prompt):
    loader = WebBaseLoader(target_url)
    raw_documents = loader.load()

    text_splitter = RecursiveCharacterTextSplistter()
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len



    splitted_documents = txt_splitter.split_documents(raw_documents)

    vectorstore = FAISS.from_documents(splitted_documents, embeddings)
    retriever = vectorstore.as_retriever()

    retriever_documents = retriever.get_relevant_documents(prompt) # asagidaki ??? yerine kullanilacak.
    context_data = ""

    for document in relevant_documents:
        context_data = context_data + document.page_content
    
    final_prompt = f"""This is a problem: {prompt} 
    Bu soruyu yanitlamak icin elimizde su bilgiler var: {???} .
    Bu sorunun yanitini vermek icin yalnizca sana burada verdigim eldeki bilgiler var. Bunlarin disina asla cikma!"""

    AI_Response = llm_gemini.invoke(final_prompt)

    return AI_Response.content

#veri tipine göre fonksiyon degisir : 

def rag_with_pdf(filepath, prompt): #data adresi + prompt

    loader = PyPDFloader(filepath)  #WEB'den değil yereldeki  pdf'ten kaynak gelir
    raw_documents = loader.load()

    text_splitter = RecursiveCharacterTextSplistter()
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len



    splitted_documents = txt_splitter.split_documents(raw_documents)

    vectorstore = FAISS.from_documents(splitted_documents, embeddings)
    retriever = vectorstore.as_retriever()

    retriever_documents = retriever.get_relevant_documents(prompt) # asagidaki ??? yerine kullanilacak.
    context_data = ""

    for document in relevant_documents:
        context_data = context_data + document.page_content
    
    final_prompt = f"""This is a problem: {prompt} 
    Bu soruyu yanitlamak icin elimizde su bilgiler var: {???} .
    Bu sorunun yanitini vermek icin yalnizca sana burada verdigim eldeki bilgiler var. Bunlarin disina asla cikma!"""

    AI_Response = llm_gemini.invoke(final_prompt)

    return AI_Response.content, relevant_documents






