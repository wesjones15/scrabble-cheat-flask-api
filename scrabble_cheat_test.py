import unittest
from findScrabbleWordsFromLetters import getScrabbleWordsFromLetters#, filterWordListByWordLength, filterOutUnusedLetters, filterWordListByLetterFrequency
from getBestScoringWords import getBestScoringWords#, getPointValueOfWord, convertLetterToPointValue

class TestBothModules(unittest.TestCase):
    def test_both(self):
        letters = ["A","T","R","F","E","I","X"]
        word_list = getScrabbleWordsFromLetters(letters)
        best_words = getBestScoringWords(word_list, limit=1)
        expected = [["FIXATE", 16]]
        case = "should return best scoring word and its point value"
        self.assertEqual(best_words, expected, case)
        
if __name__ == "__main__":
    unittest.main()