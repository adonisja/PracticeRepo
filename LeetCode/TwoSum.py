class TwoSum(object):

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def findTarget(nums, target):
        targetDict = {}
        count = 0
        targetFound = False
        for i in nums:
            diff = target - i
            if diff in nums:
                if nums.index(diff) not in targetDict:
                    targetDict[count] = nums.index(diff)
                    targetFound = True
            count += 1
        print(targetDict)
        print("The indices are: ", targetDict if targetFound else "No 2 values add up to ", target)


def main():
    nums = [1,3,7,4,9]
    target = int(input("Enter the target: "))
    TwoSum.findTarget(nums, target)

if __name__ == "__main__":
    main()