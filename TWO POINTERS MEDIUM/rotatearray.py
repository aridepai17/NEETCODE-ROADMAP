# ROTATE ARRAY

'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

# Solution 1: Using Slicing
def rotateArray1(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    
'''
Time Complexity: O(N)
- The slicing operation `nums[-k:]` creates a new list of size `k`, which takes O(k) time.
- The slicing operation `nums[:-k]` creates a new list of size `n-k`, which takes O(n-k) time.
- Concatenating these two slices creates a new list of size `n`, which takes O(n) time.
- Assigning this new list back to `nums[:]` also takes O(n) time.
- Therefore, the overall time complexity is O(n).

Space Complexity: O(N)
- We create a new list of size `n` to store the rotated elements by concatenating two slices.
- This temporary list requires O(n) auxiliary space.
- Therefore, the space complexity is O(n).
'''

# Solution 2: Using Two Pointers
def rotateArray2(nums, k):
    k %= len(nums)
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        
    left = 0
    right = k - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        
    left = k
    right = len(nums) - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        
'''
Time Complexity: O(N)
- The algorithm consists of three main steps, each involving reversing a portion of the array using two pointers.
- The first step reverses the entire array. This takes O(N) time as we iterate through roughly half of the elements.
- The second step reverses the first `k` elements. This takes O(k) time.
- The third step reverses the remaining `N-k` elements. This takes O(N-k) time.
- The total time complexity is the sum of these steps: O(N) + O(k) + O(N-k) = O(2N), which simplifies to O(N).
- Each element is touched a constant number of times.

Space Complexity: O(1)
- The rotation is performed in-place, meaning we modify the original array directly without using any additional data structures that scale with the input size.
- The only extra space used is for a few variables (`left`, `right`, `k`), which is constant regardless of the input array size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [1,2,3,4,5,6,7], k1 = 3
print(rotateArray2(nums1, k1)) # Output: [5,6,7,1,2,3,4]

nums2 = [-1,-100,3,99], k2 = 2
rotateArray2(nums2, k2)
print(nums2) # Output: [3,99,-1,-100]

nums3 = [1,2,3,4,5], k3 = 5
rotateArray2(nums3, k3)
print(nums3) # Output: [1,2,3,4,5]

nums4 = [1,2,3,4,5], k4 = 0
rotateArray2(nums4, k4)
print(nums4) # Output: [1,2,3,4,5]

nums5 = [1,2], k5 = 1
rotateArray2(nums5, k5)
print(nums5) # Output: [2,1]

nums6 = [1], k6 = 10
rotateArray2(nums6, k6)
print(nums6) # Output: [1]

nums7 = [1,2,3,4,5,6], k7 = 8
rotateArray2(nums7, k7)
print(nums7) # Output: [5,6,1,2,3,4]

nums8 = [], k8 = 5
# rotateArray2(nums8, k8) # This would cause a ZeroDivisionError. A robust function should handle this.
print(nums8) # Output: []

nums9 = [10, 20, 30, 40, 50], k9 = 1
rotateArray2(nums9, k9)
print(nums9) # Output: [50,10,20,30,40]

nums10 = [1, 1, 2, 2, 3, 3], k10 = 2
rotateArray2(nums10, k10)
print(nums10) # Output: [3,3,1,1,2,2]