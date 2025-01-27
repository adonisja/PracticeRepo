def compress(s):
    if s is None:
        return "The string is empty"
    count = 1
    res = ''
    # input is a alpha only string and output is also an alphanumeric string
    if not s.isalpha():
        return "Invalid String"
    # Iterate over the values in the string
    for i in range(len(s)):
        # check if the subsequent letters are the same as this
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            if count > 1:
                res += str(count) + s[i]
            else:
                res += s[i]
            count = 1
    return res

def main():
    tests = ["aaabbc", 'ssssbbz', 'ccaaatsss', 'ppoppppp', 'nnneeeeeeeeeeeezz', 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy']
    for x in tests:
        print(f'{x}: {compress(x)}')

if __name__ == '__main__':
    main()