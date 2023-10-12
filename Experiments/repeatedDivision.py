base = int(input("Enter the base: "))
num = int(input("Enter the number you wish to convert: "))

quotient = 9999
remainder = []
i = 0

while quotient != 0 :
    if quotient == 9999:
        quotient = num / base
        remainder[i] = int(num % base)
    else:
        quotient = quotient / base
        remainder[i] = int(quotient % base)
        print("quotient: ", quotient, "remainder: ", remainder)
    i += 1

print("The converted value is: ")
for i in remainder:
    print(remainder[i])
    i -= 1