def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars):
    
    if dollars[0] == '$':
        dollars = float(dollars[1:])
    else:
        dollars = float(dollars)
    print (dollars)
    return dollars


def percent_to_float(percent):
    if percent[-1] == "%":
        percent = float(percent[:-1]) / 100
    else:
        percent = float(percent) / 100
    print(percent)
    return percent

main()