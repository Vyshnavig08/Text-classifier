
import streamlit as st
import joblib

#load the trained model
model=joblib.load("news-classification-model.pkl")

#define sentiment labels
news_labels={'0':'Technical','1':'Business','2':'Sports','3':'Entertainment','4':'Politics'}
 
 #create streamlite app
st.title("News Classification")

#input text area
user_input=st.text_area("Enter news here:")

#prediction button

if st.button("Predict"):
    print(user_input)
    predicted_label=model.predict([user_input])[0]
    predicted_news_label=news_labels[str(predicted_label)]
    
    st.info(f"Predicted Sentiment: {predicted_news_label}")

