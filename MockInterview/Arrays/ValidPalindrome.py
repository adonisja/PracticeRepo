def isPalindrome(word):
    if word[::] == word[::-1]:
        return True
    else:
        return False
    
def main():
    word = input('Enter a word: ')
    print(word + ' is a valid Palindrome' if isPalindrome(word) else word + ' is not a Palindrome')

if __name__ == '__main__':
    main()