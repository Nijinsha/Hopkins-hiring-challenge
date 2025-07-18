import os
from hopkins.core.pdf_reader import extract_text_from_pdf
from hopkins.core.llm_summerizer import summarize_to_json
from hopkins.core.ppt_writer import write_pptx
from hopkins.core.markdown_writer import write_markdown
from hopkins.core.utils import (
    load_text_file, save_json, ensure_dir_exists, get_output_dir
)

class ExecutiveSummaryGenerator:
    def __init__(self, input_path):
        self.input_path = input_path
        self.output_dir = get_output_dir(input_path)
        ensure_dir_exists(self.output_dir)

    def extract_text(self):
        ext = os.path.splitext(self.input_path)[1].lower()
        if ext == '.pdf':
            return extract_text_from_pdf(self.input_path)
        elif ext == '.txt':
            return load_text_file(self.input_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    def run(self):
        cim_text = self.extract_text()
        print(f"✅ Extracted {len(cim_text)} characters.")

        summary_data = summarize_to_json(cim_text)
        json_path = os.path.join(self.output_dir, "executive_summary.json")
        save_json(summary_data, json_path)
        print(f"✅ JSON saved: {json_path}")

        md_path = os.path.join(self.output_dir, "executive_summary.md")
        write_markdown(summary_data, md_path)

        pptx_path = os.path.join(self.output_dir, "mini_deck.pptx")
        write_pptx(summary_data, pptx_path)