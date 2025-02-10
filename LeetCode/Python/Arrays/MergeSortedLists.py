def mergeArrays(list1, list2):
    x = y = 0
    size1 = len(list1)
    size2 = len(list2)
    newList = []
    while x < size1 and y < size2:
        if list1[x] < list2[y]:
            newList.append(list1[x])
            x += 1
        else:
            newList.append(list2[y])
            y += 1

    newList.extend(list1[x:]) 
    newList.extend(list2[y:])

    return newList

def main():
    for test in testcases():
        list1, list2, expected = test["list1"], test["list2"], test["expected"]
        result = mergeArrays(list1, list2)
        assert result == expected, f"Test failed for lists {list1}, and {list2}. Expected: {expected} but got {result}"
    print(f'All test cases passed')


def testcases():
    return [
        {"list1": [1,4,5,7,9], "list2": [1, 2, 3, 4, 5], "expected":[1, 1, 2, 3, 4, 4, 5, 5, 7, 9]},
        {"list1": [1,2,3,4], "list2": [1,2,3,4], "expected": [ 1, 1, 2, 2, 3, 3, 4, 4]},
        {"list1": [], "list2":[1,2,3], "expected": [1,2,3]},
        {"list1": [1, 2, 3], "list2": [], "expected": [ 1, 2, 3]},
        {"list1": [], "list2": [], "expected": []},
    ]

if __name__ == '__main__':
    main()