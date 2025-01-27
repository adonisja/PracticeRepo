def convertList(A):
    length = len(A)
    B = []
    for i in range(length):
        B.append(A[i])
    return B



def main():
    num = input('Enter a number: ')
    print(convertList(num)) 
    
if __name__ == "__main__":
    main()

'''Write a function that takes a number and returns
a list of its digits. So for 2342 it should return [2,3,4,2]'''