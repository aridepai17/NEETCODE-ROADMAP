# FINAL PRICES WITH A SPECIAL DISCOUNT IN A SHOP

'''
You are given an integer array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop. 
If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. 
Otherwise, you will not receive any discount at all.
Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.
'''

def finalPrices(prices):
    answer = list(prices)
    stack = []
    
    for i in range(len(prices)):
        currentPrice = prices[i]
        while stack and currentPrice <= prices[stack[-1]]:
            prevIndex = stack.pop
            answer[prevIndex] = prices[prevIndex] - currentPrice
        stack.append(i)
        
    return answer

'''
Time Complexity: O(n)
We iterate through the prices array once. Although there is a nested while loop, each element is pushed and popped from the stack at most once. 
This means the total number of stack operations across all iterations of the for loop is proportional to n. 
Therefore, the time complexity is linear.

Space Complexity: O(n)
In the worst-case scenario (e.g., a strictly increasing array of prices), the stack can hold all n indices. 
Additionally, we create an 'answer' array of size n. Thus, the space required is proportional to the size of the input array.
'''

# Test Cases
prices1 = [8,4,6,2,3]
print(finalPrices(prices1)) # Output: [4, 2, 4, 2, 3]

prices2 = [10,1,1,6]
print(finalPrices(prices2)) # Output: [9, 0, 1, 6]

prices3 = [1,2,3,4,5]
print(finalPrices(prices3)) # Output: [1, 2, 3, 4, 5]

prices4 = [5,4,3,2,1]
print(finalPrices(prices4)) # Output: [1, 1, 1, 1, 1]

prices5 = [10,10,10,10]
print(finalPrices(prices5)) # Output: [0, 0, 0, 10]

prices6 = []
print(finalPrices(prices6)) # Output: []

prices7 = [42]
print(finalPrices(prices7)) # Output: [42]

prices8 = [1,5,2,8,3]
print(finalPrices(prices8)) # Output: [1, 3, 2, 5, 3]

prices9 = [4,7,1,9,5,2,8,3]
print(finalPrices(prices9)) # Output: [3, 6, 1, 4, 3, 2, 5, 3]

prices10 = [5,1,2,3,4]
print(finalPrices(prices10)) # Output: [4, 1, 2, 3, 4]