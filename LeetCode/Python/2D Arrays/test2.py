def findMax(imagePixels):
    i = iMax = 0
    for r in range(len(imagePixels)):
        for c in range(len(imagePixels[0])):
            i = imagePixels[r][c]
            if i > iMax:
                iMax = i

    return iMax