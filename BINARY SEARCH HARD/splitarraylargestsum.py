# SPLIT ARRAY LARGEST SUM

'''
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

INTUITION:
This problem can be solved using binary search on the answer space. The key insight is:
- We are searching for the minimum possible largest sum (let's call it 'target')
- The answer must be between max(nums) and sum(nums)
  * Lower bound: max(nums) - because each subarray must contain at least one element
  * Upper bound: sum(nums) - because we could put all elements in one subarray
- For any candidate value, we can check if it's possible to split the array into k subarrays
  where no subarray sum exceeds that candidate value
- If it's possible with a candidate value, we can try a smaller value (search left)
- If it's not possible, we need a larger value (search right)

ALGORITHM:
1. Define search boundaries:
   - left = max(nums)  (minimum possible answer)
   - right = sum(nums) (maximum possible answer)

2. Binary search on the answer space:
   - mid = (left + right) // 2
   - Check if we can split array into k subarrays with max sum <= mid
   
3. Helper function canSplit(largest):
   - Greedily form subarrays by adding elements until sum exceeds 'largest'
   - Count how many subarrays are needed
   - If count <= k, return True (we can split with max sum <= largest)
   - Otherwise, return False (we need more subarrays, so largest is too small)

4. Binary search logic:
   - If canSplit(mid) is True:
     * We can achieve max sum = mid, try smaller values
     * right = mid - 1
   - If canSplit(mid) is False:
     * We cannot achieve max sum = mid, need larger values
     * left = mid + 1

5. Return left (the minimum largest sum that allows k splits)
'''


def splitArray(nums, k):
    def canSplit(largest):
        subarray = 1
        currentSum = 0
        
        for num in nums:
            currentSum += num
            if currentSum > largest:
                subarray += 1
                currentSum = num
                
        if subarray <= k:
            return True
        return False
    
    left = max(nums)
    right = sum(nums)
    
    while left <= right:
        mid = (left + right) // 2
        if canSplit(mid):

            right = mid - 1
        else:
            left = mid + 1
            
    return left

'''
Time Complexity: O(n * log(sum(nums)))
    - canSplit(largest): O(n) - iterates through all elements once
    - Binary search: O(log(sum(nums))) - search space from max(nums) to sum(nums)
    - Each binary search iteration calls canSplit: O(n)
    - Overall: O(n * log(sum(nums)))

Space Complexity: O(1)
    - Only uses a constant amount of extra space for variables
    - No additional data structures that scale with input size
'''

# Test Cases
nums1 = [7,2,5,10,8], k1 = 2
print(splitArray(nums1, k1)) # Output: 18

nums2 = [1,2,3,4,5], k2 = 2
print(splitArray(nums2, k2)) # Output: 9

nums3 = [1,4,4], k3 = 3
print(splitArray(nums3, k3)) # Output: 4

nums4 = [10,20,30,40], k4 = 1
print(splitArray(nums4, k4)) # Output: 100

nums5 = [1,2,3,4,5], k5 = 5
print(splitArray(nums5, k5)) # Output: 5

nums6 = [1,1,1,1,1], k6 = 3
print(splitArray(nums6, k6)) # Output: 2

nums7 = [1,2,3,4,5,6,7,8,9,10], k7 = 3
print(splitArray(nums7, k7)) # Output: 21

nums8 = [10,9,8,7,6,5,4,3,2,1], k8 = 4
print(splitArray(nums8, k8)) # Output: 19

nums9 = [100,200,300,400,500], k9 = 2
print(splitArray(nums9, k9)) # Output: 900

nums10 = [1,2,3], k10 = 2
print(splitArray(nums10, k10)) # Output: 3