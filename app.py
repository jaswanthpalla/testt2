import streamlit as st
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Streamlit app
st.title("Meeting Notes Summarizer")
text = st.text_area("Enter your text here")
if st.button("Analyze"):
    doc = nlp(text)
    st.write("Named Entities:")
    for ent in doc.ents:
        st.write(f"{ent.text} - {ent.label_}")

