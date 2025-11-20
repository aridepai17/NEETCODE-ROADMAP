# MINIMIZE THE MAXIMUM DIFFERENCE OF PAIRS

'''
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. 
Also, ensure no index appears more than once amongst the p pairs.
Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
'''

"""
Algorithm (step by step):
1. If p == 0, return 0 because no pairs are required.
2. Sort nums in nondecreasing order. Greedy adjacent pairing is optimal only on a sorted array.
3. Initialize binary search bounds for the answer:
   - left = 0 (minimum possible maximum difference)
   - right = max(nums) (a safe upper bound on the difference)
   - result = right (store best feasible answer as we search)
4. Define helper isValid(threshold):
   - Greedily scan nums from left to right with index i.
   - Whenever nums[i+1] - nums[i] <= threshold, form a pair (i, i+1), increment pair count, and advance i by 2.
   - Otherwise, advance i by 1.
   - If the number of formed pairs >= p at any time, return True; otherwise return False after the scan.
5. While left <= right:
   - mid = (left + right) // 2  (candidate maximum difference)
   - If isValid(mid) is True:
       • Update result = mid and move right = mid - 1 to search for a smaller feasible difference.
     Else:
       • Move left = mid + 1 to allow larger differences.
6. Return result as the minimal maximum difference that allows at least p non-overlapping pairs.
"""

def minimizeMax(nums, p):
    def isValid(threshold):
        count = 0
        i = 0
        
        while i < len(nums) - 1:
            if abs(nums[i] - nums[i + 1]) <= threshold:
                count += 1
                i += 2
            else:
                i += 1
            if count >= p:
                return True
        return False
        
    if p == 0:
        return 0
    
    nums.sort()
    left = 0
    right = max(nums)
    result = max(nums)
    
    while left <= right:
        mid = (left + right) // 2 # mid = left + (right - left) // 2
        
        if isValid(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return result

'''
Time Complexity: O(nlog(max(nums)))
- The algorithm performs a binary search over the answer range [0, max(nums)], which takes O(log U) iterations, where U = max(nums).
- In each iteration, it runs `isValid(threshold)`, which linearly scans the array once using a greedy pairing of adjacent elements, taking O(n), where n = len(nums).
- Therefore, total time is O(n · log U).

Notes:
- This analysis matches the code as written (no sorting step present). If an implementation pre-sorts `nums` to ensure greedy adjacent pairing is valid, add an O(n log n) sort once; total would then be O(n log n + n log U).

Space Complexity: O(1)
- O(1) auxiliary space. The algorithm uses a constant number of scalar variables (pointers/counters and bounds) and no additional data structures that scale with n.
'''

# Test Cases (10)
nums1 = [10,1,2,7,1,3]; p1 = 2
print(minimizeMax(nums1, p1))  # Expected: 1

nums2 = [4,2,1,2]; p2 = 1
print(minimizeMax(nums2, p2))  # Expected: 0

nums3 = [1,3,6,19,20]; p3 = 2
print(minimizeMax(nums3, p3))  # Expected: 2

nums4 = [1,1,1,1]; p4 = 2
print(minimizeMax(nums4, p4))  # Expected: 0

nums5 = [1,5,9,14]; p5 = 1
print(minimizeMax(nums5, p5))  # Expected: 4

nums6 = [1,5,9,14]; p6 = 2
print(minimizeMax(nums6, p6))  # Expected: 5

nums7 = [3,4,2,3,2,1]; p7 = 2
print(minimizeMax(nums7, p7))  # Expected: 1

nums8 = [1,6,1,2,6,2]; p8 = 3
print(minimizeMax(nums8, p8))  # Expected: 0

nums9 = [9,1,10,3,8,4]; p9 = 2
print(minimizeMax(nums9, p9))  # Expected: 1

nums10 = [5,5,10,10,15,15]; p10 = 3
print(minimizeMax(nums10, p10))  # Expected: 0