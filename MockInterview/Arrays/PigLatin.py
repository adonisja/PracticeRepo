def Piggify(phrase):
    wordList = phrase.split(' ')
    newPhrase = ''
    
    for word in wordList:
        word = word[1:] + word[0].lower() + 'ay'
        newPhrase += word + ' '
    newPhrase = newPhrase[0].upper() + newPhrase[1:]
    return newPhrase.strip()

def main():
    phrase = 'Hello my new friends' #input("What did the you say?: ")
    if len(phrase) == 0:
        print("I didn't hear you, please speak louder next time")
    else: 
        print(f'The pig said "{Piggify(phrase)}"')

if __name__ == '__main__':
    main()

'''Write function that translates a text to Pig Latin and back.
English is translated to Pig Latin by taking the first letter
of every word, moving it to the end of the word and adding ‘ay’.
“The quick brown fox” becomes “Hetay uickqay rownbay oxfay”.'''