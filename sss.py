import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# ✅ Load the saved model and vectorizer
model = joblib.load(r'C:\Users\HP440G4\Desktop\spam\spam_classifier_model.pkl')
vectorizer = joblib.load(r'C:\Users\HP440G4\Desktop\spam\tfidf_vectorizer.pkl')

# ✅ Preprocessing function
def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# ✅ Streamlit UI
st.title("📧 Email Spam Detector")
st.write("Paste your email message below and find out if it's spam or not.")

user_input = st.text_area("Enter an email message:")

if st.button("Check"):
    if user_input.strip() != "":
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)
        st.success("✅ HAM (Not Spam)" if prediction[0] == 0 else "🚨 SPAM")
    else:
        st.warning("⚠️ Please enter some text to check.")
