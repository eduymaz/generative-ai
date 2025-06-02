#WebBaseLoader - Bir URL'den içerik yükleme 
############################################################ """

from langchain_community.document_loaders import WebBaseLoader

target_url =  "https://kpmg.com/tr/tr/home/gorusler/2023/12/uretken-yapay-zeka-uygulamalarinin-kurumsallasma-yaklasimi.html"
loader = WebBaseLoader(target_url)
raw_documents = loader.load()


with open("URL_icerik.txt", "w") as file:
    file.write(raw_documents[0].page_content)

print(raw_documents[0].metadata)

############################################################ """
############################################################ """

# PyPDFLoader - Bir PDF dosyasından içerik yükleme
from langchain_community.document_loaders import PyPDFLoader

#SAYFA

filepath = "./data/timeline.pdf"
loader = PyPDFLoader(filepath)
pages = loader.load()
print(pages[39].page_content,pages[39].page_metadata)
############################################################ """
############################################################ """


#GÖRSEL

filepath = "./data/digital.pdf"
loader = PyPDFLoader(filepath, extract_images=True)
pages = loader.load()
print(pages[6].page_content)
############################################################ """
############################################################ """


from langchain_community.document_loaders import UnstructuredExcelLoader

filepath = "./data/ai_course.xlsx"

loader=UnstructuredExcelLoader(filepath, mode="elements")
docs = loader.load()

excel_content = docs[0].metadata["text_as_html"]

with open("excel.html", "w") as file:
    file.write(excel_content)
############################################################ """
############################################################ """


