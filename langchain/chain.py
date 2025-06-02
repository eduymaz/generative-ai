
#Create Stuff Documents Chain

from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chains.combine_documents import create_stuff_documents_chain


import os 
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

llm = ChatOpenAI(model="gtp-4-0125-preview", api_key=my_key_openai)

prompt = ChatPromptTemplate.from_messages(
    [("system", "Burada ismi geçen kişilerin en sevdiği rengi tek tek yazı: \n\n{context}")]
)

docs = [
    Document(page_content="Gamze kırmızı sever ama sarıyı sevmez."),
    Document(page_content="Murat yeşili sever ama maviyi sevdiği kadar değil."),
    Document(page_content="Burak'a sorsan favori rengim yok der ama belli ki turuncu rengi seviyor.")
]

# AI'n muhakeme yapmasını ve karşılaştırma yapmasını istiyoruz :

chain_1 = create_stuff_documents_chain(llm, prompt)
print(chain_1.invoke({"context": docs}))
