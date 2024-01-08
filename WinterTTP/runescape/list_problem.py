print("Enter three values: ")
val = []
for x in range(3):
    newValue = input("Enter your value: ")
    val.append(newValue)
print(val[2])
print(f"John has {val[2]} siblings, {val[1]} pets and {val[0]} friends")