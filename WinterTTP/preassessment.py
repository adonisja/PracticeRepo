import random
import time


def ArrayInitializer():
    numArray = []
    reversedArray = []
    for x in range(10):
        i = random.randrange(1,10)
        numArray.append(i)
        reversedArray.insert(0,numArray[x])
    print(f'NumArray: {numArray}')
    print(f'ReversedArray: {reversedArray}')


def checkPalindrome():
    word = input("Enter a palindrome: ")
    if word[::] == word[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
   

def main():
    ArrayInitializer()
    checkPalindrome()

main()