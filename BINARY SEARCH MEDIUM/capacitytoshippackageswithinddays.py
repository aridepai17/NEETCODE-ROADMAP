# CAPACITY TO SHIP PACKAGES WITHIN D DAYS

'''
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. 
Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
'''

"""
Algorithm:
1. Initialize two pointers: left = max(weights) and right = sum(weights)
2. While left <= right:
   a. Calculate mid = (left + right) // 2
   b. Calculate daysNeeded = 1 and currentWeight = 0
   c. For each weight in weights:
      - If currentWeight + weight > mid:
         - Increment daysNeeded by 1
         - Set currentWeight to weight
      - Else:
         - Add weight to currentWeight
   d. If daysNeeded <= days:
      - Move right to mid - 1
   e. Else:
      - Move left to mid + 1
3. Return left
"""

def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)
    
    while left <= right:
        mid = (left + right) // 2
        
        daysNeeded = 1
        currentWeight = 0
        
        for weight in weights:
            if currentWeight + weight > mid:
                daysNeeded += 1
                currentWeight = weight
            else:
                currentWeight += weight
        
        if daysNeeded <= days:
            right = mid - 1
        else:
            left = mid + 1
            
    return left

"""
Time Complexity: O(nlog(∑weights))
The algorithm uses binary search on the total weight of the packages.
In each iteration, we calculate the midpoint and update daysNeeded and currentWeight.
The loop continues until left > right, which takes at most log₂(∑weights) iterations.
All operations inside the loop (calculating mid, updating daysNeeded and currentWeight) are O(n).
Therefore, the overall time complexity is O(nlog(∑weights)).


Space Complexity: O(1)
The algorithm uses a constant amount of extra space for variables: left, right, mid, daysNeeded, and currentWeight.
No additional data structures are created that scale with the input size.
Therefore, the space complexity is O(1).
"""

# Test Cases
weights1 = [1,2,3,4,5,6,7,8,9,10], days1 = 5
print(shipWithinDays(weights1, days1)) # Output: 15

weights2 = [1,2,3,4,5], days2 = 3
print(shipWithinDays(weights2, days2)) # Output: 6

weights3 = [1,2,3,4,5,6], days3 = 4
print(shipWithinDays(weights3, days3)) # Output: 10

weights4 = [1,2,3], days4 = 1
print(shipWithinDays(weights4, days4)) # Output: 6

weights5 = [1,2,3,4,5,6,7,8,9,10,11], days5 = 10
print(shipWithinDays(weights5, days5)) # Output: 11

weights6 = [1,2,3,4,5,6,7,8,9,10,11,12], days6 = 3
print(shipWithinDays(weights6, days6)) # Output: 12

weights7 = [1,2,3,4,5,6,7,8,9,10,11,12,13], days7 = 4
print(shipWithinDays(weights7, days7)) # Output: 13

weights8 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], days8 = 5
print(shipWithinDays(weights8, days8)) # Output: 14

weights9 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], days9 = 6
print(shipWithinDays(weights9, days9)) # Output: 15

weights10 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], days10 = 7
print(shipWithinDays(weights10, days10)) # Output: 16