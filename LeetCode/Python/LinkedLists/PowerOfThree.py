import math
def isPowerOfThree(n):
    if n <= 0:
        return False
    else:
        return math.log10(n)/math.log10(3) % 1 == 0 

def main():
    n = 81
    print(isPowerOfThree(n))

if __name__ == '__main__':
    main()