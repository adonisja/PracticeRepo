weight = 3.0
numItems = 12.0
if weight < 1:
    price = 1.45
if weight >= 1:
    price = 1.15
total = weight * price
if numItems >= 10:
    total = total * 0.9
print(weight)
print(price)
print(total)