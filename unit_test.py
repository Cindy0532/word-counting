from project import *
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        file = open("text.txt", 'r')
        self.text = file.read()
        file.close()

    def test_wc(self):
        expected = {'in': 5, 'this': 2, 'project': 1, 'you': 1, 'need': 1, 'to': 1, 'go': 1, 'through': 1, 'all': 1, 'software': 1, 'engineering': 1, 'practices': 1, 'with': 1, 'a': 1, 'small': 1, 'dfdt': 1, 'jjl': 1, 'time': 1, 'my': 1, 'ininin': 1, 'dsfsd': 1}
        word_list =WordStatistics.words(self.text)
        self.assertDictEqual(WordStatistics.wc(word_list), expected)

    def test_line_count(self):
        self.assertTrue(WordStatistics.line_count(self.text), 2)

    def test_char_count(self):
        self.assertTrue(WordStatistics.char_count(self.text), 146)

    def test_replacement(self):
        expected = 'In this project, you need to go through all software engnameeernameg practices with a small     dfdt   name    jjl. name time name this my name ininin.\ndsfsd.'
        replaced = WordStatistics.replacement('in', 'name', self.text)
        self.assertTrue(replaced, expected)

if __name__ == '__main__':
    unittest.main()

