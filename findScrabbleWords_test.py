import unittest
from findScrabbleWordsFromLetters import getScrabbleWordsFromLetters, filterOutUnusedLetters, filterWordListByLetterFrequency, getFrequencyOfLetterInWord

class TestGetScrabbleWords(unittest.TestCase):
    def test_getScrabbleWordsFromLetters(self):
        letters = "WESTERN"
        result = getScrabbleWordsFromLetters(letters)
        expected = [""]
        case = "should return words that are spellable with given input letters"
        self.assertEqual(result, expected, case)
    
    def test_filterOutUnusedLetters(self):
        letters = "WESTERN"
        result = filterOutUnusedLetters(letters)
        expected = [""]
        case = "should return filtered word list with words containing only input letters"
        self.assertEqual(result, expected, case)

    def test_filterWordListByLetterFrequency(self):
        letters = "WESTERN"
        result = filterWordListByLetterFrequency(letters, word_list)
        expected = [""]
        case = "should further filter word list to only include words that do not exceed frequency of any input letter"
        self.assertEqual(result, expected, case)
        
    def test_getFrequencyOfLetterInWord(self):
        letter = "A"
        word = "BANANA"
        result = getFrequencyOfLetterInWord(letter, word)
        expected = 3
        case = "should return number of times given letter appears in a given word"
        self.assertEqual(result, expected, case)
    
    
if __name__ == '__main__':
    unittest.main()