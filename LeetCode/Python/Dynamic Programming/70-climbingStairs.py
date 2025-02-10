''' You are climbing a staircase. It takes n steps to reach the top.
 Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? '''

''' Solution 1: Time: O(n) - Space: O(n)
 Using a Dynamic Programming Approach to Break the overall problem into subproblems, 
 I've figured that we can only take 1 step or 2 steps, so for each position those are the options available
 Doing a bottoms up approach I build out the possible paths starting from 0
                          0
                        /   \ 
                      1      2
                     / \    / \ 
                    2   3  3   4
 and so on, store each value in a dict for easy look-up O(1) to reduce the time complexity
 and calculate each possible path for each step'''
def climbStairs(n, memDict= {}): # Time Complexity:  - Space Complexity: 
    if n == 1:   # Base-case: return 1 when n gets to 1
        return 1
    if n == 2:   # Second Base-case: return 2 when get gets back to 2
        return 2
    if n not in memDict:  # if the current number is not in dict go down further by 1 and by 2 steps
        memDict[n] = climbStairs(n-1, memDict) + climbStairs(n-2, memDict) # Store this value and its possible paths in a dict
    return memDict[n] #returns the final value for all possible paths

''' Solution 2: Time: O(n) - Space: O(1)
    I can use the iterative approach to calculate the possible paths as we go up the ladder
    if n = 1:       # Base-case, if theres only 1 step, then theres only 1 path
        return 1
    if n = 2:       # same as above, if theres only 2 steps then theres only 2 paths
        return 2
    prev, curr = 1, 2   # Initialize my prev and curr values to 1 and 2
     # I'll then calculate the possible steps from 3 (1 and 2 are already accounted for in prev and curr) up to the current number inclusive
    for i in range(3, n+1):
        prev, curr = curr, curr+prev # The prev value should be adjust to the curr value and 
        curr value will always adjust to add itself to the prev value 
        -- This means if prev = 1 and curr = 2, while n = 10 then 
        when i = 3, prev becomes 2 and curr become 1 + 2 = 3
        when i = 4, prev becomes 3 and curr becomes 2 + 3 = 5
        when i = 5, prev becomes 5 and curr becomes 3 + 5 = 8
        when i = 6, prev becomes 8 and curr becomes 8 + 5 = 13, etc.
    return curr'''

def main():
    count = 1
    for test in testcases():
        n, expected = test['n'], test['expected']
        result = climbStairs(n)
        print(f'Test {count}: Passed, Result = {result}' if result == expected else f'Test {count}: Failed\n Result = {result} - Expected Result = {expected}')
        count += 1

def testcases():
    return [
        {'n': 2, 'expected': 2},
        {'n': 3, 'expected': 3},
        {'n': 20, 'expected': 10946},
        {'n': 5, 'expected': 8}
    ]

if __name__ == '__main__':
    main()