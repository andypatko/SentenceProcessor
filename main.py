#   1) open text file and process the file
#   - remove punctuation
#   - convert all to capital letters
#   - collect all words in an array

import re
import string
import os
import sys
import statistics


with open(os.path.join(sys.path[0], "sentences.txt"), "r") as file:

    # Processing file to remove punctuation & lowercase.
    # Fullstops and /n are not removed as they will be used to detect a sentence.
    data = file.read()
    data = data.lower()
    punctuations = '''!()-[]{};:"',<>/?@#$%^&*_~'''

    processedData = ""
    for char in data:
        if char not in punctuations:
            processedData += char


    wordList = []
    sentenceIndex = []
    currentWord = ""
    fullstopPos = 0
    #A value stating the position of a fullstop by counting of words. Is useful for processing sentences

    # Generating a word list and detecting sentences
    for i in range(len(processedData)):
        if currentWord.isalpha() == True and processedData[i].isalnum() == False:
            wordList.append(currentWord)
            currentWord = ""
            fullstopPos += 1

            # A sentence is detected when an alphanum character is followed by a fullstop, then non-alphanumeric
            # This method handles exceptions such as numbers with decimal places and elipses

        elif processedData[i].isalnum() == True:
            currentWord = currentWord + processedData[i]

        if processedData[i - 1].isalnum() == True \
                and processedData[i] == "." \
                and (processedData[min(i + 1, len(processedData) - 1)].isalnum() == False):
            #processedData[i] cannot go over len(processedData - 1) to avoid indexerror
            sentenceIndex.append(fullstopPos)

def words_in_sentence():
    wordsinsentence = ""

    for i in range(len(sentenceIndex)):
        wordsinsentence = wordsinsentence + "Words in sentence " + str(i + 1) + ": " + \
                          str(min(sentenceIndex[i], abs(sentenceIndex[i] - sentenceIndex[i - 1]))) + "\n"
        #Difference between number of words between fullstop, min function prevents the list underflow when using i -1
    print(wordsinsentence)

def length_freq_dict():
    lengthfreqdict = ""

    wordlengthcount = []
    for word in wordList:
        if len(word) > len(wordlengthcount):
            for i in range(len(word) - (len(wordlengthcount))):
                wordlengthcount.append(0)

        wordlengthcount[len(word)-1] += 1

    for i in range(len(wordlengthcount)):
        lengthfreqdict = lengthfreqdict + str(i+1) + " letter long word count: " + str(wordlengthcount[i]) +"\n"

    print(lengthfreqdict)

def most_common_word():
    print("Most common word: " + statistics.mode(wordList))
#


words_in_sentence()
length_freq_dict()
most_common_word()



