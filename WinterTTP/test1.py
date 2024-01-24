input = [0,2,3]
inputLength = len(input)
for i in range(inputLength - 1):
    if i != input[i]:
        input.append(i)
        input.sort()
print(input)