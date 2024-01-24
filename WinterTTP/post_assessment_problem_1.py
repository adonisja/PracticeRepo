def findLetters():
    word1 = input("Enter a string: ")
    word2 = input("Enter another string: ")
    word3 = word1 + word2 #concatenates the two inputted stings
    new_word = '' #creates a new variable to store the result

    for i, c in enumerate(word3):  #uses the enumerate function to loop through each character in "word3"
        if c.isalpha():            #checks if the character at this position is an alphabet
            new_word += c          # if it is then it is added to the result
    print("Letters used: ", set(new_word))     #outputs the result as a set to show the letters used in both strings






def main():
    findLetters()


main()