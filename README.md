# Intelligent Document Analyst — Connect What Matters

> **Theme:** “Connect What Matters — For the User Who Matters”  
> Build a system that acts as an intelligent document analyst, extracting and prioritizing the most relevant sections from a collection of documents based on a specific persona and their job-to-be-done.

---


- `input/` — Place your input PDF documents here (minimum 3 files).
- `output/` — JSON outputs of the analysis will be saved here.
- `persona_extractor.py` — Main processing script that performs persona-based document analysis.
- `requirements.txt` — Python package dependencies.
- `approach_explanation.md` — Methodology description.
- `README.md` — This documentation file.

---

## Quickstart Guide

### Prerequisites

- Python 3.7 or above

---

### Running the Tool

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Place your PDF documents (minimum 3) inside the `input/` directory.
3. Run the main script:
    ```
    python persona_extractor.py
    ```
4. You will be prompted to enter:
    - **Persona** (e.g., `PhD Researcher`, `Investment Analyst`, `Student`)
    - **Job-to-be-Done** (a description of the task, e.g., `"Prepare a literature review on..."`)
5. The output JSON file (e.g., `output/PhD_Researcher_analysis_output.json`) will be generated automatically in the `output/` folder.

---

## Troubleshooting

- **No output or empty results:**  
  Verify your PDFs contain readable searchable text (not scanned images). Consistent formatting helps extraction quality.

- **File not found errors:**  
  Ensure PDF files are correctly named and placed under `input/`.

- **Processing time too long:**  
  Run on documents fewer than 5 files or reduce document sizes/content if possible.

- **Model errors or memory issues:**  
  Make sure you’re running with CPU-only environments and have at least 4GB RAM free.

---

## Credits

- Developed by [Team: MaHa]
- Uses [PyMuPDF](https://github.com/pymupdf/PyMuPDF) for PDF parsing
- Uses [Hugging Face Transformers](https://huggingface.co/transformers/) for summarization
- Inspired by the “Connecting the Dots” Challenge: Rethink Reading initiative



Happy analyzing!  
Connect what matters, for the user who matters.


