import unittest
from findScrabbleWordsFromLetters import getScrabbleWordsFromLetters, filterWordListByWordLength, filterOutUnusedLetters, filterWordListByLetterFrequency

class TestGetScrabbleWords(unittest.TestCase):
    def test_getScrabbleWordsFromLetters(self):
        letters = ["W","E","S","T","E","R","N"]
        result = len(getScrabbleWordsFromLetters(letters))
        expected = 167
        case = "should return words that are spellable with given input letters"
        self.assertEqual(result, expected, case)
    
    def test_filterWordListByWordLength(self):
        letters = ["W","E","S","T","E","R","N"]
        word_list = ["WESTERN","BEEFJERKY","PANCAKEMIX","WEST","WESTSOUTHWEST","WEASEL"]
        result = filterWordListByWordLength(letters, word_list)
        expected = ["WESTERN", "WEST", "WEASEL"]
        case = "should filter list by word length"
        self.assertEqual(result, expected, case)
    
    def test_filterOutUnusedLetters(self):
        letters = ["W","E","S","T","E","R","N"]
        word_list = ["WESTERN","BEEFJERKY","WEWEWEWE","PANCAKEMIX","WEST","WESTSOUTHWEST","WEASEL"]
        result = filterOutUnusedLetters(letters, word_list)
        expected = ["WESTERN","WEWEWEWE", "WEST"]
        case = "should return filtered word list with words containing only input letters"
        self.assertEqual(result, expected, case)

    def test_filterWordListByLetterFrequency(self):
        letters = ["W","E","S","T","E","R","N"]
        word_list = ["WESTERN","WEEE","WEEEE", "WEE"]
        result = filterWordListByLetterFrequency(letters, word_list)
        expected = ["WESTERN","WEE"]
        case = "should filter out words that exceed frequency of any input letter"
        self.assertEqual(result, expected, case)
    
if __name__ == '__main__':
    unittest.main()