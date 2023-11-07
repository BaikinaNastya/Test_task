import unittest
import roman_numerals_to_int


class Test_roman_numerals_to_int(unittest.TestCase):
    def test_roman_numerals_to_int_example_1(self):
        str = "MCDXL"
        result = roman_numerals_to_int.roman_numerals_to_int(str)
        expected = 1440
        self.assertEqual(result, expected)

    def test_roman_numerals_to_int_example_2(self):
        str = "MCMLXXIV"
        result = roman_numerals_to_int.roman_numerals_to_int(str)
        expected = 1974
        self.assertEqual(result, expected)

    def test_roman_numerals_to_int_none_1(self):
        str = "XXIXVII"
        result = roman_numerals_to_int.roman_numerals_to_int(str)
        expected = None
        self.assertEqual(result, expected)

    def test_roman_numerals_to_int_none_2(self):
        str = "MCMLLIL"
        result = roman_numerals_to_int.roman_numerals_to_int(str)
        expected = None
        self.assertEqual(result, expected)
    
    def test_roman_numerals_to_int_none_3(self):
        str = "MXCD"
        result = roman_numerals_to_int.roman_numerals_to_int(str)
        expected = None
        self.assertEqual(result, expected)

    def test_roman_numerals_to_int_none_4(self):
        str = "MXVVI"
        result = roman_numerals_to_int.roman_numerals_to_int(str)
        expected = None
        self.assertEqual(result, expected)

    def test_roman_numerals_to_int_none_5(self):
        str = "MCCCCXI"
        result = roman_numerals_to_int.roman_numerals_to_int(str)
        expected = None
        self.assertEqual(result, expected)

    def test_roman_numerals_to_int_none_6(self):
        str = ""
        result = roman_numerals_to_int.roman_numerals_to_int(str)
        expected = None
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()