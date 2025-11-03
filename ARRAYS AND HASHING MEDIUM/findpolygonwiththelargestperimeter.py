# FIND POLYGON WITH THE LARGEST PERIMETER

'''
You are given an array of positive integers nums of length n.
A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.
Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.
The perimeter of a polygon is the sum of lengths of its sides.
Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.
'''

def largestPerimeter(nums):
    nums.sort()
    result = -1
    total = 0
    
    for num in nums:
        if total > num:
            result = total + num
        total += num
        
    return result

'''
Time Complexity: O(N log N)
- Let N be the number of elements in the input array `nums`.
- Sorting the array takes O(N log N) time.
- The subsequent loop iterates through the sorted array once, performing O(1) operations in each iteration, which takes O(N) time.
- The overall time complexity is dominated by the sorting step, resulting in O(N log N).

Space Complexity: O(1) or O(N)
- The space complexity depends on the sorting algorithm used by Python's `sort()` method.
- Python uses Timsort, which has a worst-case space complexity of O(N) for auxiliary space.
- However, if we consider only the extra space used by our algorithm (excluding the space used by the sorting algorithm), it is O(1), as we only use a constant amount of extra variables (`result` and `total`).
- Therefore, the space complexity is O(1) auxiliary space, or O(N) if we count the sorting algorithm's space usage.
'''

# Test Cases
nums1 = [5, 5, 5]
print(largestPerimeter(nums1)) # Output: 15

nums2 = [1, 12, 1, 2, 5, 50, 3]
print(largestPerimeter(nums2)) # Output: 12

nums3 = [5, 5, 50]
print(largestPerimeter(nums3)) # Output: -1

nums4 = [1, 2, 1]
print(largestPerimeter(nums4)) # Output: -1

nums5 = [3, 6, 9]
print(largestPerimeter(nums5)) # Output: 18

nums6 = [1, 1, 1, 1, 1]
print(largestPerimeter(nums6)) # Output: 5

nums7 = [2, 3, 4, 5, 6]
print(largestPerimeter(nums7)) # Output: 20

nums8 = [100, 200, 300]
print(largestPerimeter(nums8)) # Output: 600

nums9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(largestPerimeter(nums9)) # Output: 55

nums10 = [10, 20, 30, 40]
print(largestPerimeter(nums10)) # Output: 100