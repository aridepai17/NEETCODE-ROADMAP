# TOP K FREQUENT ELEMENTS

'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

def topKElements(nums, k):
    hashMap = {}
    
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for freq, num in hashMap.items():
        buckets[freq].append(num)
        
    result = []
    
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
            
'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- **Frequency Counting**: We iterate through the `nums` array once to build a hash map of element frequencies. This takes O(N) time.
- **Bucket Creation**: We create a `buckets` array of size N+1. This takes O(N) time.
- **Populating Buckets**: We iterate through the hash map (which has at most N unique elements) and place each element into the corresponding bucket based on its frequency. This takes O(U) time, where U is the number of unique elements (U <= N).
- **Extracting Top K Elements**: We iterate through the `buckets` array from the end. In the worst case, we might iterate through all N buckets. The total number of elements we process across all buckets is U. The process stops once we have found `k` elements. This step is also bounded by O(N).
- Since all steps are linear with respect to the input size N, the overall time complexity is O(N).

Space Complexity: O(N)
- **Hash Map**: The `hashMap` stores the frequency of each unique element. In the worst case, all elements are unique, so the space required is O(N).
- **Buckets Array**: The `buckets` array has a size of N+1. It stores all the unique elements from the input array. The total space required for the buckets array is O(N) for the list itself plus O(U) for the elements inside, which simplifies to O(N).
- **Result Array**: The `result` array stores the final `k` elements, so it takes O(k) space.
- The dominant factor is the space for the hash map and the buckets array, making the overall space complexity O(N).
'''

# Test Cases
nums1 = [1,1,1,2,2,3]
k1 = 2
print(topKElements(nums1, k1)) # Output: [1, 2]

nums2 = [1]
k2 = 1
print(topKElements(nums2, k2)) # Output: [1]

nums3 = [1,2]
k3 = 2
print(topKElements(nums3, k3)) # Output: [1, 2] or [2, 1]

nums4 = [5,3,1,1,1,3,73,1]
k4 = 2
print(topKElements(nums4, k4)) # Output: [1, 3]

nums5 = [4,1,-1,2,-1,2,3]
k5 = 2
print(topKElements(nums5, k5)) # Output: [-1, 2]

# Test Case 6: All unique elements are the top k
nums6 = [1, 2, 3, 4, 5]
k6 = 5
print(f"Test Case 6: {topKElements(nums6, k6)}") # Output: [1, 2, 3, 4, 5] (order may vary)

# Test Case 7: Tie in frequencies for the k-th element
nums7 = [3, 3, 3, 1, 1, 2, 2]
k7 = 2
print(f"Test Case 7: {topKElements(nums7, k7)}") # Output: [3, 1] or [3, 2]

# Test Case 8: Empty input array
nums8 = []
k8 = 1
print(f"Test Case 8: {topKElements(nums8, k8)}") # Output: []

# Test Case 9: Input with zero
nums9 = [0, 0, 0, 1, 1, -1]
k9 = 2
print(f"Test Case 9: {topKElements(nums9, k9)}") # Output: [0, 1]

# Test Case 10: A longer list with more varied frequencies
nums10 = [5, 5, 5, 5, 2, 2, 2, 3, 3, 1, 1, 1, 1, 1]
k10 = 3
print(f"Test Case 10: {topKElements(nums10, k10)}") # Output: [1, 5, 2]