#Solution for Dail Programmer challenge #380
#https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

import re
import requests
import collections
import itertools

def Smooshed_Morse(Word):
    #Changes words to Smooshed morse code    
    Morse='.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'
    Morse_lst = Morse.split()
    Mword = []
    for lett in Word:
        Mword.append(Morse_lst[ord(lett)-97])
    return(''.join(Mword))

def Perfectly_balanced(Word):
    Dot_count = 0
    Dash_count = 0
    for lett in Word:
        if lett == '.':
            Dot_count+=1
        else:
            Dash_count+=1
    if Dot_count == Dash_count:
        return True

if __name__ == "__main__":
    print('Check if smooshed morse function works')    
    print(Smooshed_Morse('sos'))
    print(Smooshed_Morse('daily'))
    print(Smooshed_Morse('programmer'))
    print(Smooshed_Morse('bits'))
    print(Smooshed_Morse('three'))

    #Bonus challenges
    #Fetch the world list
    url = 'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt'
    Word_get  = requests.get(url)
    Word_list = re.findall(r'[\w]{2,}',Word_get.text)
        
    #Create morse code for all words
    Morse_list = []
    for Word in Word_list:
        Morse_list.append(Smooshed_Morse(Word))
#Bonus 1
    #Create counter object and extract key which occurs 13 times
    MorseCounter = collections.Counter(Morse_list)
    print('Bonus #1: ', list(MorseCounter.keys())[list(MorseCounter.values()).index(13)])
#Bonus 2
    #Find only string that has 15 consecutive dashes
    Mfile = '\n'.join(Morse_list)
    W = re.search(r'[\S]*[/-]{15}[\S]*',Mfile)
    print('Bonus #2: ', Word_list[(Morse_list.index(W[0]))])
#Bonus 3
    #Find a 21-letter word that has the same number of dots and dashes
    for Word in Word_list:
        if len(Word) == 21 and Perfectly_balanced(Smooshed_Morse(Word)) == True:
            print('Bonus #3: ', Word)
#Bonus 4
    #Find the only 13-letter world that encodes to a palindrome
    for Word in Word_list:
        if len(Word) == 13 and Smooshed_Morse(Word) == ''.join(reversed(Smooshed_Morse(Word))):
           print('Bonus #4: ', Word)
           break
#Bonut 5
    #Find 13-character sequence that does not appear in the encoding of any word
    Codes = (list(itertools.product('.-', repeat =13)))
    Codes = list(map(''.join,Codes))
    print('Bonus #5: ')
    for code in Codes:
        for morse in Morse_list:
            if code in morse:
                break
        else:
            print(code)
