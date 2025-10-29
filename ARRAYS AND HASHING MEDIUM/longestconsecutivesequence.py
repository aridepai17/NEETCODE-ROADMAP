# LONGEST CONSECUTIVE SEQUENCE

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''

def longestConsecutive(nums):
    numSet = set(nums)
    currentStreak = 0
    longestStreak = 0
    
    for num in numSet:
        if (num - 1) not in numSet:
            currentNum = num
            currentStreak = 1
            
            while (currentNum + 1) in numSet:
                currentNum += 1
                currentStreak += 1
                
        longestStreak = max(longestStreak, currentStreak)
        
    return longestStreak

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The first step is to convert the list `nums` into a set `numSet`. This operation takes O(N) time on average, as it involves iterating through all N elements and inserting them into the hash set.
- The main part of the algorithm is the loop that iterates through each number in `numSet`. Although there is a nested `while` loop, the algorithm is still O(N).
- This is because the `while` loop is only entered for numbers that are the start of a consecutive sequence (i.e., `num - 1` is not in the set).
- Each number in the set is visited at most twice: once by the outer `for` loop and at most once by the inner `while` loop.
- For example, if we have a sequence `1, 2, 3, 4`, the `for` loop will check `1`, `2`, `3`, and `4`. The `while` loop will only start when `num` is `1`. It will then iterate through `2`, `3`, and `4`. The numbers `2`, `3`, and `4` will be skipped by the outer `if` condition because their preceding numbers (`1`, `2`, `3`) are in the set.
- Therefore, the total number of operations is proportional to N, making the time complexity O(N).

Space Complexity: O(N)
- The space complexity is determined by the additional space used by the hash set `numSet`.
- In the worst-case scenario, all elements in the input array `nums` are unique. In this case, the `numSet` will store N elements.
- Therefore, the space required for the set is O(N).
- The other variables (`currentStreak`, `longestStreak`, `currentNum`) use a constant amount of space, O(1).
- The dominant factor is the `numSet`, so the overall space complexity is O(N).
'''

# Test Cases
nums1 = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums1)) # Output: 4

nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums2)) # Output: 9

nums3 = []
print(longestConsecutive(nums3)) # Output: 0

nums4 = [5]
print(longestConsecutive(nums4)) # Output: 1

nums5 = [1, 2, 3, 4, 5]
print(longestConsecutive(nums5)) # Output: 5

nums6 = [-1, -2, 0, 1, -3]
print(longestConsecutive(nums6)) # Output: 5

nums7 = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(longestConsecutive(nums7)) # Output: 6

nums8 = [1, 2, 0, 1]
print(longestConsecutive(nums8)) # Output: 3

# Test Case 9: All elements are the same
nums9 = [5, 5, 5, 5, 5]
print(longestConsecutive(nums9)) # Output: 1

# Test Case 10: Multiple sequences of the same max length
nums10 = [1, 2, 3, 10, 11, 12]
print(longestConsecutive(nums10)) # Output: 3