# MAXIMUM PRODUCT SUBARRAY

'''
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.
'''

'''
ALGORITHM:

This problem is trickier than maximum sum subarray because the product can flip signs. 
A negative number multiplied by another negative becomes positive, so we need to track both the maximum and minimum products ending at each position.

At each position, we need to track:
- currentMax: Maximum product ending at current position
- currentMin: Minimum product ending at current position (could become max if multiplied by negative)

Key insight: When we encounter a negative number, swapping currentMax and currentMin gives us the correct values because multiplying by a negative flips the sign.

Algorithm:
1. Initialize currentMax, currentMin, and result to nums[0]
2. For each element nums[i] starting from index 1:
    a. If nums[i] is negative, swap currentMax and currentMin (because negative flips the sign)
    b. Update currentMax = max(nums[i], currentMax * nums[i])
    c. Update currentMin = min(nums[i], currentMin * nums[i])
    d. Update result = max(result, currentMax)
3. Return result
'''

def maxProduct(nums):
    currentMax, currentMin, result = nums[0], nums[0], nums[0]
    
    for i in range(1, len(nums)):
        n = nums[i]
        if n < 0:
            currentMax, currentMin = currentMin, currentMax
            
        currentMax = max(n, currentMax * n)
        currentMin = min(n, currentMin * n)
        result = max(result, currentMax)
        
    return result

'''
Time Complexity: O(N), where N is the length of the array. We iterate through the array once.
Space Complexity: O(1) - only using constant extra space.
'''

# Test Cases

# Test Case 1: Basic case
nums1 = [2, 3, -2, 4]
result1 = maxProduct(nums1)
print(result1) # Expected: 6 (2 * 3)

# Test Case 2: Single element
nums2 = [5]
result2 = maxProduct(nums2)
print(result2) # Expected: 5

# Test Case 3: All negative
nums3 = [-1, -2, -3, -4]
result3 = maxProduct(nums3)
print(result3) # Expected: 24 (-2 * -3 * -4 = -24... wait, let's think: best is (-2)*(-3)*(-4) = -24, or just -1 = -1, so actually 2*3*4 = 24? No, that's wrong. The subarray with product 24 would be [2,3] but there are no 2,3. Let me recalculate: -1*-2 = 2, 2*-3 = -6, -6*-4 = 24. So answer is 24. But wait, that's not a contiguous subarray of the original [-1,-2,-3,-4]. The contiguous subarrays are [-1], [-2], [-3], [-4], [-1,-2], [-2,-3], [-3,-4], [-1,-2,-3], [-2,-3,-4], [-1,-2,-3,-4]. Products: -1, -2, -3, -4, 2, 6, 12, -6, 24, -24. Max is 12? No wait: -2*-3 = 6, then 6*-4 = -24, so no. The max is actually 12 (-3 * -4). Wait let me recalculate all products:
# -1 = -1
# -2 = -2
# -3 = -3
# -4 = -4
# -1*-2 = 2
# -2*-3 = 6
# -3*-4 = 12
# -1*-2*-3 = 6
# -2*-3*-4 = -24
# -1*-2*-3*-4 = 24
# Actually max is 12 from [-3,-4]

nums3_correct = [-3, -1, -2, -4]
result3_correct = maxProduct(nums3_correct)
print(result3_correct) # Expected: 48

# Test Case 4: Contains zero
nums4 = [2, 0, 3, -1]
result4 = maxProduct(nums4)
print(result4) # Expected: 3

# Test Case 5: Mixed positives and negatives
nums5 = [2, 3, -2, -3, -1, 5]
result5 = maxProduct(nums5)
print(result5) # Expected: 15

# Test Case 6: Two elements
nums6 = [2, -5]
result6 = maxProduct(nums6)
print(result6) # Expected: 2

# Test Case 7: Two negative elements
nums7 = [-2, -3]
result7 = maxProduct(nums7)
print(result7) # Expected: 6

# Test Case 8: Large array with zeros
nums8 = [0, 2, -5, 0, -1, 3, 0, -2, 0, 5]
result8 = maxProduct(nums8)
print(result8) # Expected: 15

# Test Case 9: All positive
nums9 = [1, 2, 3, 4, 5]
result9 = maxProduct(nums9)
print(result9) # Expected: 120 (entire array product)

# Test Case 10: Leading negative
nums10 = [-2, 3, -4]
result10 = maxProduct(nums10)
print(result10) # Expected: 24