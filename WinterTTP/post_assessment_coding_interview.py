def isAcronym(words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        letters = []
        for word in words:
            letters.append(word[0])
            print(word[0])
        print(str(letters))
        return s == "".join(letters)
            

def main():
     words = input("Your word: ")
     words = words.split()
     s = "smu"
     print(f'{words} is a valid Acronym' if isAcronym(words, s) is True else f'{words} is NOT a valid Acronym')

main()