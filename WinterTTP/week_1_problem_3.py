import emoji

def emoticonConverter(word):
    for x in range(len(word)-1):
        if word[x] == ':' and word[x+1] == ')':
            print(word.replace(":)", "\N{slightly smiling face}"))
        elif word[x] == ':' and word[x+1] == '(':
            print(word.replace(":(", "\N{slightly frowning face}"))
        elif x == len(word)-2 and word[x] != ':':
            print(word)


if __name__ == '__main__':
    word = input("Enter your text: ")
    emoticonConverter(word)
