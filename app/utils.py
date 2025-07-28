import fitz  # PyMuPDF
import json
import os

def load_input_metadata(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    filenames = [doc["filename"] for doc in data["documents"]]
    persona = data["persona"]["role"]
    job = data["job_to_be_done"]["task"]
    return filenames, persona, job, data

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    items = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text:
                        continue
                    items.append({
                        "level": "H1",  # placeholder
                        "text": text,
                        "page": page_num
                    })
    return {"outline": items}

def rank_sections(text, persona, job):
    score = 0
    keywords = (persona + " " + job).lower().split()
    for word in keywords:
        if word in text.lower():
            score += 1
    return score
