# BOATS TO SAVE PEOPLE

'''
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.
'''

def numRescueBoats(people, limit):
    people.sort()
    boats = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        boats += 1
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        
    return boats

'''
Time Complexity: O(N log N)
- The first step is sorting the `people` array, which takes O(N log N) time, where N is the number of people.
- The two-pointer approach (`left` and `right`) involves a single pass through the sorted array.
- The `while` loop runs as long as `left <= right`. In each iteration, the `right` pointer always moves one step to the left, and the `left` pointer may or may not move to the right.
- Since the pointers only move towards each other, the loop will run at most N times. This traversal takes O(N) time.
- The sorting step is the bottleneck, so the overall time complexity is dominated by it.
- Therefore, the time complexity is O(N log N).

Space Complexity: O(log N) or O(N)
- The space complexity is primarily determined by the sorting algorithm used.
- Python's `sort()` method is performed in-place, but it can use auxiliary space for its implementation (Timsort). The space complexity of Timsort can range from O(log N) to O(N) in the worst case.
- Apart from the space used by sorting, the algorithm uses only a few variables (`boats`, `left`, `right`), which occupy a constant amount of space, O(1).
- Therefore, the dominant factor for space is the sorting algorithm, resulting in a space complexity of O(log N) to O(N).
'''

# Test Cases
people1 = [1, 2], limit1 = 3
print(numRescueBoats(people1, limit1)) # Output: 1

people2 = [3, 5, 3, 4], limit2 = 5
print(numRescueBoats(people2, limit2)) # Output: 4

people3 = [3, 2, 2, 1], limit3 = 3
print(numRescueBoats(people3, limit3)) # Output: 3

people4 = [1, 2, 3, 4], limit4 = 5
print(numRescueBoats(people4, limit4)) # Output: 2

people5 = [5], limit5 = 5
print(numRescueBoats(people5, limit5)) # Output: 1

people6 = [2, 2, 2, 2], limit6 = 5
print(numRescueBoats(people6, limit6)) # Output: 2

people7 = [3, 3, 3, 3], limit7 = 5
print(numRescueBoats(people7, limit7)) # Output: 4

people8 = [5, 1, 4, 2, 3], limit8 = 6
print(numRescueBoats(people8, limit8)) # Output: 3

people9 = [6, 6, 6, 6, 6], limit9 = 10
print(numRescueBoats(people9, limit9)) # Output: 5

people10 = [1, 2, 3], limit10 = 3
print(numRescueBoats(people10, limit10)) # Output: 2