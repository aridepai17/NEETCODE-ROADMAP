# KOKO EATING BANANAS

'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
'''

"""
Algorithm:
1. Initialize two pointers: left = 1 and right = max(piles)
2. While left <= right:
   a. Calculate mid = (left + right) // 2
   b. Calculate hours = 0
   c. For each pile in piles:
      - Calculate the number of hours needed to eat the pile at speed mid
      - Add the number of hours to hours
   d. If hours <= h:
      - The target is found
      - Return True
   e. If hours > h:
      - The target is in the right half of the matrix
      - Move left to mid + 1
   f. Else:
      - The target is in the left half of the matrix
      - Move right to mid - 1
3. The target is not found in the matrix
- Return False
"""

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    
    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid # Ceil 
        if hours <= h:
            right = mid - 1
        else:
            left = mid + 1
            
    return left

'''
Time Complexity: O(nlog(max(piles)))
Let n be the number of piles, and let m be the maximum number of bananas in a pile.
- The while loop runs at most log(m) times.
- In each iteration of the while loop, we iterate through the piles once. This takes O(n) time.
- The division operation in the calculation of hours takes O(1) time.
- Therefore, the overall time complexity is O(nlog(m)).

Space Complexity: O(1)
- The algorithm uses two variables left and right, which are constant sized.
- The calculation of hours involves a loop that iterates through the piles once. This takes O(n) space.
- The calculation of hours also involves a constant number of variables, which are constant sized.
- Therefore, the space complexity is O(1).
'''

# Test Cases
piles1 = [3,6,7,11]
h1 = 8
print(minEatingSpeed(piles1, h1)) # Output: 4


piles2 = [1,10,10]
h2 = 1
print(minEatingSpeed(piles2, h2)) # Output: 1

piles3 = [1,2,3]
h3 = 2
print(minEatingSpeed(piles3, h3)) # Output: 3

piles4 = [10,10,10]
h4 = 1
print(minEatingSpeed(piles4, h4)) # Output: 10

piles5 = [1,100,1000]
h5 = 2
print(minEatingSpeed(piles5, h5)) # Output: 100

piles6 = [1,2,3,4,5,6]
h6 = 3
print(minEatingSpeed(piles6, h6)) # Output: 6

piles7 = [1,2,3,4,5,6,7]
h7 = 4
print(minEatingSpeed(piles7, h7)) # Output: 7

piles8 = [1,2,3,4,5,6,7,8]
h8 = 5
print(minEatingSpeed(piles8, h8)) # Output: 8

piles9 = [1,2,3,4,5,6,7,8,9]
h9 = 6
print(minEatingSpeed(piles9, h9)) # Output: 9

piles10 = [1,2,3,4,5,6,7,8,9,10]
h10 = 7
print(minEatingSpeed(piles10, h10)) # Output: 10