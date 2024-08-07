def flipAndInvertImage(image):
    flip = []
    for i in range(len(image)):
        reversed_arr = image[i][::-1]
        flip.append(reversed_arr)
    for n in range(len(flip)):
        for m in range(len(flip[n])):
            if flip[n][m] == 0:
                flip [n][m] = 1
            else:
                flip[n][m] = 0
    return flip

def main():
    image = [[1,1,0],[1,0,1],[0,0,0]]
    print(flipAndInvertImage(image))

if __name__ == '__main__': 
    main()