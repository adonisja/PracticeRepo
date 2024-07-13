def productExceptSelf(nums):
    ans = [1] * len(nums)
    pref, post = 1, 1
    for i in range(len(nums)):
        ans[i] = pref
        pref *= nums[i]
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= post
        post *= nums[i]
    return ans

def main():
    nums = [1,2,3,4]
    print(productExceptSelf(nums))

if __name__ == '__main__':
    main()