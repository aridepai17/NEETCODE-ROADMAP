# HOUSE ROBBER 4

'''
There are several consecutive houses along a street, each of which has some money inside.
There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.
You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.
Return the minimum capability of the robber out of all the possible ways to steal at least k houses.
'''

'''
Algorithm and Intuition (Binary Search on the Answer):
Intuition:
The problem asks for the minimum capability, where capability is the maximum amount stolen from a single house.
This suggests that we can binary search on the possible values of this maximum amount (the "capability").
If a robber can steal at least `k` houses with a maximum capability `X`, they can also steal at least `k` houses with any capability `Y > X`.
This monotonic property allows us to use binary search to find the smallest `X` that satisfies the condition.

The core of the problem is to define a `canSteal(capability)` function:
Given a maximum `capability` (i.e., the robber will only steal from houses with money `nums[i] <= capability`),
can the robber steal at least `k` houses without stealing from adjacent homes?

Algorithm Steps:
1. Define the search space for the `capability`:
 - `left = min(nums)`: The smallest possible capability is the minimum money in any house.
 - `right = max(nums)`: The largest possible capability is the maximum money in any house.
2. Implement the `canSteal(capability)` helper function:
 - Iterate through `nums`. If `nums[i] <= capability`, the robber can steal this house. Increment a `count` of stolen houses and skip the next house (`i += 2`) because adjacent houses cannot be robbed.
 - Otherwise, if `nums[i] > capability`, the robber cannot steal this house, so move to the next house (`i += 1`).
 - If `count` reaches `k` at any point, return `True`.
 - If the loop finishes and `count < k`, return `False`.
3. Perform binary search on the range `[left, right]`:
 - If `canSteal(mid)` is `True`, it means `mid` is a possible answer. We try to find an even smaller capability, so we set `right = mid - 1`.
 - If `canSteal(mid)` is `False`, `mid` is too low. We need a higher capability, so we set `left = mid + 1`.
4. The loop terminates when `left > right`. The value of `left` will be the smallest capability for which `canSteal` returned `True`. Return `left`.
'''

def minCapability(nums, k):
    def canSteal(capability):
        i = 0
        count = 0
        
        while i < len(nums):
            if nums[i] <= capability:
                i += 2
                count += 1
            else:
                i += 1
            if count == k:
                return True
        return False
    
    left = min(nums)
    right = max(nums)
    
    while left <= right:
        mid = (left + right) // 2
        
        if canSteal(mid):
            right = mid - 1
        else:
            left = mid + 1
            
    return left

'''
Time Complexity: O(N log M)
- The binary search operates on the range [min(nums), max(nums)]. Let M be the difference between max(nums) and min(nums).
  The number of iterations for the binary search is O(log M).
- Inside the `while` loop, the `canSteal` function is called.
- The `canSteal` function iterates through the `nums` array once.
  Let N be the number of houses (len(nums)). This takes O(N) time.
- Therefore, the total time complexity is O(N log M).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for variables: `left`, `right`, `mid`, `i`, `count`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [2, 3, 5, 9], k1 = 2
print(minCapability(nums1, k1)) # Output: 5

nums2 = [2, 7, 9, 3, 1], k2 = 2
print(minCapability(nums2, k2)) # Output: 3

nums3 = [10, 2, 3, 100, 3, 1], k3 = 3
print(minCapability(nums3, k3)) # Output: 3

nums4 = [1, 1, 1], k4 = 1
print(minCapability(nums4, k4)) # Output: 1

nums5 = [1, 2, 3, 4, 5], k5 = 3
print(minCapability(nums5, k5)) # Output: 3

nums6 = [8, 6, 7, 8, 7, 6, 8], k6 = 3
print(minCapability(nums6, k6)) # Output: 7

nums7 = [100], k7 = 1
print(minCapability(nums7, k7)) # Output: 100

nums8 = [5, 1, 4, 6, 2, 7, 3], k8 = 4
print(minCapability(nums8, k8)) # Output: 4

nums9 = [12, 34, 56, 78, 90], k9 = 2
print(minCapability(nums9, k9)) # Output: 34

nums10 = [10, 20, 10, 30, 10, 40, 10], k10 = 3
print(minCapability(nums10, k10)) # Output: 10