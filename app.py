import streamlit as st
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import pickle
# with open("vectorizer.pkl", "rb") as vec_file:
#     loaded_vectorizer = pickle.load(vec_file)
# with open("model.pkl", "rb") as model_file:
#     loaded_model = pickle.load(model_file)

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)

    text=y[:]
    y.clear()
    for i in text :
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text=y[:]
    y.clear()
    ps= PorterStemmer()
    for i in text:
        y.append(ps.stem(i))
    
    
    return " ".join(y)


vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

# print("Model and Vectorizer loaded successfully!")
st.title("Email/SMS Spam Classifier")
sms = st.text_area("Enter the message")

if st.button("predict"):

    transform_sms =transform_text(sms)
    vectorized_sms = vectorizer.transform([transform_sms])

    result = model.predict(vectorized_sms)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
