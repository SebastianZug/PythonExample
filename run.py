# read a text from file commanline and print it
# print the number of lines, sentences and words the file includes
# Usage: python run.py <filename>
# Example: python run.py test.txt

import sys
import re
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

def count_lines(filename):
    read_file(filename)
    lines = text.splitlines()
    num_lines = len(lines)
    return num_lines

def count_sentences(filename):
    read_file(filename)
    sentences = re.findall(r'[.!?]', text)
    num_sentences = len(sentences)
    return num_sentences

def count_words(filename):
    read_file(filename)
    words = re.findall(r'\b\w+\b', text)
    num_words = len(words)
    return num_words
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <filename>")
    else:
        text = read_file(sys.argv[1])
        lines = count_lines(sys.argv[1])
        sentences = count_sentences(sys.argv[1])
        words = count_words(sys.argv[1])
        print(detect_langs(text))
        print(f"Number of lines: {lines}")
        print(f"Number of sentences: {sentences}")
        print(f"Number of words: {words}")