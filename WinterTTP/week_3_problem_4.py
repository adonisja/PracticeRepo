'''Rules: 1. if not plate_num[:1].isdigit()
        2. len(plate_num) >=2 && plate_num.isalpha()
        3. len(plate_num) >=2 && len(plate_num) <=6
        4. plate_num[len(plate_num)/2 : ].isalnum && plate_num[-1].isalpha()
if plate_num[len(plate_num)/2 : ].isdigit * use a loop to return the index of each letter 
        5. plate_num.isalnum()        
'''
def is_valid(plate):
        numDigit = len(plate) #sets a variable for the length of plate
        if plate[:1].isdigit(): #checks if the first or second indices is a number
                return False
        if not (numDigit >= 2 and numDigit <= 6): #checks if the plate number is not between 2-6
                return False
        for i, c in enumerate(plate): #loops through plates, i represents the index and c is the value stored at that index for plate
                if c.isdigit():
                        if c == '0': 
                                return False
                        if plate[i:].isalpha():
                                return False
        if not plate.isalnum():
                return False
        return True


def main():
        plate = input("Plate: ")
        if is_valid(plate):
                print("Valid")
        else:
                print("Invalid")


main()