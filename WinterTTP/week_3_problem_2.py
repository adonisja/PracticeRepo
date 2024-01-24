price = 50
payment = 0 
while price > payment: #Initializes a while loop that will continuously prompt the user until the total payment is met or exceeded
    payment = int(input("Enter your a coin: "))
    price -= payment
    payment = 0 #resets the payment to 0 after calculating the new price to verify the logic of the loop
    if price > 0:
        print(f'Please deposit {price}\u00A2 more')
    elif payment > price:
        price = abs(price) #Price is set to the absolute value of itself to prevent outputing a negative value
        print(f'Thank You for your purchase\nYour change is {price}\u00A2\nEnjoy Your Coke!')
        break
    else:
        print(f'Thank You for your purchase\nEnjoy Your Coke!')
