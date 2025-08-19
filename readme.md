**Flashcard Generator using LLM**

**ShelfEx** is a simple app that takes educational text and uses a language model (LLM) to generate structured flashcards (question-answer format). Built using **Python**, **Streamlit**, and **Hugging Face Transformers**.

---

## 🧠 Features

- Upload or paste input text
- Flashcards generated using GPT/Gemma
- Clean UI via Streamlit
- Modular and easy to extend

---

## 🔧 Quick Start

  ```bash
  git clone https://github.com/your-username/ShelfEx.git
  cd ShelfEx
  pip install -r requirements.txt
  streamlit run app.py

📂 Folder Structure
  sample_input/           # Example text files
  app.py                  # Streamlit UI
  llm_utils.py            # LLM interaction logic
  flashcard_formatter.py  # Flashcard output formatting
  requirements.txt


📝 Sample Input
Place .txt files in sample_input/, like:

  The Industrial Revolution was a period of major industrialization that took place during the late 1700s and early 1800s. It began in Great Britain and quickly spread to other parts of the world.

📌 Notes
  For local LLMs (e.g. Gemma), ensure hardware supports it

  LLM outputs are parsed and formatted for clean Q&A

  Works best with structured input

  
