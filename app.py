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

st.set_page_config(page_title="Spam Message Detection", page_icon="📩", layout="centered")
st.title("Email/SMS Spam Classifier")
st.markdown("""
    ### 🔍 Detect Spam Messages Instantly!""")
sms = st.text_area("Enter a message below and our ML model will predict whether it is spam or not.")

st.sidebar.header("⚙️ Settings")
st.sidebar.write("Adjust parameters if needed.")
st.sidebar.markdown("---")

if st.button("Check Message"):

    transform_sms =transform_text(sms)
    vectorized_sms = vectorizer.transform([transform_sms])

    result = model.predict(vectorized_sms)[0]
    if result == 1:
        st.header("🔴 Spam")
    else:
        st.header("🟢 Not Spam")

    st.success("✅ Try different messages and see how the model performs!")