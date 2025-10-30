# CONTIGUOUS ARRAY

'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
'''

def findMaxLength(nums):
    hashMap = {0 : -1}
    currentSum = 0
    maxLength = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            currentSum -= 1
        else:
            currentSum += 1
            
        if currentSum in hashMap:
            firstIndex = hashMap[currentSum]
            currentLength = i - firstLength
            maxLength = max(maxLength, currentLength)
        else:
            hashMap[currentLength] = i
            
    return maxLength

'''
Time Complexity: O(N)
- The function iterates through the input array `nums` exactly once, where N is the length of `nums`.
- All operations inside the loop (dictionary lookup, update, arithmetic operations) are O(1).
- Therefore, the overall time complexity is O(N).

Space Complexity: O(N)
- A hash map is used to store the `currentSum` values and their earliest indices.
- In the worst case, each unique cumulative sum gets an entry in the hash map resulting in up to N different keys.
- Thus, the space complexity is O(N).
'''

# Test Cases
nums1 = [0,1]
print(findMaxLength(nums1)) # Output: 2

nums2 = [0,1,0]
print(findMaxLength(nums2)) # Output: 2

nums3 = [0,0,1,0,0,0,1,1]
print(findMaxLength(nums3)) # Output: 6

nums4 = [0,1,1,0,1,1,1,0]
print(findMaxLength(nums4)) # Output: 4

nums5 = [1,1,1,1,0,0,0,0]
print(findMaxLength(nums5)) # Output: 8

nums6 = [0,1,0,1,0,1]
print(findMaxLength(nums6)) # Output: 6

nums7 = []
print(findMaxLength(nums7)) # Output: 0

nums8 = [0]
print(findMaxLength(nums8)) # Output: 0

nums9 = [1]
print(findMaxLength(nums9)) # Output: 0

nums10 = [0,0,1,1,0]
print(findMaxLength(nums10)) # Output: 4