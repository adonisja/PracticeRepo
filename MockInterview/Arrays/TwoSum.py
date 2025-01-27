def twoSum(nums, target):
    res = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in res:
            return [res[diff], index]
        res[num] = index
    return []

def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))


if __name__ == "__main__":
    main()