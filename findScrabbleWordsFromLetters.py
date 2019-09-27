def getScrabbleWordsFromLetters(letters):
    with open('./assets/scrabble_word_list.txt') as file:
        word_list = [line.rstrip('\n') for line in file]
    
    filtered_list = filterWordListByWordLength(letters, word_list)
    # print("WORD LEN",len(filtered_list))
    # The React app can't get past here
    filtered_list = filterOutUnusedLetters(letters, filtered_list)
    # print("LETTERS OUT",len(filtered_list))
    filtered_list = filterWordListByLetterFrequency(letters, filtered_list)
    # print('WORD FREQ',len(filtered_list))
    return filtered_list

def filterWordListByWordLength(letters, word_list):
    return list(filter(lambda word: len(word) <= len(letters), word_list))

def filterOutUnusedLetters(letters, word_list):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    unused_letters = list(filter(lambda letter: letter not in letters, alphabet))
    # print(unused_letters)
    filtered_list = word_list
    for letter in unused_letters:
        filtered_list = list(filter(lambda word: letter not in word, filtered_list))
    return filtered_list

def filterWordListByLetterFrequency(letters, word_list):
    filtered_list = word_list
    for letter in letters:
        filtered_list = list(filter(lambda word: word.count(letter) <= letters.count(letter), filtered_list))
    return filtered_list