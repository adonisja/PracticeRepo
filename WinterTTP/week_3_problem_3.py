text = input("What is your sentence: ")
'''Using the translate method to replace all occurences of vowels in your text with a null character
Breakdown: returns the unicode of each character in the dictionary given, maps each vowel to the
    Null Character then loops through the string and replaces each instance of the keys found to the new Null value
'''
text = text.translate({ord(i): None for i in 'AaEeIiOoUu'}) 
print(text)