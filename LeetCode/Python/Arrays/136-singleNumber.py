''' Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.'''

def singleNumber(nums): # Time Complexity: O(n), Space Complexity: O(1)
    ''' we will use a bit-wise XOR comparison to find the value that is unique in the array
    that is 2 converted to binary is 010, any number XOR'd on itself is 0, 
    2 XOR 2 =
    10   
    10
    ----
    00  remember 0 bit represents True and 1 represents False,
    therefore a bit-wise XOR comparison yields 0 XOR 0 = 0 : True XOR True = True
                                               1 XOR 1 = 0 :  False XOR False = True
    Just a reminder XOR = NOT OR operation: where 0 or 0 = 0 then Not 0 = 1
                                                True or True = True, then Not True = False
    '''
    res = 0
    for n in nums:
        res ^= n  
    # Conduct a XOR comparison, res will store the value that is unique because all other values will equate to 0 when their duplicate is reached
    return res 

def main():
    count = 1
    for test in testcases():
        nums, expected = test['nums'], test['expected']
        result = singleNumber(nums)
        print(f'Test {count}: Passed, Result = {result}' if result == expected else 'Test {count}: Failed, Result: {result}')
        count += 1

def testcases():
    return[
        {'nums': [2,2,1], 'expected': 1},
        {'nums': [4,1,2,1,2], 'expected': 4},
        {'nums': [1], 'expected': 1}
    ]

if __name__ == "__main__":
    main()