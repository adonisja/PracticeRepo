answer = input("What is the meaning of life? ")
''' Uses the ternary operator to check if the user given answer is 42 and outputs yes if it is or no if it isn't
answer.lower() converts the user response to all lower case and checks it'''
print(f"{'Yes' if answer == '42' or answer.lower() == 'forty two' else 'No'}") 
