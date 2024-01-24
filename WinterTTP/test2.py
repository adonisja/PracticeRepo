input = [7,3,8,4,2]
result = []
max = 5
for i in input:
    if i < max:
        result.append(i)
result.sort()
print(result)
