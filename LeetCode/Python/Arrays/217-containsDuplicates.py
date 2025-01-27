''' Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.
'''
def containsDuplicate(nums):
    # First, initialize a diction to hold numbers in the array,
    numDict = {}
    # Then traverse each element in the array
    for x in nums:
        # If we haven't seen the value, add it to the dictionary
        if x in numDict:
            return True
        else:
            # If we haven't seen the value before add it to the dictionary
            numDict[x] = True
    return False # Return false if we've traversed the entire array w/o finding a duplicate value

def main():
    for test in testcases():
        nums, expected = test['nums'], test['expected']
        result = containsDuplicate(nums)
        print(f'Accepted' if result == expected else 'Failed')

def testcases():
    return [
        {'nums': [1, 2, 3, 1], 'expected': True},
        {'nums': [1, 2, 3, 4], 'expected': False},
        {'nums': [1, 1, 1, 1], 'expected': True},
        {'nums': [], 'expected': False},
        {'nums': [1], 'expected': False}
    ]

if __name__ == '__main__':
    main()