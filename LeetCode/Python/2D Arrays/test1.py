mat=[[0 for c in range(3)] for r in range(4)]
for row in range(4):
    for col in range(3):
        if row < col:
            mat[row][col] = 1
        elif row == col:
            mat[row][col] = 2
        else:
            mat[row][col] = 3
print(mat)