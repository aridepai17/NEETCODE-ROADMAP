# CONTAINS DUPLICATE 2

'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

def containsNearbyDuplicate(nums, k):
    window = set()
    left = 0
    
    for right in range(len(nums)):
        if right - left > k:
            window.remove(nums[left])
            left += 1
        if nums[right] in window:
            return True
        window.add(nums[right])
        
    return False

'''
Time Complexity: O(N)
- The algorithm iterates through the input array `nums` exactly once using the `right` pointer.
- Inside the loop, the operations on the hash set (`add`, `remove`, and checking for existence) take, on average, constant time, O(1).
- As each element is processed once, the total time complexity is linear with respect to the number of elements in the array, N.

Space Complexity: O(min(N, k))
- The algorithm uses a hash set, `window`, to store the elements within the current sliding window.
- The size of this window is at most `k + 1`.
- The number of elements in the set is therefore bounded by `k`.
- It is also bounded by the total number of elements, `N`, in the case where `k` is larger than `N`.
- Thus, the space required is O(min(N, k)).
'''

# Test Cases
nums1 = [1, 2, 3, 1], k1 = 3
print(containsNearbyDuplicate(nums1, k1)) # Output: True

nums2, k2 = [1,0,1,1], 1
print(containsNearbyDuplicate(nums2, k2)) # Output: True

nums3, k3 = [1,2,3,1,2,3], 2
print(containsNearbyDuplicate(nums3, k3)) # Output: False

nums4, k4 = [], 0
print(containsNearbyDuplicate(nums4, k4)) # Output: False

nums5, k5 = [1], 1
print(containsNearbyDuplicate(nums5, k5)) # Output: False

nums6, k6 = [1, 1], 0
print(containsNearbyDuplicate(nums6, k6)) # Output: False

nums7, k7 = [1, 2, 3, 4, 5], 5
print(containsNearbyDuplicate(nums7, k7)) # Output: False

nums8, k8 = [1, 2, 1], 100
print(containsNearbyDuplicate(nums8, k8)) # Output: True

nums9, k9 = [99, 99], 2
print(containsNearbyDuplicate(nums9, k9)) # Output: True

nums10, k10 = [4,1,2,3,1,5], 3
print(containsNearbyDuplicate(nums10, k10)) # Output: True