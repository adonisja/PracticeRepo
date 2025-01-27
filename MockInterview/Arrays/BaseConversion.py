def BaseConversion(num, b1, b2):
    # Convert from base b1 to base 10
    base10 = 0
    size = len(num)
    for i in range(size):
        base10 += num[i] * (b1 ** (size - i - 1))
    
    # Convert from base 10 to base b2
    res = []
    while base10 > 0:
        res.append(base10 % b2)
        base10 //= b2
    
    return res[::-1]  # Reverse the result to get the correct order
        


def main():
    num = [2, 1, 0]
    b1 = 3
    b2 = 10
    print(f'Your number {num} base {b1} in base {b2} is: {BaseConversion(num, b1, b2)}')



if __name__ == '__main__':
    main()

'''Write a function that takes a list of numbers,
a starting base b1 and a target base b2 and
interprets the list as a number in base b1 and converts it
into a number in base b2 (in the form of a list-of-digits).
So for example [2,1,0] in base 3 gets converted to base 10
as [2,1].
'''