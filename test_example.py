import unittest
from run import read_file, count_lines, count_sentences, count_words

class TestExample(unittest.TestCase):
    filename = "test.txt"
        
    def test_count_lines(self):
        text = read_file(self.filename)
        lines = count_lines(content=text)
        self.assertEqual(lines, 5)
        
    def test_count_sentences(self):
        text = read_file(self.filename)
        sentences = count_sentences(content=text)
        self.assertEqual(sentences, 6)
        
    def test_count_words(self):
        text = read_file(self.filename)
        words = count_words(content=text)
        self.assertEqual(words, 89)
            
if __name__ == "__main__":
    unittest.main()