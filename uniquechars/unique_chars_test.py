import unittest
from unique_chars import unique_characters

class test_unique_characters(unittest.TestCase):
    
    def test_string(self):
        self.assertTrue(unique_characters("anagram"))

        
    def test_list(self):
        self.assertTrue(unique_characters("anagram"))

   # Have to correct it later, remove the a
    def test_result(self):
        self.assertEqual(unique_characters("anagram"), "'m', 'n', 'g', 'a', 'r'" )


if __name__ == '__main__':
    unittest.main()