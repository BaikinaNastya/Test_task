import unittest
import text_stat
import os


class Test_text_stat(unittest.TestCase):
    path = os.path.abspath(os.path.join(os.getcwd(), "Ex2", "Files for tests"))

    def test_text_stat_file_not_found(self):
        filename = "Not_existing_file.txt"
        result = text_stat.text_stat(filename)
        expected = {"error": "Файл не найден."}
        self.assertDictEqual(result, expected)

    def test_text_stat_not_a_text_file(self):
        filename = os.path.join(self.path, "image.png")
        result = text_stat.text_stat(filename)
        expected = {"error": "Файл не является текстовым."}
        self.assertDictEqual(result, expected)
    
    def test_text_stat_empty_file(self):
        filename = os.path.join(self.path, "text2.txt")
        result = text_stat.text_stat(filename)
        expected = {"error": "Количество слов или символов в файле равно нулю."}
        self.assertDictEqual(result, expected)
    
    def test_text_stat_no_words(self):
        filename = os.path.join(self.path, "text3.txt")
        result = text_stat.text_stat(filename)
        expected = {"error": "Количество слов или символов в файле равно нулю."}
        self.assertDictEqual(result, expected)
    
    def test_text_stat_example(self):
        filename = os.path.join(self.path, "text.txt")
        result = text_stat.text_stat(filename)
        expected = {
            "а": (0.1081, 0.5), 
            "б": (0.0, 0.0), 
            "в": (0.0541, 0.25), 
            "г": (0.0, 0.0), 
            "д": (0.027, 0.125), 
            "е": (0.0811, 0.375), 
            "ё": (0.0, 0.0), 
            "ж": (0.0, 0.0), 
            "з": (0.0, 0.0), 
            "и": (0.027, 0.125), 
            "й": (0.0, 0.0), 
            "к": (0.1081, 0.25), 
            "л": (0.027, 0.125), 
            "м": (0.027, 0.125), 
            "н": (0.0, 0.0), 
            "о": (0.0, 0.0), 
            "п": (0.027, 0.125), 
            "р": (0.027, 0.125), 
            "с": (0.0541, 0.25), 
            "т": (0.027, 0.125), 
            "у": (0.0, 0.0), 
            "ф": (0.0, 0.0), 
            "х": (0.0, 0.0), 
            "ц": (0.0, 0.0), 
            "ч": (0.0, 0.0), 
            "ш": (0.0, 0.0), 
            "щ": (0.0, 0.0), 
            "ъ": (0.0, 0.0), 
            "ы": (0.0, 0.0), 
            "ь": (0.0, 0.0), 
            "э": (0.0, 0.0), 
            "ю": (0.0, 0.0), 
            "я": (0.0, 0.0), 
            "a": (0.027, 0.125), 
            "b": (0.0, 0.0), 
            "c": (0.0, 0.0), 
            "d": (0.027, 0.125), 
            "e": (0.0, 0.0), 
            "f": (0.0, 0.0), 
            "g": (0.027, 0.125), 
            "h": (0.0, 0.0), 
            "i": (0.0, 0.0), 
            "j": (0.0, 0.0), 
            "k": (0.0, 0.0), 
            "l": (0.0, 0.0), 
            "m": (0.0, 0.0), 
            "n": (0.0, 0.0), 
            "o": (0.0541, 0.125), 
            "p": (0.0, 0.0), 
            "q": (0.0, 0.0), 
            "r": (0.0, 0.0), 
            "s": (0.0, 0.0), 
            "t": (0.0, 0.0), 
            "u": (0.0, 0.0), 
            "v": (0.0, 0.0), 
            "w": (0.0, 0.0), 
            "x": (0.0, 0.0), 
            "y": (0.0, 0.0), 
            "z": (0.0, 0.0), 
            "paragraph_amount": 3, 
            "word_amount": 8, 
            "bilingual_word_amount": 1
            }
        self.assertDictEqual(result, expected)


if __name__ == "__main__":
    unittest.main()