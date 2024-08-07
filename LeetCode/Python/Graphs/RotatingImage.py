def rotate(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        top = layer 
        bottom = n - 1 - layer
        for i in range(top, bottom):
            offset = i - top
            topLeft = matrix[top][i]
            # move bottom left into top left
            matrix[top][i] = matrix[bottom - offset][top]
            # move bottom right into bottom left
            matrix[bottom - offset][top] = matrix[bottom][bottom - offset]
            # move top right into bottom right
            matrix[bottom][bottom - offset] = matrix[i][bottom]
            # move top left into top right
            matrix[i][bottom] = topLeft

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print(matrix)

if __name__ == '__main__':
    main()