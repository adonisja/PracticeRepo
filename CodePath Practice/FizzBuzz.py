def FizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def main():
    n = int(input("Please Enter a number: "))
    FizzBuzz(n)

if __name__ == '__main__':
    main()