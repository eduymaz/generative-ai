# Create OpenAI Function Runnable Chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional
from langchain.chains.openai_functions import create_openai_fn_runnable

import os 
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

llm = ChatOpenAI(model="gtp-4-0125-preview", api_key=my_key_openai)

class Insan(BaseModel):

    """Bir insan hakkında tanımlayıcı bilgiler"""

    isim: str = Field(..., description="Kişinin ismi")
    yas: int = Field(..., description="Kişinin yaşı")
    meslek: Optional[str] = Field(None, description="Kişinin mesleği")


class Sehir(BaseModel):

    """Bir şehir hakkında tanımlayıcı bilgiler"""

    isim: str = Field(..., description="Şehrin ismi")
    plaka_no: int = Field(..., description="Şehrin plaka numarası")
    iklim: Optional[str] = Field(None, description="Şehrin iklimi")



llm = ChatOpenAI(model="gtp-4-0125", api_key=my_key_openai)
prompt = ChatPromptTemplate.from_message(
    [
        ("system", "Sen varlıkları kaydetmek konusunda dünyanın en başarılı algoritmasısın."),
        ("human", "Şu verdiğim girdideki varlıklarıkaydetmek için gerekli fonksiyonlara çağrı yap: {input}"),
        ("human", "İpucu: Doğru formatta yanıtladığından emin ol!")
    ]
)


chain_2 = create_openai_fn_runnable([Insan, Sehir], llm, prompt)

print(chain_2.invoke({"input": "Aydın 34 yaşında, başarılı bir bilgisayar mühendisiydi."}))
print(chain_2.invoke({"input": "Aydın'da hava her zaman sıcaktır ve bu yüzden 09 plakalı araçlarda klima hep çalışır"}))
