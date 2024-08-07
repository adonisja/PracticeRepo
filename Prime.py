import math
'''This is an efficient Program check if a number is Prime'''
def isPrime(num):
    if num < 2:         # Numbers less than 2 are not Prime
        return False
    if num == 2:        # 2 is the only Even Prime Number
        return True
    if num % 2 == 0:    # For efficiency check if the number is even
        return False 
    for i in range(3, int(math.sqrt(num))+1, 2):
            
        print(f'i: {i}')
        if num % i == 0:
            return False
    return True


def main():
    num = int(input("Enter a number: "))
    prime = isPrime(num)
    print(f'{num} is Prime' if prime else f'{num} is not prime')

if __name__ == '__main__':
    main()