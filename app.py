!pip install streamlit --quiet
!pip install pyngrok==4.1.1
from pyngrok import ngrok
%%writefile app.py
import streamlit as st
import joblib
model = joblib.load('amazon review')
st.title('AMAZON REVIEW PREDICTION')
ip = st.text_input("enter the message")
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
!nohup streamlit run app.py &
url = ngrok.connect(port='8501')
url

