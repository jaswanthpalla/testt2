import streamlit as st
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

st.title("spaCy and Streamlit Example")
text = st.text_area("Enter text to analyze boby")
if text:
    doc = nlp(text)
    st.write("Named Entities:")
    for ent in doc.ents:
        st.write(f"{ent.text} - {ent.label_}")
