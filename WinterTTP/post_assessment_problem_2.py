def SumMultiples():
    num = int(input("Enter a number: "))        #
    sum = 0.                                    #initializes an accumulator
    for i in range(num + 1):                    #loops through a range of 0 until the number given
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:      #checks if the current value is divisible by 3, 5 or 7
            sum += i                              #if true then the value is added to the accumulator
    print("Sum: ", sum)

def main():
    SumMultiples()

main()