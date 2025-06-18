import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

import streamlit as st
from llm_utils import generate_flashcards_from_text

def main():
    st.set_page_config(page_title="Flashcard Generator", layout="wide")
    st.title("📚 Educational Flashcard Generator")

    st.markdown("Generate Q&A flashcards from educational content like notes, chapters, or documents.")

    input_type = st.radio("Choose input type:", ["Text", "File Upload"], horizontal=True)
    text_input = ""

    if input_type == "Text":
        text_input = st.text_area("Paste educational content here:", height=300)
    else:
        uploaded_file = st.file_uploader("Upload a text file:", type=["txt", "md"])
        if uploaded_file is not None:
            text_input = uploaded_file.read().decode("utf-8")

    if st.button("✨ Generate Flashcards") and text_input:
        with st.spinner("Generating flashcards using the model..."):
            flashcards = generate_flashcards_from_text(text_input)

        if flashcards:
            st.success(f"Generated {len(flashcards)} flashcards!")
            for i, card in enumerate(flashcards, 1):
                with st.expander(f"Flashcard {i}"):
                    st.markdown(f"**Q:** {card['question']}")
                    st.markdown(f"**A:** {card['answer']}")
        else:
            st.error("⚠️ No flashcards were generated. Please try with different content.")

if __name__ == "__main__":
    main()




