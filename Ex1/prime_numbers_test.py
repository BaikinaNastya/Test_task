import unittest
import prime_numbers


class Test_prime_numbers(unittest.TestCase):
    def test_prime_numbers_str(self):
        low, high = "low", "high"
        result = prime_numbers.prime_numbers(low, high)
        expected = []
        self.assertListEqual(result, expected)

    def test_prime_numbers_float(self):
        low, high = 4, 15.5
        result = prime_numbers.prime_numbers(low, high)
        expected = []
        self.assertListEqual(result, expected)

    def test_prime_numbers_negative_num(self):
        low, high = -5, 11
        result = prime_numbers.prime_numbers(low, high)
        expected = []
        self.assertListEqual(result, expected)

    def test_prime_numbers_negative_example_1(self):
        low, high = 5, 20
        result = prime_numbers.prime_numbers(low, high)
        expected = [5, 7, 11, 13, 17, 19]
        self.assertListEqual(result, expected)
    
    def test_prime_numbers_negative_example_2(self):
        low, high = 15, 10
        result = prime_numbers.prime_numbers(low, high)
        expected = []
        self.assertListEqual(result, expected)

    def test_prime_numbers_negative_example_3(self):
        low, high = 1, 29
        result = prime_numbers.prime_numbers(low, high)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()