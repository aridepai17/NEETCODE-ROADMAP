# FIND THE DUPLICATE NUMBER

'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.
'''

'''
ALGORITHM:

This problem can be solved using Floyd's Tortoise and Hare algorithm, which is typically used for detecting cycles in linked lists.
The key insight is to treat the array `nums` as a linked list where `nums[i]` is the next node for `i`.
Since there is a duplicate number and all numbers are within the range [1, n], this guarantees a cycle.

1. FIND THE INTERSECTION POINT OF THE TWO POINTERS:
   - Initialize two pointers, `slow` and `fast`, both starting at index 0.
   - In each step:
     - `slow` moves one step: `slow = nums[slow]`
     - `fast` moves two steps: `fast = nums[nums[fast]]`
   - Continue this process until `slow` and `fast` meet (i.e., `slow == fast`). This meeting point is within the cycle.

2. FIND THE START OF THE CYCLE (THE DUPLICATE NUMBER):
   - Initialize a new pointer, `slow2`, starting at index 0.
   - Keep `slow` at its intersection point.
   - In each step:
     - `slow` moves one step: `slow = nums[slow]`
     - `slow2` moves one step: `slow2 = nums[slow2]`
   - The point where `slow` and `slow2` meet is the start of the cycle, which is the duplicate number.
   - Return `slow` (or `slow2`).
'''

def findDuplicate(nums):
    slow = 0
    fast = 0
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
        
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

'''
Time Complexity: O(N), where N is the number of elements in `nums`.
- The first `while` loop (finding the intersection point) traverses the array. In the worst case, `slow` and `fast` pointers will traverse the cycle and reach the intersection point. The total number of steps is proportional to N.
- The second `while` loop (finding the start of the cycle) also traverses the array. In the worst case, both `slow` and `slow2` will traverse the cycle and reach the start of the cycle. The total number of steps is proportional to N.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We only use a few pointers (`slow`, `fast`, `slow2`), which consume constant extra space.
- We are not modifying the input array.
'''

# Test Cases
nums1 = [1,3,4,2,2]
print(findDuplicate(nums1)) # Output: 2

nums2 = [3,1,3,4,2]
print(findDuplicate(nums2)) # Output: 3

nums3 = [3,3,3,3,3]
print(findDuplicate(nums3)) # Output: 3

nums4 = [1,1]
print(findDuplicate(nums4)) # Output: 1

nums5 = [1,1,2]
print(findDuplicate(nums5)) # Output: 1

nums6 = [2,5,9,6,9,3,8,9,7,1]
print(findDuplicate(nums6)) # Output: 9

nums7 = [4,3,1,4,2]
print(findDuplicate(nums7)) # Output: 4

nums8 = [1,2,3,4,5,6,7,8,9,9]
print(findDuplicate(nums8)) # Output: 9

nums9 = [7,9,7,4,2,8,7,7,1,5]
print(findDuplicate(nums9)) # Output: 7

nums10 = [1,1,2,3,4,5,6,7,8,9,10]
print(findDuplicate(nums10)) # Output: 1