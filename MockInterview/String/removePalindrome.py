def isPalindrome(s, i, j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return isPalindrome(s[i+1], s[j-1])

def main():
    s = "abb"
    pali = isPalindrome(s, 0, len(s)-1)
    print(2 - pali - (s == ""))

if __name__ == '__main__':
    main()