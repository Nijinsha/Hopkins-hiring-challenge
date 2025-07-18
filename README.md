# Hopkins Coding Challenge: CIM Summarizer + Mini Deck Generator

## 🎯 Objective

Build a prototype that ingests a Confidential Information Memorandum (CIM) in PDF or TXT format and produces:

- A 1-page executive summary (Markdown)
- A 3-slide PowerPoint deck

## 💼 Context

Hopkins is building an AI analyst for private equity. This tool parses CIMs and generates investment-ready summaries and decks.

## 📥 Input

- A sample CIM in PDF or TXT format, including sections such as:
  - Company Overview
  - Financials
  - Market Opportunity
  - Risks

## 📤 Output

- **Executive Summary**: Markdown file with business overview, key financials, investment highlights, and risks.
- **Mini PowerPoint Deck**: 3 slides (Company Overview, Key Financials, Investment Rationale).

## 🚀 Usage

```bash
export OPENAI_API_KEY="YOUR_KEY_HERE"
pip install -r requirements.txt
python main.py <input_file.pdf|input_file.txt>
```

- Output files will be saved in a folder named after the input file (without extension), in the same directory as the input.

## 🏗️ Project Structure

```
hopkins/
│
├── main.py                      # CLI entry point
├── README.md
├── LICENSE
│
├── hopkins/                     # Main package (for importable code)
│   ├── __init__.py
│   │
│   ├── core/                    # Core business logic
│   │   ├── __init__.py
│   │   ├── workflow.py          # Orchestrates the end-to-end process
│   │   ├── pdf_reader.py        # PDF extraction logic
│   │   ├── llm_summerizer.py    # LLM summarization logic
│   │   ├── llm_prompt.py        # LLM prompt/schema (editable)
│   │   ├── markdown_writer.py   # Markdown output logic
│   │   ├── ppt_writer.py        # PowerPoint output logic
│   │   └── utils.py             # File/path helpers
```

## 📝 Extension Guidelines

- To tune the LLM prompt or schema, edit `hopkins/core/llm_prompt.py`.
- To add new input types, extend `ExecutiveSummaryGenerator.extract_text()` in `hopkins/core/workflow.py`.
- To add new output formats, create a new writer module and call it from the workflow.

---

For questions or improvements, please open an issue or PR.
