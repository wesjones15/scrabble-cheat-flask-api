from operator import itemgetter

def getBestScoringWords(word_list):
    sorted_list = [] # 2D list with word and score
    for word in word_list:
        sorted_list.append([word, getPointValueOfWord(word)])
    sorted_list = sorted(sorted_list, key=itemgetter(1), reverse=True)
    return sorted_list

def getPointValueOfWord(word):
    score = 0
    for letter in word:
        score += convertLetterToPointValue(letter)
    return score

def convertLetterToPointValue(letter):
    tileScoreGroups = [ 
        [['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1],
        [['D', 'G'], 2],
        [['B', 'C', 'M', 'P'], 3],
        [['F', 'H', 'V', 'W', 'Y'], 4],
        [['K'], 5],
        [['J', 'X'], 8],
        [['Q', 'Z'], 10]
    ]
    value = 0
    for letters, points in tileScoreGroups:
        if letter in letters:
            value = points
    return value

if __name__ == '__main__':
    convertLetterToPointValue("A")