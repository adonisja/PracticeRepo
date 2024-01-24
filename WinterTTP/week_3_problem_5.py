import sys

def checkCalories(fruit):
    fruitDict = { #Creates a dictionary with the list of top 20 fruits and their caloric content
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "cherries" : 100,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew melon" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapples" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "tangerine" : 50,
        "watermelon" : 80
    }
    if fruit in fruitDict:      #checks if the fruit listed is contained in the dictionary
        return fruitDict[fruit]     #returns the value assigned to the key if found
    else:
        sys.exit(fruit + " is not found!") #otherwise the program is terminated and an error message is outputted to the user

def main():
    fruit = input("Enter a fruit: ")
    fruit = fruit.lower()
    calories = checkCalories(fruit)
    print(f'{fruit} contain {calories} calories per serving')

main()