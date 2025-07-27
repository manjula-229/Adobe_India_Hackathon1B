import fitz  # PyMuPDF
import json
import os
from transformers import pipeline

# Load summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Define keywords per persona
PERSONA_NEEDS = {
    "student": ["definition", "introduction", "example", "summary"],
    "teacher": ["learning objective", "key concept", "important points"],
    "journalist": ["impact", "controversy", "quote", "highlight"],
    "researcher": ["evidence", "experiment", "method", "conclusion"],
    "policy_maker": ["impact", "recommendation", "result", "conclusion"]
}

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    text_blocks = []
    for i, page in enumerate(doc):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if text:
                text_blocks.append({"page": i + 1, "text": text})
    return text_blocks

def filter_relevant_blocks(blocks, persona):
    keywords = PERSONA_NEEDS.get(persona.lower(), [])
    relevant = []
    for block in blocks:
        for keyword in keywords:
            if keyword.lower() in block["text"].lower():
                relevant.append(block)
                break
    return relevant

def summarize_blocks(blocks):
    summaries = []
    for block in blocks:
        try:
            summary = summarizer(block["text"][:1024], max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
        except:
            summary = block["text"][:300] + "..."  # Fallback
        summaries.append({"page": block["page"], "summary": summary})
    return summaries

def generate_persona_summary(pdf_path, persona, output_path):
    blocks = extract_pdf_text(pdf_path)
    relevant = filter_relevant_blocks(blocks, persona)
    summaries = summarize_blocks(relevant)
    result = {"persona": persona, "summary": summaries}
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"✅ Output saved to {output_path}")

# Entry point
if __name__ == "__main__":
    persona = input("Enter persona (e.g. student, teacher, journalist): ").strip().lower()
    filename = input("Enter PDF filename (e.g. sample.pdf): ").strip()
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    input_path = os.path.join("input", filename)
    output_path = os.path.join("output", f"{persona}_{filename[:-4]}.json")

    os.makedirs("output", exist_ok=True)

    if os.path.exists(input_path):
        generate_persona_summary(input_path, persona, output_path)
    else:
        print("❌ PDF file not found in /input")
