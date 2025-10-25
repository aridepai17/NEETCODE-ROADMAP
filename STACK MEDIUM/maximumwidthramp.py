# MAXIMUM RAMP WIDTH

'''
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. 
The width of such a ramp is j - i.
Given an integer array nums, return the maximum width of a ramp in nums. 
If there is no ramp in nums, return 0.
'''

def maximumWidthRamp(nums):
    maxRight = [0] * len(nums)
    i = len(nums) - 1
    prevMax = 0
    
    for num in nums[::-1]:
        maxRight[i] = max(num, prevMax)
        prevMax = maxRight[i]
        i -= 1
        
    result = 0
    left = 0
    
    for right in range(len(nums)):
        if nums[left] > maxRight[right]:
            left += 1
        result = max(result, right - left)
        
    return result

'''
Time Complexity: O(N), where N is the length of the input array `nums`.
- The first loop iterates through the array once in reverse to build the `maxRight` array. This takes O(N) time.
- The second loop iterates through the array once with the `right` pointer. The `left` pointer also moves forward, but it does not reset. This two-pointer approach ensures that each element is visited a constant number of times across both pointers. This part is also O(N).
- Since the loops are sequential, the total time complexity is O(N).

Space Complexity: O(N)
- We use an auxiliary array `maxRight` which has the same size as the input array `nums`.
- The space required for this array scales linearly with the size of the input.
- Therefore, the space complexity is O(N).
'''

# Test Cases
nums1 = [6,0,8,2,1,5]
print(maximumWidthRamp(nums1)) # Output: 4 (from i=1, j=5, nums[1]=0, nums[5]=5)

nums2 = [9,8,1,0,1,9,4,0,4,1]
print(maximumWidthRamp(nums2)) # Output: 7 (from i=2, j=9, nums[2]=1, nums[9]=1)

nums3 = [1,2,3,4,5]
print(maximumWidthRamp(nums3)) # Output: 4 (from i=0, j=4)

nums4 = [5,4,3,2,1]
print(maximumWidthRamp(nums4)) # Output: 0

nums5 = [1]
print(maximumWidthRamp(nums5)) # Output: 0

nums6 = []
print(maximumWidthRamp(nums6)) # Output: 0

nums7 = [2,2,1]
print(maximumWidthRamp(nums7)) # Output: 1 (from i=0, j=1)

nums8 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(maximumWidthRamp(nums8)) # Output: 8 (from i=1, j=9)

nums9 = [5, 4, 3, 0, 1, 2, 6]
print(maximumWidthRamp(nums9)) # Output: 6 (from i=0, j=6, nums[0]=5, nums[6]=6)

nums10 = [7, 7, 7, 7, 7]
print(maximumWidthRamp(nums10)) # Output: 4 (from i=0, j=4)