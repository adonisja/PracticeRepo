def convert(hour, minute):
    convertedMinutes = float(minute / 60) #converts minutes to decimal format
    convertedMinutes = str(convertedMinutes) #changes the variable to a string for easier formatting in the print statement
    print(f"time is: {hour}{convertedMinutes[1:4]}hrs") 

def main():
    time = input("Enter the current time: ")
    timeList = time.split(":") #splits the time into a list containing two members along the : symbol
    hour = int(timeList[0]) # assigns the first member as the hour
    minute = int(timeList[1]) #assigns the second member as the minutes
    #initiates the flags for the special times as false
    breakfastTime = False
    lunchTime = False
    dinnerTime = False
    match hour: #creates a switch case with the hour as the determinant
        case 7:
            breakfastTime = True #sets the breakfastTime flag to true for all times within the range of 7:00 to 7:59
        case 8:
            if minute == 0: #sets the breakfastTime flag to true if it is exactly 8:00
                breakfastTime = True
        case 12:
            lunchTime = True #sets the lunchTime flag to true for all times within the range of 12:00 to 12:59
        case 13:
            if minute == 0:
                lunchTime = True #sets the lunchTime flag to true if it is exactly 13:00
        case 18:
            dinnerTime = True #sets the dinnerTime flag to true for all times within the range of 18:00 to 18:59
        case 19:
            if minute == 0:
                dinnerTime = True #sets the lunchTime flag to true if it is exactly 18:00
    #checks to which statement is true and prints an output based on that evaluation
    if breakfastTime:
        print("It's Breakfast Time!")
    elif lunchTime:
        print("It's Lunch Time!")
    elif dinnerTime:
        print("It's Dinner Time!")
    convert(hour, minute)



main()
