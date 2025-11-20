# MAXIMUM CANDLES ALLOCATED TO K CHILDREN

'''
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i].
You can divide each pile into any number of sub piles, but you cannot merge two piles together.
You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. 
Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.
Return the maximum number of candies each child can get.
'''

"""
Algorithm:
1. Initialize two pointers: left = 1 and right = sum(candies) // k
2. While left <= right:
   a. Calculate mid = (left + right) // 2
   b. Calculate piles = 0
   c. For each candy in candies:
      - Calculate the number of piles needed to divide the candy at speed mid
      - Add the number of piles to piles
   d. If piles >= k:
      - Move right to mid - 1
   e. Else:
      - Move left to mid + 1
3. Return right
"""


def maximumCandies(candies, k):
    if sum(candies) < k:
        return 0
    
    left = 1
    right = sum(candies) // k
    
    while left <= right:
        mid = (left + right) // 2
        
        piles = 0
        for candy in candies:
            piles += candy // mid
            
        if piles >= k:
            left = mid + 1
        else:
            right = mid - 1
            
    return right

"""
Time Complexity: O(nlog(sum(candies)))
We iterate through the candies array once and check if the division is possible.
Each division operation takes O(1) time.
- The while loop runs at most log(sum(candies)) times.
- The for loop iterates through the candies array once. This takes O(n) time, where n is the number of candies.
- Therefore, the overall time complexity is O(nlog(sum(candies))) or O(nlog(sum(candies)/k)) if we divide by k.

Space Complexity: O(1)
We use constant space for the loop variables.
- The candies array is not modified, so the space complexity is O(1).
- The division operation involves creating temporary variables, which require additional O(1) space.
- Overall, the space complexity is O(1).
"""

# Test Cases
candies1 = [5, 8, 6]
k1 = 3
print(maximumCandies(candies1, k1))  # Output: 5

candies2 = [1, 2, 3, 4, 5]
k2 = 2
print(maximumCandies(candies2, k2))  # Output: 4

candies3 = [1, 2, 3, 4, 5, 6]
k3 = 3
print(maximumCandies(candies3, k3))  # Output: 4

candies4 = [1, 2, 3, 4, 5, 6, 7]
k4 = 4
print(maximumCandies(candies4, k4))  # Output: 4

candies5 = [1, 2, 3, 4, 5, 6, 7, 8]
k5 = 5
print(maximumCandies(candies5, k5))  # Output: 4

candies6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k6 = 6
print(maximumCandies(candies6, k6))  # Output: 4

candies7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k7 = 7
print(maximumCandies(candies7, k7))  # Output: 5

candies8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k8 = 8
print(maximumCandies(candies8, k8))  # Output: 5

candies9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
k9 = 9
print(maximumCandies(candies9, k9))  # Output: 5

candies10 = [2, 5]
k10 = 11
print(maximumCandies(candies10, k10))  # Output: 0