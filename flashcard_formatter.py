# flashcard_formatter.py
import pandas as pd
import json
import os

def export_flashcards(flashcards, export_format="json", output_path="outputs/flashcards.json"):
    """
    Exports flashcards to a file in JSON or CSV format.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if export_format == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(flashcards, f, indent=2)

    elif export_format == "csv":
        df = pd.DataFrame(flashcards)
        df.to_csv(output_path, index=False, encoding="utf-8")
