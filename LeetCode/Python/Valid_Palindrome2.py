def validPalindrome(s: str) -> bool:
    # l,r = 0, len(s) - 1   #Create 2 pointers, one at the beginning and the other at the end of the string
    # while l < r:           #While both pointers havent met
    #     if s[l] == s[r]:   #increment l and decrement r if both letters are the same
    #         l += 1
    #         r -= 1
    #     else:
    #         #else drop the left OR right most letters
    #         dropL, dropR = s[l+1:r+1], s[l:r]
    #         #and return true or false depending on if the resulting string is a palindrome
    #         return (dropL == dropL[::-1] or dropR == dropR[::-1])
    # return True
    return s[:]==s[::-1]

def main():
    s = "acabbaa"
    print(validPalindrome(s))

if __name__ == '__main__':
    main()