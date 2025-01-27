def findCheapestCost(costs):
    '''diffs = []
    for c1, c2 in costs:
        diffs.append([c2 - c1, c1, c2])
    diffs.sort()
    res = 0
    for i in range(len(diffs)):
        if i < len(diffs)//2:
            res += diffs[i][2]
        else:
            res += diffs[i][1]
    return res'''
    n = len(costs)
    first_city = sum(a for a, b in costs)
    differences = [b - a for a, b in costs]
    differences.sort()
    return first_city + sum(differences[:n // 2])

def main():
    costList = [[[10,20],[30,200],[400,50],[30,20]],
    [[259,770],[448,54],[926,667],[184,139]],
    [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    ]
    i = 1
    for cost in costList:
        print(f'The Lowest Cost for List {i} is: {findCheapestCost(cost)}')
        i += 1

if __name__ == '__main__':
    main()