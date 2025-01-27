def Fibonacci(A, n):
    fib_sum = 1
    for i in range(len(A), n):
        fib_sum = A[-1] + A[-2]
        A.append(fib_sum)
    return A

def main():
    A = [1, 1]
    n = 100
    print(Fibonacci(A, n))

if __name__ == '__main__':
    main()

'''Write a function that computes the list of the first 100
 Fibonacci numbers. The first two Fibonacci numbers are 1 and 1.
The n+1-st Fibonacci number can be computed by adding the n-th
and the n-1-th Fibonacci number. The first few are
therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8'''