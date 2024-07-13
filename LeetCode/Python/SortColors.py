def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i, l, r = 0, 0, len(nums) - 1
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
        if nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
            i -= 1
        i += 1
    return nums
def main():
    nums = [2,0,1]
    nums = sortColors(nums)
    print(nums)

if __name__ == "__main__":
    main()