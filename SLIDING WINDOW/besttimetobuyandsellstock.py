# BEST TIME TO BUY AND SELL STOCK

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

# Solution 1: Using Greedy One Pass
def maxProfit1(prices):
    minPrice = float('inf')
    maxPrice = float('-inf')
    
    for price in prices:
        minPrice = min(price, minPrice)
        maxPrice = max(price - minPrice, maxPrice)
        
    return maxPrice

'''
Time Complexity: O(N)
- The algorithm iterates through the input array `prices` exactly once.
- In each iteration, it performs a constant number of operations (comparisons and assignments).
- As the loop runs N times, where N is the number of days (elements in the `prices` array), the time complexity is linear.

Space Complexity: O(1)
- The algorithm uses only a few variables (`minPrice`, `maxPrice`) to keep track of the minimum price seen so far and the maximum profit.
- The amount of extra space used does not depend on the size of the input array.
- Thus, the space complexity is constant.
'''

# Solution 2: Sliding Window 
def maxProfit2(prices):
    left = 0
    right = 1
    maxProfit = 0
    
    for right in range(len(prices)):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
            
    return maxProfit

'''
Time Complexity: O(N)
- The algorithm uses a sliding window approach with two pointers, `left` and `right`.
- The `right` pointer iterates through the entire `prices` array from the beginning to the end, visiting each element once.
- The `left` pointer only moves forward, being updated to the position of `right` when a lower price is found.
- Since each element is processed at most a constant number of times, the overall time complexity is linear with respect to the number of elements, N, in the input array.

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- It only requires a few variables (`left`, `right`, `maxProfit`, `profit`) to store pointers and the maximum profit found so far.
- The memory usage does not scale with the size of the input `prices` array.
- Thus, the space complexity is constant.
'''