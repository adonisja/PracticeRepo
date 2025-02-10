def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    
    return b


def main():
    num = int(input('Enter a number: '))
    print(f'The Fibonacci sequence of {num} is : {fib(num)}')

if __name__ == '__main__':
    main()