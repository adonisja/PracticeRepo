greeting = input("Enter a greeting: ")
greeting = greeting.lower() #changes the user input to all lower case
greetingList = greeting.split() # splits the user input into a list of individual words
print(greetingList)
if 'hello' in greetingList[0]: #checks if the first list contains the word "hello"
    print('$0')                 
elif greetingList[0][0] == 'h': #checks if the first word in the list starts with a 'h' (index 0 of index 0 of list 'greetingList')
    print('$20')
else:           #if none of the above were true then the user wins $100
    print('$100')
