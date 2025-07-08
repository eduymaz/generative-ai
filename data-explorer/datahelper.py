import pandas as pd
from lanchain_experimental.agents.agent_toolkits.pandas.base import (
    create_pandas_dataframe_agent,
)

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os

from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")
my_key_anthropic = os.getenv("anthropic_apikey")


llm_gtp = ChatOpenAI(api_key=my_key_openai, model = "gtp-4-turbo-preview", temperature=0)
llm_claude_opus = ChatAnthropic(anthropic_api_key = my_key_anthropic, model_name="claude-3-opus", temperature=0)
llm_claude_haiku = ChatAnthropic(anthropic_api_key = my_key_anthropic, model_name="claude-3-haiku", temperature=0)


selected_llm = llm_gtp

#summarize data

def summarize_csv(data_file):
   
    df = pd.read_csv(data_file, low_memory=False) # performans problemlerini düşürmek için False
    pandas_agent = create_pandas_dataframe_agent(selected_llm, df, verbose=True, agent_executer_kwargs={"handle_parsing_errors":"True"}) # ajanın konuşmalarını loglamak için verbose True olmalı
    
    data_summary = {}
    
    data_summary["initial_data_sample"] = df.head()
    data_summary["column_descriptions"] = pandas_agent.run("Verideki Sütunları içeren bir tablo yap. Tabloda sütunların adları ve yanlarında kısaca içerdikleri bilgiye dair Türkçe bir açıklama yer alsın. Bunu bir tablo olarak ver.")
    data_summary["missing_values"] = pandas_agent.run("Bu veri kümesinde eksik veri var mı ? Varsa kaç adet var ? Yanıtını ' Bu veri kümesinde X adet hücrede eksik var.' şeklinde ver. ")
    data_summary["duplicate_values"] = pandas_agent.run("Bu veri kümesinde mükerrer veri var mı ? Varsa kaç adet var ? Yanıtını ' Bu veri kümesinde X adet hücrede mükerrer var.' şeklinde ver. ")
    data_summary["essential_metrics"] = df.describe()

    return data_summary

#get dataframe

def get_dataframe(data_file):

    df = pd.read_csv(data_file, low_memory=False)
    return df


#analyze trend

def analyze_trend(data_file, variable_of_interest):

    df = pd.read_csv(data_file, low_memory=False)
    pandas_agent = create_pandas_dataframe_agent(selected_llm, df, verbose=True, agent_executer_kwargs={"handle_parsing_errors":"True"})

    trend_response = pandas_agent.run(f"Veri kümesi içindeki şu değişkenin değişim trendini kısaca yorumla: {variable_of_interest} Yorumlamayı reddetme. Verideki satırlar geçmişten günümüze tarih bazlı olduğu için, verideki satırlara bakarak yorumda bulunabilirsin. Yanıtları Türkçe olarak ver. ")
    
    return trend_response

#ask question

def ask_question(data_file, question):
    df = pd.read_csv(data_file, low_memory=False)
    pandas_agent = create_pandas_dataframe_agent(selected_llm, df, verbose=True, agent_executer_kwargs={"handle_parsing_errors":"True"})


    AI_Response = pandas_agent.run(f"{question} Bu soruyu Türkçe yanıtla.")

    return AI_Response