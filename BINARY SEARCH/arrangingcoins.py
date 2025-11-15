# ARRANGING COINS

'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.
'''

# Brute Force Approach
def arrangingCoins1(n):
    count = 1
    
    while n >= count:
        n -= count
        count += 1
        
    return count - 1

'''
Time Complexity: O(√n)
- The while loop continues as long as n >= count, where count starts at 1 and increments by 1 each iteration.
- In each iteration, we subtract count from n. The sum of the first k natural numbers is k(k+1)/2.
- The loop terminates when k(k+1)/2 ≈ n, which means k ≈ √(2n) ≈ √n.
- Therefore, the loop runs approximately √n times, making the time complexity O(√n).

Space Complexity: O(1)
- The algorithm uses only a constant amount of extra space for the variables count and n.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Binary Search Approach
def arrangingCoins2(n):
    left = 1
    right = n
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        coins = (mid / 2) * (mid + 1)
        
        if coins > n:
            right = mid - 1
        else:
            left = mid + 1
            result = max(result, mid)
            
    return result

'''
Time Complexity: O(log n)
- The algorithm uses binary search on the range [1, n].
- In each iteration, we calculate the midpoint and determine the total number of coins needed to complete `mid` rows using the formula: coins = (mid / 2) * (mid + 1), which is the sum of first `mid` natural numbers.
- The search space is halved in each iteration by adjusting either `left` or `right`.
- The loop continues until `left > right`, which takes at most log₂(n) iterations.
- All operations inside the loop (calculating mid, computing coins, comparisons, updates) are O(1).
- Therefore, the overall time complexity is O(log n).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for variables: `left`, `right`, `result`, `mid`, and `coins`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Math Approach
def arrangingCoins3(n):
    return int((math.sqrt(1 + 8 * n) - 1) / 2)

'''
Time Complexity: O(1)
- The algorithm uses a mathematical formula to directly calculate the number of complete rows.
- The formula is derived from solving the quadratic equation: k(k+1)/2 = n for k, which gives k = (√(1 + 8n) - 1) / 2.
- All operations (multiplication, addition, square root, subtraction, division, and int conversion) are performed in constant time.
- There are no loops or recursive calls that depend on the input size n.
- Therefore, the time complexity is O(1).

Space Complexity: O(1)
- The algorithm uses only a constant amount of extra space for the intermediate calculation and the return value.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
n1 = 5
print(arrangingCoins1(n1)) # Output: 2

n2 = 8
print(arrangingCoins1(n2)) # Output: 3

n3 = 1
print(arrangingCoins1(n3)) # Output: 1

n4 = 3
print(arrangingCoins1(n4)) # Output: 2

n5 = 6
print(arrangingCoins1(n5)) # Output: 3

n6 = 10
print(arrangingCoins1(n6)) # Output: 4

n7 = 15
print(arrangingCoins1(n7)) # Output: 5

n8 = 21
print(arrangingCoins1(n8)) # Output: 6

n9 = 100
print(arrangingCoins1(n9)) # Output: 13

n10 = 1000
print(arrangingCoins1(n10)) # Output: 44