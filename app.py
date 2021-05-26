import streamlit as st
import joblib
model = joblib.load('amazon review')
st.title('AMAZON REVIEW PREDICTION')
ip = st.text_input("enter the message")
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
   
