# ARRAY WITH ELEMENTS NOT EQUAL TO AVERAGE OF NEIGHBORS

'''
You are given a 0-indexed array nums of distinct integers. 
You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.
More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].
Return any rearrangement of nums that meets the requirements.
'''

def rearrangeArray(nums):
    nums.sort()
    result = []
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        result.append(nums[left])
        left += 1
        if left <= right:
            result.append(nums[right])
            right -= 1
            
    return result

'''
Time Complexity: O(N log N)
- The first step is to sort the input array `nums`. In Python, this uses Timsort, which has an average and worst-case time complexity of O(N log N).
- After sorting, the algorithm uses a two-pointer approach (`left` and `right`) to build the `result` array.
- The `while` loop iterates as long as `left <= right`. In each iteration, at least one pointer moves towards the center. The loop runs approximately N/2 times, processing all N elements once. This part of the algorithm takes O(N) time.
- Since the sorting step (O(N log N)) is more time-consuming than the two-pointer traversal (O(N)), the overall time complexity is dominated by sorting.
- Therefore, the time complexity is O(N log N).

Space Complexity: O(N)
- The space complexity is determined by the storage required for the output array and the space used by the sorting algorithm.
- A new list `result` is created to store the rearranged elements. In the end, this list will contain N elements, so it requires O(N) space.
- The sorting algorithm (Timsort) can use up to O(N) auxiliary space in the worst case.
- The variables `left` and `right` use constant O(1) space.
- Therefore, the total auxiliary space complexity is O(N).
'''

# Test Cases
nums1 = [1,2,3,4,5]
print(rearrangeArray(nums1)) # Output: [1, 2, 4, 5, 3]

nums2 = [6,1,7,2,8,3]
print(rearrangeArray(nums2)) # Output: [1, 8, 2, 7, 3, 6]

nums3 = [10, 20, 30, 40]
print(rearrangeArray(nums3)) # Output: [10, 40, 20, 30]

nums4 = [5,4,3,2,1]
print(rearrangeArray(nums4)) # Output: [1, 5, 2, 4, 3]

nums5 = [-2, -1, 0, 1, 2]
print(rearrangeArray(nums5)) # Output: [-2, 2, -1, 1, 0]

nums6 = [100]
print(rearrangeArray(nums6)) # Output: [100]

nums7 = [10, 20]
print(rearrangeArray(nums7)) # Output: [10, 20]

nums8 = [3,1,4,5,9,2,6,8]
print(rearrangeArray(nums8)) # Output: [1, 9, 2, 8, 3, 6, 4, 5]

nums9 = [4, 0, 2, -2]
print(rearrangeArray(nums9)) # Output: [-2, 4, 0, 2]

nums10 = [0,1,2,3,4,5,6,7,8,9]
print(rearrangeArray(nums10)) # Output: [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]