import unittest
import cap

class CapTest(unittest.TestCase):
    def test_one_word(self):
        text='python'
        r=cap.cap_text(text)
        self.assertEqual(r,'Python')

    def test_mult_words(self):
        text='learning python'
        r=cap.cap_text(text)
        self.assertNotEqual(r,'Learning Python')

    def test_titile(self):
        text='learning python3'
        r=cap.cap_titiles(text)
        self.assertEqual(r,'Learning Python3')
    def test_titile2(self):
        text='learning python2'
        r=cap.cap_titiles(text)
        self.assertNotEqual(r,'learning Python2')

if __name__ == '__main__':
    unittest.main()