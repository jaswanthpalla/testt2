import streamlit as st
import spacy
from spacy.cli import download

# Load the spaCy model, downloading it if not present
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Streamlit app
st.title("Meeting Notes Summarizer")
text = st.text_area("Enter your text here")
if st.button("Analyze"):
    doc = nlp(text)
    st.write("Named Entities:")
    for ent in doc.ents:
        st.write(f"{ent.text} - {ent.label_}")
