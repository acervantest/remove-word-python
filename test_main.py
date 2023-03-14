import unittest
from main import remove_word_from_sentence


class TestRemoveWordFromSentence(unittest.TestCase):
    def testRemoveWordFromSentence(self):
        self.assertEqual(remove_word_from_sentence('this is a test', 'test'), 'this is a ')
        self.assertEqual(remove_word_from_sentence('this test is good', 'test'), 'this  is good')
        self.assertEqual(remove_word_from_sentence('programmers can write code that is computer-understandable while '
                                                   'Good programmers write code understandable by humans', 'write'),
                         'programmers can  code that is computer-understandable while Good programmers  code '
                         'understandable by humans')

    def testTestWordValues(self):
        with self.assertRaises(ValueError):
            remove_word_from_sentence('this is a test', '')
        with self.assertRaises(ValueError):
            remove_word_from_sentence('', 'test')
        with self.assertRaises(ValueError):
            remove_word_from_sentence('', '')

    def testTestWordTypes(self):
        with self.assertRaises(TypeError):
            remove_word_from_sentence('this is a test', 3)
        with self.assertRaises(TypeError):
            remove_word_from_sentence(True, 'test')
        with self.assertRaises(TypeError):
            remove_word_from_sentence('', 3+5j)
