# MAJORITY ELEMENT 2

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
'''

def majorityElement(nums):
    count1 = 0
    count2 = 0
    candidate1 = None
    candidate2 = None
    n = len(nums)
    
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
            
    result = []
    for candidate in set([candidate1, candidate2]):
        if nums.count(candidate) > n // 3:
            result.append(candidate)
            
    return result

'''
Time Complexity: O(N)
- The algorithm processes the input list nums twice:
1. The first pass assigns candidates for majority elements, iterating through nums once (O(N)).
2. The second pass counts the occurrences of the candidates, using nums.count(candidate) for at most two candidates. Each count is O(N) in the worst case, but there are only two candidates, so it is still O(N).
- Therefore, the total time complexity is O(N).

Space Complexity: O(1)
- Only a constant amount of extra space is used for a few counters and candidate variables, regardless of the size of the input list.
- The result list will contain at most two elements, as there can be at most two elements that appear more than ⌊ n/3 ⌋ times.
- No data structure used grows with the input size, so the space complexity is O(1).
'''

# Test Cases
nums1 = [3,2,3]
print(majorityElement(nums1)) # Output: [3]

nums2 = [1]
print(majorityElement(nums2)) # Output: [1]

nums3 = [1,2]
print(majorityElement(nums3)) # Output: []

nums4 = [1,1,1,3,3,2,2,2]
print(majorityElement(nums4)) # Output: [1, 2]

nums5 = [2,2,9,3,9,3,9,3,9,3,9,3,9]
print(majorityElement(nums5)) # Output: [9, 3]

nums6 = []
print(majorityElement(nums6)) # Output: []

nums7 = [4,4,4,4,4,5,5,5,5]
print(majorityElement(nums7)) # Output: [4, 5]

nums8 = [2,2,1,1,1,2,2]
print(majorityElement(nums8)) # Output: [2]

nums9 = [1,1,2,2,3,3,4,4]
print(majorityElement(nums9)) # Output: []

nums10 = [0,0,0,0,1,2,3,4,5,6,7]
print(majorityElement(nums10)) # Output: [0]