def mathInterpreter():
    print("Please use spaces between values!")
    mathProblem = input("Enter an arithmetic problem: \n")
    list = mathProblem.split() # splits the user input into a list of variables
    while len(list) < 3:
        print("Invalid Entry!\nPlease use spaces between values!")
        mathProblem = input("Enter an arithmetic problem: \n")
        list = mathProblem.split()
    print(list)
    val1 = float(list[0]) #assigns the first member of the list as a float to variable val1
    arithmetic = list[1] #assigns the second member of the list as the arithmetic sign of the problem
    val2 = float(list[2]) #assigns the third member of the list as a float to variable val2
    #uses a switch-case function on the arithmeic variable to determine which arithmetic procedure to follow
    match arithmetic:
        case '+':
            print(val1+val2)
        case '-':
            print(val1-val2)
        case '*':
            print(val1*val2)
        case '/':
            if val2 == 0: # outputs an error of if the denominator of a division is 0
                print('denominator cannot be 0')
            else:
                print(f"{val1/val2:.02f}")
        case '**':
            print(val1**val2)
        case _:
            raise TypeError("Invalid Syntax")

def main():
    mathInterpreter()

main()