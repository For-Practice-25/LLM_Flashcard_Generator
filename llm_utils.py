from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

tokenizer = AutoTokenizer.from_pretrained("google/gemma-1.1-2b-it", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-1.1-2b-it",
    device_map="auto",  # let Accelerate decide
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
    # Don't use device=... here
)


def generate_flashcards_from_text(input_text, device="cpu"):
    prompt = f"""You are an expert flashcard creator.

Based on the following content, generate exactly 5 flashcards.

Format strictly as:
Q: <question>
A: <answer>

Content:
\"\"\"{input_text}\"\"\"

Generate the flashcards now:
"""

    result = generator(
        prompt,
        max_new_tokens=512,
        temperature=0.7,
        do_sample=False
    )

    output_text = result[0]["generated_text"]
    flashcards = []

    lines = output_text.strip().splitlines()
    current_q, current_a = None, None

    for line in lines:
        if line.strip().startswith("Q:"):
            if current_q and current_a:
                flashcards.append({"question": current_q, "answer": current_a})
                current_q, current_a = None, None
            current_q = line.strip()[2:].strip()
        elif line.strip().startswith("A:"):
            current_a = line.strip()[2:].strip()

    # Append last flashcard if both Q and A found
    if current_q and current_a:
        flashcards.append({"question": current_q, "answer": current_a})

    return flashcards


