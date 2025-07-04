from langchain.agents import AgentExecuter, create_react_agent, load_tools
from  langchain_communit.chat_models import ChatAnthropic
from langchain import hub
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_communnity.tools.tavil_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os 
from dotenv import load_dotenv


load_dotenv()

my_key_openai = os.getenv("openai_apikey")
my_key_google = os.getenv("google_apikey")
my_key_anthropic = os.getenv("anthropic_apikey")
os.environ["TAVILY_API_KEY"] = os.getenv("tavily_apikey")

llm_gemini = ChatGoogleGenerativeAI(google_api_key=my_key_google, model="gemini-pro")
llm_gpt = ChatOpenAI(api_key = my_key_openai, model="gpt-4-0125-preview", temperature=0, streaming=True)
llm_claude = ChatAnthropic(anthropic_api_key=my_key_anthropic, model_name="claude-2.1")

agent_prompt = hub.pull("hwchase17/react")


def configure_agent(selected_llm, selected_search_engine, selected_image_generator=""):
    if selected_llm == "GPT-4":
        llm = llm_gpt
    elif selected_llm == "Gemini Pro":
        llm = llm_gemini
    elif selected_llm == "Claude-2.1":
        llm = llm_claude

    if selected_search_engine == "DuckDuckGo":
        tools = load_tools(["ddg-search"])
    elif selected_search_engine == "Tavily":
        tools = [TavilySearchResults(max_results=1)]

    agent = create_react_agent(llm=llm, tools=tools, prompt=agent_prompt)
    agent_executer = AgentExecuter(agent=agent, tools=tools, verbose=True)

    return agent_executer



st.set_page_config(page_title="ReAct Ajan ile Sohbet Etkileşimi")
st.image(image="./img/ai_agent_banner.png")
st.divider()


st.sidebar.header("Ajan Konfigürasyonu")
st.sidebar.divider()

selected_llm = st.sidebar.radio(label="Dil Modeli Seçiniz", options=["GPT-4", "Gemini Pro", "Claude-2.1"])
st.sidebar.divider()

selected_search_engine = st.sidebar.radio(label="Arama Motoru Seçiniz", options=["DuckDuckGo", "Tavily"], index=1)
st.sidebar.divider()

selected_image_generator = st.sidebar.radio(label="Resim Üretim Modeli Seçiniz", options=["Stable Diffusion XL", "DALL-E 3"])
st.sidebar.divider()

selected_web_scraper = st.sidebar.radio(label="Web Kazıma Aracı Seçiniz", options=["BeautifulSoup"])
st.sidebar.divider()

turkish_sensitivity = st.sidebar.chackbox(label="Türkçe Yanıta Zorla", value=True)
st.sidebar.divider()

reset_chat_btn = st.sidebar.button(label="Sohbeti Geçmişini Sıfırla")


if "messages" not in st.session_state:
    st.session_state.messages = []


# >>> mesage is printed on the chat window
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(placeholder="Mesajınızı yazınız"):
    st.chat_message("user").write(prompt)

    if turkish_sensitivity:
        st.session_state.messages.append({"role": "user", "content": prompt + "Bu soruyu Türkçe yanıtla"})
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})

    
    with st.chat_message("assistant"):
        st.info("🧠 Düşünce Zinciri İşletiliyor...")
        st_callback = StreamlitCallbackHandler(st.container())

        executor = configure_agent(selected_llm=selected_llm, selected_search_engine=selected_search_engine)

        AI_Response = executor.invoke(
            {"input": st.session_state.messages},
            {"callback": [st_callback]},
            handle_persing_errors=True
        )


        st.markdown(AI_Response["output"], unsafe_allow_html = True)
        st.session_state.message.append({"role":"assistant", "content": AI_Response["output"]})


if reset_chat_btn:
    st.session_state.messages = []
    st.toast("Sohbet geçmişi sıfırlandı!")


