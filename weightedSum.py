lookupTable = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'a' : 10,
    'b' : 11,
    'c' : 12,
    'd' : 13,
    'e' : 14,
    'f' : 15
}

lookupTable2 = {
    0 : '0',
    1 : '1',
    2 : '2',
    3 : '3',
    4 : '4',
    5 : '5',
    6 : '6',
    7 : '7',
    8 : '8',
    9 : '9',
    10 : 'a',
    11 : 'b',
    12 : 'c',
    13 : 'd',
    14 : 'e',
    15 : 'f'
}

print("Enter the base you wish to convert to decimal")
base = int(input("You may ONLY choose from base 2 (binary), base 4, base 8 (octal), or base 16 (hexadecimal): "))
print("base = ",base)
while base != 2 or base != 4 or base != 8 or base != 16:
    base = int(input("Invalid input! You may ONLY choose from base 2 (binary), base 4, base 8 (octal), or base 16 (hexadecimal): "))
    print("base = ",base)
num = str(input("Enter the value you wish to convert to decimal: "))
i = int(len(num) - 1)
sum = 0


while i >= 0:
    if base != 16:
        x:int = int(num[i])
        sum = sum + x * 10**x
    else:
        x:int = int(lookupTable[num[i]])
        sum = sum + lookupTable[x] * 10**x
    i += 1
    x -= 1

print("The original base value is: ", base)
print("The original number is: ", num)
print("The converted number in decimal is: ", sum)