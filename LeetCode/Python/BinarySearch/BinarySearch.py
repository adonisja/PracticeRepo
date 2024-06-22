'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1'''

class BinarySearch:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target


    def findTarget(self, nums, target):
        high = len(nums)
        low = 0
        found = False
        while not found:
            mid = low + (high - low) // 2
            print(f'mid = {mid}')
            if nums[mid] == target:
                print(f'{target} found @ index: {mid}')
                found = True
                return found
            elif target < nums[mid]:
                high = mid - 1
                print(f'target is less than mid val\nhigh = {high}')
            elif target > nums[mid]:
                low = mid + 1
                print(f'target is greater than mid\nlow = {low}')
            elif low == high and nums[mid] != target:
                print(f'target is not found')
                return -1
            
def main():
    nums = [-1,0,3,5,9,12]
    target = 9
    bs = BinarySearch(nums, target)
    print(bs.findTarget(nums,target))

if __name__ == "__main__":
    main()