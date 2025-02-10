def ReverseArray(num_list, start, stop):
    while start < stop:
        num_list[start], num_list[stop] = num_list[stop], num_list[start]
        start += 1
        stop -= 1
    return num_list
    
      
    

    

def main():
    for test in testcases():
        list1, k, expected = test["list1"], test["k"], test["expected"]
        size = len(list1)
        reversedList = ReverseArray(list1, 0, size-1) # reverse the entire list
        reversedListbeforeK = ReverseArray(reversedList, 0, size-k-1) # reverse all the numbers before k
        result = ReverseArray(reversedListbeforeK, size-k, size-1)  # Reverse the last elements
        assert result == expected, f"Test failed for {list1} rotated by {k}. Expected: {expected} but got {result}"
    print(f'All test cases passed')


def testcases():
    return [
        {"list1": [1,4,5,7,9], "k": 3, "expected":[ 7, 9, 1, 4, 5]},
        {"list1": [1,2,3,4], "k": 4, "expected": [ 1, 2, 3, 4]},
        {"list1": [1,2,3,4,5], "k": 6, "expected": [ 2, 3, 4, 5, 1]},
        {"list1": [1, 2, 3], "k": 0, "expected": [ 1, 2, 3]},
        #{"list1": [], "list2": [], "expected": []},
    ]

if __name__ == '__main__':
    main()
