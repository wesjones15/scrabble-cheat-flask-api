import unittest
from getBestScoringWords import getBestScoringWords, getPointValueOfWord, convertLetterToPointValue

class TestBestWords(unittest.TestCase):
    def test_getBestScoringWords(self):
        word_list = ["DOG", "A", "ZEBRA"]
        result = getBestScoringWords(word_list)
        expected = [["ZEBRA", 16], ["DOG", 5], ["A", 1]]
        case = "should sort word list by word score"
        self.assertEqual(result, expected, case)

    def test_getPointValueOfWord(self):
        word = "WESTERN"
        result = getPointValueOfWord(word)
        expected = 10
        case = "should return point value of given word"
        self.assertEqual(result, expected, case)

    def test_convertLetterToPointValue(self):
        letter = "A"
        result = convertLetterToPointValue(letter)
        expected = 1
        case = "should return point value of given letter"
        self.assertEqual(result, expected, case)
        
    def test_BestWordsLength(self):
        word_list = ["DOG", "DOGS", "DOGSXXX", "DOGSXXXZZZ"]
        result = len(getBestScoringWords(word_list))
        expected = 3
        case = "should only return top 3 words"
        
    def test_returnOneWord(self):
        word_list = ["DOG", "A", "ZEBRA"]
        result = getBestScoringWords(word_list,limit=1)
        expected = [["ZEBRA", 16]]
        case = "should return only one word"
        self.assertEqual(result, expected, case)
        
        
if __name__ == '__main__':
    unittest.main()