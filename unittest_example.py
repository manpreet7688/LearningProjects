import unittest
import cap_unittestExample

class Test_Cap(unittest.TestCase):

    def single_word_cap(self):
        text = 'python'
        result = cap_unittestExample.cap_text(text)
        self.assertEqual(result, 'Python')

    def multi_words(self):
        text = 'my python'
        result = cap_unittestExample.cap_text(text)
        self.assertEqual(result,'My Python')

if __name__=='__main__':
    unittest.main()
