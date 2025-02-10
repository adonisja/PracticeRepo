'''There are some processes that need to be executed. Amount of a load that process causes on a server that runs it,
is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes
that run on that server. You have at your disposal two servers, on which mentioned processes can be run.
Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.


Write a function that, given an array A of N integers, of which represents loads caused by successive processes,
the function should return the minimum absolute difference of server loads.


For example, given array A such that:

  A[0] = 1

  A[1] = 2

  A[2] = 3

  A[3] = 4

  A[4] = 5


your function should return 1. We can distribute the processes with loads 1, 2, 4 to the first server and 3, 5 to the second one,
so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.



Assume that:

N is an integer within the range [1..1,000]

the sum of the elements of array A does not exceed 100,000


In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
'''

'''Solution: Time: O() - Space O()
The solution we'll use is to calculate the total sum of the entire array and find the half of that sum
This gives us a pivot we can use to decide what values when add can get as close to it as possible'''
def loadBalancer(A):
    # n = len(array)
    # arrSum = sum(array)    
    # midSum = arrSum // 2
    
    '''We'll create a table (DP) to keep track of whether a particular sum can be achieved
    using a subset of the array
    rows represent the number of elements in the array
    and columns represent the possible sums from 0 to midSum
    The table is initialized with False for all except dp[0][0] which
    is True because a sum of 0 can always be achieved with 0 elements
     Here's what the table looks like initially:

    Elements \ Sum	0	1	2	3	4	5	6	7
                0	T	F	F	F	F	F	F	F
                1	F	F	F	F	F	F	F	F
                2	F	F	F	F	F	F	F	F
                3	F	F	F	F	F	F	F	F
                4	F	F	F	F	F	F	F	F
                5	F	F	F	F	F	F	F	F 
    '''
    # dp = [[False] * (midSum + 1) for _ in range(n+1)] 
    # dp[0][0] = True # Base-case: sum 0 can always be achieved with 0 elements
    # # Traverse the array
    # for i in range(1, n+1):         # remember column 0 is the range of values, while row 1 is the range of sums
    #     current_load = array[i-1]   # current load is the value in the column 0
    #     for j in range(midSum + 1):  # for each possible sum (row 0)
    #         if dp[i-1][j]:          
    #             # Checks if the sum can be achieved without this current element so if the cell above this one is True then this is True
    #             dp[i][j] = True     # marks the row as True if it you can get the midSum without this current value
    #             if j + current_load <= midSum: 
    #                 ''' then check if adding the current load to the number we are looking at is still less than the midSum 
    #                 if it is then mark that adjacent cell dp[i][j+current_load] as True to denote that '''
    #                 dp[i][j + current_load] = True
        
        
    # for j in range(midSum, -1, -1):
    #     if dp[n][j]:
    #         return arrSum - 2 * j
    # return arrSum
    arr_length = len(A)
    total = sum(A)
    half_sum = total // 2
    
    # Use a 1D DP array instead of 2D
    dp = [False] * (half_sum + 1)
    dp[0] = True  # Base case: sum of 0 is always possible

    if len(set(A)) == 1:  # All elements are the same
        if total % 2 == 0:
            return 0  # Even split possible if the total sum is even
        else:
            return total  # No split possible if the sum is odd
    
    for num in A:
        for j in range(half_sum, num - 1, -1):  # Iterate backward to prevent overwriting
            dp[j] = dp[j] or dp[j - num]
    
    for j in range(half_sum, -1, -1):
        if dp[j]:
            return total - 2 * j  # Minimize the difference
    return total


def main():
    for case in testcases():
        nums, expected = case["nums"], case["expected"]
        result = loadBalancer(nums)
        assert result == expected, f'Test failed for nums = {case["nums"]}, Expected {expected}, but got {result}'
    print(f'All tests passed!')

def testcases():
    return [
        {"nums": [1, 2, 3, 4, 5], "expected": 1},
        {"nums": [1, 1, 1, 1, 1], "expected": 1},
        {"nums": [10], "expected": 10},
        {"nums": [1, 10, 11], "expected": 0},
        {"nums": [], "expected": 0},  # Edge case: empty array
    ]

if __name__ == '__main__':
    main()