def shortestToChar(s: str, c: str):
    ans = [len(s)] * len(s)
    prev = None
    for i in range(len(s)):
        char = s[i]
        if char == c:
            prev = i
            ans[i] = 0
        elif prev:
                ans[i] = min(ans[i], abs(prev_c_index - i))

    prev_c_index = None
    for i in range(len(s)-1, -1, -1):
        char = s[i]
        if char == c:
             prev = i
             ans[i] = 0
        elif prev:
             ans[i] = min(ans[i], abs(prev - i))


def main():
    s = "loveleetcode"
    c = "e"
    print(shortestToChar(s, c))

if __name__ == '__main__':
    main()