''' Given an array nums containing n distinct numbers in the range [0, n],
 return the only number in the range that is missing from the array.
'''
def missingNumber(nums): # Time Complexity O(n), Space Complexity O(1)
    '''Method 1:'''
    n = len(nums) # take the length of the Array
    actual_sum = sum(nums) # and get the sum of the numbers within the array
    expected_sum = n * (n + 1) // 2 
    ''' Since we know only 1 number can be missing we can calculate the length of the array times one greater than the length of the array
    and floor divide by half which would give use the sum of all the numbers within the range from 1 to the highest number in the array
    or the sum from 1 to the next sumber in the range if all numbers are present'''
    print(f'Actual Sum: {actual_sum}, Expected Sum: {expected_sum}')
    return expected_sum - actual_sum # We can then return the difference of the expected sum from the actual sum that we have to get the missing value

    ''' Method 2: Time Complexity: O(n) Space Complexity: O(n)
    Second method involves checking if the previous value for each number we are currently looking at is in the array
    we convert the array to a set for efficient look-up if we traverse the entire array without finding a missing value
    then we return the current highest value+1
    maxNum = 0
    nums = set(nums)
    for i in nums:
        if i-1 not in nums and i != 0:
            return i-1
    return max(nums)+1
    '''


def main():
    count = 1
    for test in testcases():
        nums, expected = test['nums'], test['expected']
        result = missingNumber(nums)
        print(f'Test {count}: : Passed; Result = {result}' if expected == result else 'Test {count}: Failed; Result = {result}')
        count += 1

def testcases():
    return [
        {'nums': [3,0,1], 'expected': 2},
        {'nums': [0,1], 'expected': 2},
        {'nums': [9,6,4,2,3,5,7,0,1], 'expected': 8}
    ]

if __name__ == '__main__':
    main()