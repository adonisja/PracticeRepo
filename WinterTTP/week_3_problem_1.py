camelCase = input("Enter a name: ") #Takes a name in camel case
snake_case = ""
for i in range(len(camelCase)): #iterates through the string
    if camelCase[i].isupper(): #checks each character of the string for the occurence of an uppercase letter
        print(f'Letter: {camelCase[i]}, Index: {i}')
        snake_case +=  "_" + camelCase[i].lower() #if a capital letter is found, then a '_' is added before it followed by the lower case version of the letter
    else:
        snake_case += camelCase[i] #adds each letter of camelCase to snake_case per loop
print(snake_case)