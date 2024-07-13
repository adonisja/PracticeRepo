
    def maxSubsequence(nums, k):
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
    largest = sorted_nums[:k]
    original_nums_sort = sorted(largest, key=lambda x: x[0])
    result = [value for index, value in original_nums_sort]
    return result
