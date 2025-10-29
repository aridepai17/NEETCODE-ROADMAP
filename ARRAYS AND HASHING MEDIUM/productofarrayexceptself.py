# PRODUCT OF ARRAY EXCEPT SELF

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''

def productExceptSelf(nums):
    result = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
        
    return result

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The algorithm makes two passes through the array.
- The first loop iterates from the beginning to the end to calculate the prefix products. This loop runs N times, and each operation inside is O(1). So, this pass takes O(N) time.
- The second loop iterates from the end to the beginning to calculate the postfix products and multiply them with the corresponding prefix products. This loop also runs N times with O(1) operations. This pass also takes O(N) time.
- Since the two passes are sequential, the total time complexity is O(N) + O(N), which simplifies to O(N).

Space Complexity: O(N)
- The space complexity is determined by the space required for the output array `result`.
- The `result` array has the same size as the input array `nums`, which is N. Therefore, it requires O(N) space.
- The variables `prefix` and `postfix` use a constant amount of extra space, O(1).
- The dominant factor is the `result` array, so the overall space complexity is O(N).
- Note: Some problem definitions exclude the output array from space complexity analysis. In that specific case, the space complexity would be O(1). However, it's standard to include it.
'''

# Test Cases
nums1 = [1,2,3,4]
print(productExceptSelf(nums1)) # Output: [24,12,8,6]

nums2 = [-1,1,0,-3,3]
print(productExceptSelf(nums2)) # Output: [0,0,9,0,0]

nums3 = [0,0]
print(productExceptSelf(nums3)) # Output: [0,0]

nums4 = [1,1,1,1]
print(productExceptSelf(nums4)) # Output: [1,1,1,1]

nums5 = [5, 2, 3, 1, 4]
print(productExceptSelf(nums5)) # Output: [24, 60, 40, 120, 30]

# Test Case 6: Array with two elements
nums6 = [2, 5]
print(productExceptSelf(nums6)) # Output: [5, 2]

# Test Case 7: All negative numbers
nums7 = [-2, -3, -4]
print(productExceptSelf(nums7)) # Output: [12, 8, 6]

# Test Case 8: Mix of positive and negative numbers
nums8 = [1, -2, 3, -4]
print(productExceptSelf(nums8)) # Output: [24, -12, 8, -6]

# Test Case 9: Single zero at the end
nums9 = [1, 2, 3, 0]
print(productExceptSelf(nums9)) # Output: [0, 0, 0, 6]

# Test Case 10: Single element array
nums10 = [10]
print(productExceptSelf(nums10)) # Output: [1]