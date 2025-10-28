# SORT COLORS

'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
'''

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1
            
'''
Time Complexity: O(N), where N is the number of elements in the input array `nums`.
- The algorithm uses a single-pass approach with three pointers (`low`, `mid`, `high`).
- The `while` loop runs as long as `mid <= high`. In each iteration, either `mid` is incremented or `high` is decremented.
- This ensures that each element of the array is visited and processed at most a constant number of times.
- The total number of operations is directly proportional to the size of the array.
- Therefore, the time complexity is linear.

Space Complexity: O(1)
- The sorting is done in-place, meaning it modifies the input array directly without using any auxiliary data structures whose size depends on the input size.
- The algorithm only uses a few variables (`low`, `mid`, `high`) to store indices, which occupies a constant amount of extra space.
- The space required does not grow with the size of the input array.
- Thus, the space complexity is constant.
'''

# Test Cases
nums1 = [2,0,2,1,1,0]
sortColors(nums1)
print(nums1) # Output: [0,0,1,1,2,2]

nums2 = [2,0,1]
sortColors(nums2)
print(nums2) # Output: [0,1,2]

nums3 = [0]
sortColors(nums3)
print(nums3) # Output: [0]

nums4 = [1]
sortColors(nums4)
print(nums4) # Output: [1]

nums5 = [2,2,1,1,0,0]
sortColors(nums5)
print(nums5) # Output: [0,0,1,1,2,2]

nums6 = [0, 1, 2]
sortColors(nums6)
print(nums6) # Output: [0, 1, 2]

nums7 = [1, 1, 1]
sortColors(nums7)
print(nums7) # Output: [1, 1, 1]

nums8 = [2, 1, 0, 2, 1, 0]
sortColors(nums8)
print(nums8) # Output: [0, 0, 1, 1, 2, 2]

nums9 = [1, 0]
sortColors(nums9)
print(nums9) # Output: [0, 1]

nums10 = [2, 2, 2, 1, 1, 0, 0, 0]
sortColors(nums10)
print(nums10) # Output: [0, 0, 0, 1, 1, 2, 2, 2]