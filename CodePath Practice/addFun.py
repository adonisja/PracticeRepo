def addFun(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 2
    return addFun(n-1) + addFun(n-2)

def main():
    n = 6
    result = addFun(n)
    print(f'The sum of the first {n} terms is {result}')

if __name__ == '__main__':
    main()
    