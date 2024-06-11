class Duplicate(object):
    
    def __init__(self, nums):
        self.nums = nums
    
    def findDuplicate(nums):
        dupeDict = {}
        for i in nums:
            if i in dupeDict:
                return True
            dupeDict[i] = 1
            print(dupeDict)
        return False
    
def main():
    nums = [7,32,12,3,7,4]
    dupe = Duplicate.findDuplicate(nums)
    print("This array contains duplicates" if dupe else "This array does not have any duplicates")
if __name__ == "__main__":
    main()