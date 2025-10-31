# BEST TIME TO BUY AND SELL STOCK 2

'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
Find and return the maximum profit you can achieve.
'''

def maxProfit(prices):
    profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
            
    return profit

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `prices`.
- The algorithm iterates through the `prices` array exactly once, from the second element to the last.
- Inside the loop, operations like comparison, addition, and subtraction are all constant time operations, O(1).
- Therefore, the total time complexity is directly proportional to the number of days, making it O(N).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables (`profit`, `i`) regardless of the input size.
- No additional data structures are created that grow with the input size.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
prices1 = [7,1,5,3,6,4]
print(maxProfit(prices1)) # Output: 7

prices2 = [1,2,3,4,5]
print(maxProfit(prices2)) # Output: 4

prices3 = [7,6,4,3,1]
print(maxProfit(prices3)) # Output: 0

prices4 = [1, 5, 2, 8, 3, 9]
print(maxProfit(prices4)) # Output: 14

prices5 = [2, 1, 2, 0, 1]
print(maxProfit(prices5)) # Output: 2

prices6 = [1]
print(maxProfit(prices6)) # Output: 0

prices7 = []
print(maxProfit(prices7)) # Output: 0

prices8 = [1, 1, 1, 1, 1]
print(maxProfit(prices8)) # Output: 0

prices9 = [10, 1, 5, 6, 2, 8]
print(maxProfit(prices9)) # Output: 12

prices10 = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfit(prices10)) # Output: 8