'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    '''Boyer-Moore Algorithm Solution:
       This solution only works when a guaranteed majority exits (an element occurs more than half of the total number) 
        '''
        count, final = 0, 0 # set an intial count and solution to 0
        for i in nums: #iterate over the elements in the list
            if count == 0: # if the element already exists
                final = i # the solution is equal to the element found
            count += (1 if i == final else -1) 
            #if the element is a duplicate then add 1 otherwise if its distinct then subtract 1 from count
        return final
        '''count = {}
        final, high= 0, 0
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            final = i if count[i] > high else final
            high = max(count[i], high)
        return final'''