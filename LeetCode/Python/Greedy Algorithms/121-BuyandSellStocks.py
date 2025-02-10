''' You are given an array prices where prices[i] is the price of a given stock on the ith day.
 You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
 Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. '''

''' Solution: Time: O(n), Space - O(1)
    I will traverse the entire array, comparing the current value to the minimum value seen so far,
    and reassign the min value to the current value if applicable , this assignment takes place on the first
    value with in the array and reassigns for each subsequent value lower than the one before. I then calculate the profit possible
     from the if I sold on the current day and check if thats the max possible profit I can make'''
def maxProfit(prices):
    if not prices:  # Return 0 for an empty array
        return 0
    min_Price = float('inf') # min_Price is infinity
    max_Profit = 0           # max_Profit is 0
    for x in prices:                                # ----- On First Run ------- n = [4, 6, 7]               |   - Second Run
        min_Price = min(min_Price, x)               # min_Price = min(infinity and 4) so min_Price becomes 4 |    min_Price
        max_Profit = max(max_Profit, x - min_Price)  # max_Profit = max(0 and 4-0) so max_Profit becomes 4   |
    return max_Profit