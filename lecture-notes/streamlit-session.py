# FIRST SESSION

st.session_state.mesaj = "Bilgilendirme mesajı" # .mesaj bizim eklediğimiz kısımdır
st.session_state.yil = 2025
st.session_state["Kullanici Adi"] = "Miuul"
gunler = ["Pazartesi", "Sali", "Carsamba", "Persembe", "Cuma"]
st.session_state.liste = gunler
 
st.write(st.session_state)
st.session_state.yil +=10

st.write(st.session_state)

st.session_state.email = st.text_input(label="Give an e-mail address:")
st.text_input(label="Give a password", type="password", key="password")

goruntule_btn = st.button(label = "Görüntüle")

if goruntule_btn: 
    st.info(st.session_state.email)
    st.info(st.session_state.password) # Give a password kısmındaki key parametresini buraya veriyoruz

# SECOND SESSION 

import streamlit as st
import pandas as pd

st.header("Session State Mechanism: Pratic Using")

if "satir_sayisi" not in st.session_state:
    st.session_state.satir_sayisi = 10

dataframe = pd.read_csv("data.csv", sep=",")
st.table(dataframe.head(st.session_state.satir_sayisi)) # okuduklarımızı table ile gösterebiliyoruz 

## CALL BACK FUNCTIONS 

## tablodaki güncellemelerin tıklamaya entegre olarak gerçekleşmesi : 

def artir():
    st.session_state.satir_sayisi += 1

def dusur():
    st.session_state.satir_sayisi -= 1

####  yukaridaki fonksiyonlar tanımlandığı için bu kısmı kaldırdık
## if artir_btn:
##     st.session_state.satir_sayisi += 1

## if dusur_btn:
##     st.session_state.satir_sayisi -= 1


artir_btn = st.button(label="Artır 👆🏼", on_click=artir)
dusur_btn = st.button(label="Düşür 👇🏼", on_click=dusur)

st.divider()
st.header(st.session_state.satir_sayisi)