import re

def extract_name(text):
    match = re.search(r"Name:\s*(.*)", text)
    return match.group(1) if match else "Name not found"

def extract_file_number(text):
    match = re.search(r"File No:\s*(\d+)", text)
    return match.group(1) if match else "File number not found"
