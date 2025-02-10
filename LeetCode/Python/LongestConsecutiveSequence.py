from numpy import sort


class LongestConsecutiveSequence(object):
    
    def __init__(self, nums):
        self.nums = nums
        self.stack = []

    def chainCount(self, nums):
        count, maxCount = 0, 0
        for i, num in enumerate(self.nums):
            if not self.stack:
                self.stack.append(nums[i])
                count += 1
            else:
                if nums[i] == self.stack[-1] + 1:
                    self.stack.append(nums[i])
                    count += 1
                else:
                    self.stack = []
                    self.stack.append(nums[i])
                    count = 0
                    count += 1
            if count > maxCount:
                maxCount = count
                
            print(f'num: {num}, count: {count}, max count = {maxCount}')    
        return maxCount


        
        
    
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty:
            return self.stack.pop()
        else:
            return None
        
    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


        
        


def main():
    nums = [17, 21, 3, 35, 9, 23, 8, 20, 22]
    nums = sort(nums)
    lcs = LongestConsecutiveSequence(nums)
    maxCount = lcs.chainCount(nums)
    print(maxCount)


if __name__ == "__main__":
    main()