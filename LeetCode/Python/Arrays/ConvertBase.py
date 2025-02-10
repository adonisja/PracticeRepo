def baseConversion(nums, base1, base2):
    res = []
    size = len(nums)
    nums = nums[::-1]
    sum = 0
    if not nums:
        return 0

    for i, digit in enumerate(nums):
        sum += digit * (base1 ** i)
        print(f'i:{i}, digit:{digit}')
    
    
    while sum > 0:
        res.append(sum % base2)
        sum //= base2

    return res[::-1] if res else 0


def main():
    for test in testcases():
        nums, base1, base2, expected = test["nums"], test["base1"], test["base2"], test["expected"]
        result = baseConversion(nums, base1, base2)
        assert result == expected, f"Testcase failed for {nums}. Result: {result}, Expected: {expected}"
    print("All testcases passed!")

def testcases():
    return [
        {"nums": [2, 1, 0], "base1": 3, "base2": 10, "expected": [2,1]},
        {"nums": [1, 0, 1, 0], "base1": 2, "base2": 10, "expected": [1,0]},
        {"nums": [1, 0], "base1": 10, "base2": 2, "expected": [1, 0, 1, 0]},
        {"nums": [1, 0, 1, 0], "base1": 2, "base2": 16, "expected": [10]},
        {"nums": [1, 0, 1, 0], "base1": 2, "base2": 8, "expected": [1, 2]}
    ]

if __name__ == '__main__':
    main()