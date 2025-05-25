##################### Generative AI ################
 
##### #### #### Module1 : Streamlit101

# run library
import streamlit as st

# start to streamlit app
# with : " streamlit run app.py "
#st.write("Hello World!")

# page regularization
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(page_title="Streamlit 101", page_icon=":robot_face:")


st.write("En yaygın metin gösterme yöntemi")
st.markdown("_Biçimlendirilmiş Metin_")
st.header("Bu bir header örneğidir.")
st.subheader("Bu bir subheader örneğidir.")
st.code('for i in range(10): my_function()')
st.latex(r'''e^{i\pi} + 1 = 0 ''')


##### #### #### Module2 : MultiMedia

st.image(image="1-image_sample.png")
st.video(data="2-video_sample.mp4")
st.audio(data="3-audio_sample.mp3")

st.write("Please, enter your information")
st.text_input(label="Please, give your e-mail: ")
st.text_input(label="Please, give your parola: ")
st.text_input(label="Please, give your password: ", type="password")
st.checkbox(label="Forgot Password")

st.divider()

st.number_input(label="Please, give your age information: ", min_value=18, max_value=40, value=22)
st.slider(label="Please, give your age information: ", min_value=18, max_value=40, value=22)

st.divider()

st.radio(label="What is your status?", options=["Student", "Graduate"])


st.button(label="Please Enter")

st.divider()

st.file_uploader(label="Please Upload File")


##### #### #### Module3 : Uygulamayı iyileştirme : 

#### FOR COL :  ####
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3><b> User Information </b> </h3>", unsafe_allow_html=True) #büyük başlık için h3 kalın olması için b
    st.text_input(label="Give an e-mail address: ")
    st.text_input(label="Give a password", type="password")
    st.checkbox(label="Forgot password")

    st.divider()
    st.button(label="Enter")

with col2:
    st.markdown("<h3><b> User Preferences </b> </h3>", unsafe_allow_html=True) #büyük başlık için h3 kalın olması için b
    st.divider()
    st.radio(label="Account status", options=["Student", "Graduated"])
    st.slider(label="Time out (second)", min_value=3, max_value=30, value=5)
    st.file_uploader(label="Please, Upload Your Resume")

#### FOR TAB : ###

tab1, tab2 = st.tabs(["User Information", "User Preferences"]) # lsite içermelidir.
with tab1:
    st.text_input(label="Give an e-mail address: ")
    st.text_input(label="Give a password", type="password")
    st.checkbox(label="Forgot password")
    st.divider()
    st.button(label="Enter")

with tab2:
    st.radio(label="Account status", options=["Student", "Graduated"])
    st.slider(label="Time out (second)", min_value=3, max_value=30, value=5)
    st.file_uploader(label="Please, Upload Your Resume")


#### FOR SIDEBAR : ###
st.sidebar.markdown("<h4>Wellcome to Application!</h4>", unsafe_allow_html=True)
st.sidebar.image("1-image_sample.png")

tab1, tab2 = st.tabs(["User Information", "User Preferences"]) #liste içermelidir.
with tab1:
    st.text_input(label="Give an e-mail address: ")
    st.text_input(label="Give a password", type="password")
    st.checkbox(label="Forgot password")
    st.divider()
    st.button(label="Enter")

with tab2:
    st.radio(label="Account status", options=["Student", "Graduated"])
    st.slider(label="Time out (second)", min_value=3, max_value=30, value=5)
    st.file_uploader(label="Please, Upload Your Resume")


#### SAVED CHOOICE : ###

import json 

st.sidebar.markdown("<h4>Wellcome to Application!</h4>", unsafe_allow_html=True)
st.sidebar.image("1-image_sample.png")

tab1, tab2 = st.tabs(["User Information", "User Preferences"]) #liste içermelidir.
with tab1:
    email = st.text_input(label="Give an e-mail address: ")
    password = st.text_input(label="Give a password", type="password")

    st.checkbox(label="Forgot password")
    st.divider()
    save_bttn = st.button(label="Saved")

with tab2:
    account_type = st.radio(label="Account status", options=["Student", "Graduated"])

    st.slider(label="Time out (second)", min_value=3, max_value=30, value=5)
    st.file_uploader(label="Please, Upload Your Resume")

if save_bttn:
    data = []
    data.append({"email": email})
    data.append({"password": password})

    if account_type == "Student":
        validity_period = 365
    elif account_type == "Graduated":
        validity_period = 30
    
    data.append({"validity_period": validity_period})

    with open("user.txt", "w") as file:
        file.write(json.dumps(data))
    
    st.balloons()
    st.success("Your file saved.")

    st.write(f"Validity period: {validity_period}")

