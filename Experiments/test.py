import sys
import limitCheck

lookup_table1 = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15
}

lookup_table2 = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'a',
    11:'b',
    12:'c',
    13:'d',
    14:'e',
    15:'f'
}

def count(base, limit_value, number_of_digits):
    carry = 0
    reset = 0
    for i in range(number_of_digits):
        for j in range(base**i, base**(i+1)):
            if j > int(limit_value):
                reset = 1
                break
            print(lookup_table2[lookup_table1[str(j)[0]] + carry], end="")
            if carry == 1:
                print("(carry)", end=" ")
                carry = 0
            if j % base == base - 1:
                print("(reset)", end=" ")
                carry = 1
        if reset == 1:
            break

base = int(input("Please enter the base you wish to work with: "))
while base not in [2, 4, 8, 10, 16]:
    base = int(input("Invalid base, please enter a base of either 2, 4, 8, 10 or 16: "))

    for i in range(number_of_digits):
        for j in range(base**i, base**(i+1)):
            if j > int(limit):
                reset = 1
                break
            print(lookup_table2[lookup_table1[str(j)[0]] + carry], end="")
            if carry == 1:
                print("(carry)", end=" ")
                carry = 0
            if j % base == base - 1:
                print("(reset)", end=" ")
                carry = 1
        if reset == 1:
            break

base = int(input("Please enter the base you wish to work with: "))
while base not in [2, 4, 8, 10, 16]:
    base = int(input("Invalid base, please enter a base of either 2, 4, 8, 10 or 16: "))

print("The selected base uses the following alphabet: ", lookup_table2[0:base])

number_of_digits = int(input("What is the maximum number of digits for your table?: "))

limit = limitCheck.limit_check(base)
count(base, limit, number_of_digits)
