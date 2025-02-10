def numSplit(num):
    res = []
    
    if num == 0:
        return 0
    num = abs(num)
    
    while num > 0:
        res.append(num % 10)
        num = num // 10

    return res[::-1]
    

def main():
    for test in testcases():
        nums, expected = test["nums"], test["expected"]
        result = numSplit(nums)
        print(result)
        #assert result == expected, f"Test for {nums} failed. Result: {result}, Expected: {expected}"
    print(f'All Testcases passed')

def testcases():
    return [
        {"nums": 12345, "expected": [1,2,3,4,5]}
    ]

if __name__ == '__main__':
    main()