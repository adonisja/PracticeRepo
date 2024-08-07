def fib(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2, len(arr)):
        arr[i] = arr[i-1] + arr[i-2]
    
    return arr

def main():
    num = int(input('Enter a number: '))
    print(f'The Fibonacci sequence of {num} is : {fib(num)}')

if __name__ == '__main__':
    main()
