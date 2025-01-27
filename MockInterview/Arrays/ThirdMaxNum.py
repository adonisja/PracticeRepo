def findThirdLargest(num): #Time Complexity: O(n log n)
    num.sort()
    size = len(num)
    if size == 0:
        return None
    elif size < 3:
        return num[size - 1]
    else: 
        thirdLarge = num[size - 3]
        return thirdLarge
    
''' Other Option: (Time Complexity O(n))
def thirdMax(self, nums: List[int]) -> int:
        dummy = [float('-inf') for _ in range(3)]  # length of 3
        for n in nums:
            if n not in dummy:
                if n > dummy[0]:
                    dummy = [n, dummy[0], dummy[1]]
                elif n > dummy[1]:
                    dummy = [dummy[0], n, dummy[1]]
                elif n > dummy[2]:
                    dummy = [dummy[0], dummy[1], n]
        return dummy[2] if float('-inf') not in dummy else max(dummy)
'''
def main():
    nums = [[3, 2, 1],
    [7, 1, 11, 9, 5],
    [9, 4, 3, 2, 1],
    [9, 8, 7, 6, 5],
    [11, -1, 8, 21, -1, 3],
    [1, 2],
    []
    ]
    i = 1
    for num in nums: 
        print(f'Third largest of list {i} is: {findThirdLargest(num)}')
        i += 1
if __name__ == "__main__":
    main()