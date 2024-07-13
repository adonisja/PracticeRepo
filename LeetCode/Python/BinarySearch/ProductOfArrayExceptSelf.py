def productExceptSelf(nums):
    ans = [1] * len(nums) 
    pref, post = 1, 1
    '''Using the initial run through of the array, I set the ans array
        to the number ahead of the current number in ans
    '''
    for i in range(len(nums)): # loop through the array
        ans[i] = pref          # Set the resulting array to the prefix number on th initial run through
        pref *= nums[i]        # Set the new prefix to the number from the array
        print(f'Prefix Loop {i}: nums[i] = {nums[i]}, ans[i] = {ans[i]}, pref = {pref}')
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= post
        post *= nums[i]
        print(f'Postfix Loop {i}: nums[i] = {nums[i]}, ans[i] = {ans[i]}, post = {post}')
    return ans

def main():
    nums = [-1,1,0,-3, 3]
    print(productExceptSelf(nums))

if __name__ == "__main__":
    main()