import os
import json
from datetime import datetime
from utils import load_input_metadata, extract_outline, rank_sections

def main():
    input_json_path = "input/challenge1b_input.json"
    pdf_folder = "input/PDFs"
    output_path = "output/challenge1b_output.json"

    # Load metadata
    filenames, persona, job, metadata = load_input_metadata(input_json_path)

    results = []

    for filename in filenames:
        pdf_path = os.path.join(pdf_folder, filename)
        if not os.path.exists(pdf_path):
            continue

        outline = extract_outline(pdf_path)
        for item in outline["outline"]:
            score = rank_sections(item["text"], persona, job)
            results.append({
                "document": filename,
                "page": item["page"],
                "section_title": item["text"],
                "importance_rank": score
            })

    results = sorted(results, key=lambda x: -x["importance_rank"])

    final_output = {
        "metadata": {
            "input_documents": filenames,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.utcnow().isoformat()
        },
        "extracted_sections": results[:10]  # Top 10
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=2)

if __name__ == "__main__":
    main()
