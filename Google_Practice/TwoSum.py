'''Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because nums[0] + nums[1] = 9)'''

def mergeArr(nums, target):
    numDict = {}
    for index, num in enumerate(nums):
        x = target - num
        if x in numDict:
            return [numDict[x], index]
        else:
            numDict[num] = index

def main():
    for case in testcases():
        nums, target, expected = case["nums"], case["target"], case["expected"]
        result = mergeArr(nums, target)
        assert result == expected, f"Test Failed for nums = {nums}, target = {target}. Expected: {expected} but got {result}"
    print(f'All tests passed!')

def testcases():
    return [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]}
    ]

if __name__ == '__main__':
    main()