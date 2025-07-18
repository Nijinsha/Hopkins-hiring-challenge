import os
import json

def load_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def save_text_file(text, output_path):
    with open(output_path, 'w') as f:
        f.write(text)

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_output_dir(input_path):
    base = os.path.splitext(os.path.basename(input_path))[0]
    return os.path.join(os.path.dirname(input_path), base) 