from math import inf

def ConstructRectangle(area):
    mini = float(inf)
    ar = [area, 1]

    for w in range(1, int(area**0.5) + 1):
        l = area/w
        if l == int(l) and l >= w and l-w < mini:
            ar[0] = int(l)
            ar[1] = int(w)
            mini = int(l - w)
    return ar

def main():
    area = 122122
    print(ConstructRectangle(area))

if __name__ == '__main__':
    main()
