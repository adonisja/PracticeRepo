''' You are climbing a staircase. It takes n steps to reach the top.
 Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? '''

''' Solution: Using a Dynamic Programming Approach to Break the overall problem into subproblems, 
I've figured that we can only take 1 step or 2 steps, so for each position those are the options available'''
def climbStairs(n, memDict= {}): # Time Complexity:  - Space Complexity: 
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memDict:
        memDict[n] = climbStairs(n-1, memDict) + climbStairs(n-2, memDict)
    return memDict[n]

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
        {'n': 20, 'expected': 10946}
    ]

if __name__ == '__main__':
    main()