import os
from src.extract_text import extract_text_from_pdf
from src.embed_text import get_embedding
from src.similarity import compute_similarity
from src.db import save_result

INPUT_FOLDER = "data/input_pdf"
STORED_FOLDER = "data/stored_pdfs"
THRESHOLD = 0.85

# Get the single input PDF
input_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".pdf")]
input_pdf = input_files[0]  # assuming one upload at a time

input_text = extract_text_from_pdf(os.path.join(INPUT_FOLDER, input_pdf))
input_embedding = get_embedding(input_text)

print(f"\nComparing '{input_pdf}' with stored PDFs:\n")

for file in os.listdir(STORED_FOLDER):
    if not file.endswith(".pdf"):
        continue

    stored_text = extract_text_from_pdf(os.path.join(STORED_FOLDER, file))
    stored_embedding = get_embedding(stored_text)

    similarity = float(compute_similarity(input_embedding, stored_embedding))

    status = (
        "High Similarity Detected"
        if similarity >= THRESHOLD
        else "No Significant Similarity Detected"
    )

    print(f"{file} → Similarity: {similarity:.2f} → {status}")

    save_result(input_pdf, file, similarity, status)
