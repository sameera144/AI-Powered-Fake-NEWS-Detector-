import numpy as np
import pickle
import streamlit as st

model=pickle.load(open("3_model.pkl","rb"))
vectorizer=pickle.load(open("2_vectorizer.pkl","rb"))

st.title("AI-Powered Fake News Detector")

news_text=st.text_area("Enter the news","")

if st.button("check news"):
    if news_text.strip()!="":
        input_vector=vectorizer.transform([news_text])

        prediction=model.predict(input_vector)

        if prediction[0]==0:
            st.error("Fake news detected!")
        else:
            st.success("Real news!")
    else:
        st.warning("please enter some news text")
    
   