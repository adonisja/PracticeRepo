arr = [[3,2,1],[1,2,3]]
value = 0
for row in range(1, len(arr)):
    for col in range(1, len(arr[0])):
        if arr[row][col] %2 == 1:
            arr[row][col] = arr[row][col] + 1
        if arr[row][col] % 2 == 0:
            arr[row][col] = arr[row][col] * 2
print(arr)