'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between
 indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''
'''This takes a dynamic programming approach that will'''
class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for x in range(len(nums)):
            self.prefix[x + 1] = self.prefix[x] + nums[x]
        
    def sumRange(self, left, right):
        if right >= len(self.prefix) - 1:
            right = len(self.prefix) - 2
        return self.prefix[right+1] - self.prefix[left]
    
def main():
    for case in testcases():
        num_array = NumArray(case["nums"])
        for query in case["queries"]:
            left, right, expected = query["left"], query["right"], query["expected"]
            result = num_array.sumRange(left, right)
            assert result == expected, f"Test failed for nums = {case['nums']}, left={left}, right={right}. Expected {expected}, got {result}"
        print(f"All tests passed for nums = {case['nums']}")
    
def testcases():
    return [
        {
            "nums": [1, 2, 3, 4, 5],
            "queries": [
                {"left": 0, "right": 2, "expected": 6},
                {"left": 1, "right": 3, "expected": 9},
                {"left": 2, "right": 4, "expected": 12},
                {"left": 0, "right": 4, "expected": 15},
                {"left": 3, "right": 3, "expected": 4},
            ]
        },
        {
            "nums": [-1, 0, 1, 2, -3],
            "queries": [
                {"left": 0, "right": 2, "expected": 0},
                {"left": 1, "right": 4, "expected": 0},
                {"left": 2, "right": 3, "expected": 3},
                {"left": 0, "right": 4, "expected": -1},
                {"left": 1, "right": 1, "expected": 0},
            ]
        },
        {
            "nums": [10],
            "queries": [
                {"left": 0, "right": 0, "expected": 10},
            ]
        },
        {
            "nums": [],
            "queries": [
                {"left": 0, "right": 0, "expected": 0},  # Edge case: empty array
            ]
        },
    ]

if __name__ == "__main__":
    main()