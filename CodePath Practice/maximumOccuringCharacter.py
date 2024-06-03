def maximumOccuringCharacter(text):
    # Write your code here
    dict = {}
    for i in text:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    max = 0
    maxChar = ''
    for i in dict:
        if dict[i] > max:
            max = dict[i]
            maxChar = i
    return maxChar

def main():
    text = "aabbcc"
    result = maximumOccuringCharacter(text)
    print(f'The Maximum Occuring Character is {result}')


if __name__ == '__main__':
    main()
    
