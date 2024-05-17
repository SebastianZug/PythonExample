# read a text from file commanline and print it
# Usage: python run.py <filename>
# Example: python run.py test.txt

import sys
from langdetect import detect, detect_langs

def read_file(filename):
    try:
        text = ""
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error: {e}")
    return text
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <filename>")
    else:
        text = read_file(sys.argv[1])
        print(detect_langs(text))