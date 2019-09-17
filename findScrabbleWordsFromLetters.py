def getScrabbleWordsFromLetters(letters):
    return word_list

def filterOutUnusedLetters(letters):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    scrabble_dictionary = [line.rstrip('\n') for line in open('./assets/scrabble_word_list.txt')]
    unused_letters_list = list(filter(lambda letter: letter not in letters, alphabet))
    
    # filter scrabble list by length of input letters
    print(len(scrabble_dictionary))
    filtered_scrabble_word_list = list(filter(lambda word: len(word) <= len(letters), scrabble_dictionary))
    
    # filter scrabble list to exclude unused letters
    print(len(filtered_scrabble_word_list))
    for letter in unused_letters_list:
        filtered_scrabble_word_list = list(filter(lambda word: letter not in word, filtered_scrabble_word_list))
    print(len(filtered_scrabble_word_list))
    filtered_list = filtered_scrabble_word_list
    return filtered_list

def filterWordListByLetterFrequency(letters, word_list):
    print(len(word_list))
    for letter in letters:
        filtered_list = list(filter(lambda word: word.count(letter) <= letters.count(letter), word_list))
    print(len(filtered_list))
    return filtered_list

def getFrequencyOfLetterInWord(letter, word):
    frequency = word.count(letter)
    return frequency

if __name__ == '__main__':
    my_letters = ["A","B","C","A","E","P"]
    filter_lsit = filterOutUnusedLetters(my_letters)
    filterWordListByLetterFrequency(my_letters, filter_lsit)
    # getFrequencyOfLetterInWord("A", "BANANA")