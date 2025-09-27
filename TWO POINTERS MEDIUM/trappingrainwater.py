# TRAPPING RAINWATER

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

# Solution 1: Using Easier Intuition - Two Pointers + if-else loop
def trap1(height):
    left = 0
    right = len(height) - 1
    total = 0
    maxLeft = 0
    maxRight = 0
    
    while left < right:
        if height[left] <= height[right]:
            if maxLeft < height[left]:
                maxLeft = height[left]
            else:
                total += maxLeft - height[left]
            left += 1
        else:
            if maxRight < height[right]:
                maxRight = height[right]
            else:
                total += maxRight - height[right]
            right -= 1
            
    return total

'''
Time Complexity: O(N)
- We use a two-pointer approach with `left` and `right` pointers starting from the two ends of the array.
- The `left` pointer only moves forward, and the `right` pointer only moves backward.
- The loop continues until the pointers meet, which means each element in the `height` array is visited at most once.
- Therefore, the time complexity is linear with respect to the number of elements, N.

Space Complexity: O(1)
- We only use a few variables to store the pointers (`left`, `right`) and the maximum heights seen so far (`maxLeft`, `maxRight`).
- The amount of extra space used does not depend on the size of the input array.
- Thus, the space complexity is constant.
'''

# Solution 2: Using Better Intuition But Same Process
def trap2(height):
    left = 0
    right = len(height) - 1
    total = 0
    maxLeft = height[left]
    maxRight = height[right]
    
    while left < right:
        if maxLeft < maxRight:
            left += 1
            maxLeft = max(maxLeft, height[left])
            total += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            total += maxRight - height[right]
            
    return total

'''
Time Complexity: O(N)
- The algorithm uses a two-pointer approach, with `left` starting at the beginning and `right` at the end of the array.
- The `while` loop continues as long as `left` is less than `right`.
- In each iteration, either the `left` pointer moves one step to the right or the `right` pointer moves one step to the left.
- The pointers will eventually meet, and each element of the array is visited at most once.
- Thus, the time complexity is linear in the size of the input array, N.

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- We only need a few variables to store the pointers (`left`, `right`), the maximum heights found so far (`maxLeft`, `maxRight`), and the total water trapped.
- The space required does not grow with the size of the input array.
'''

# Test Cases
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap2(height1)) # Output: 6

height2 = [4,2,0,3,2,5]
print(trap2(height2)) # Output: 9

height3 = []
print(trap2(height3)) # Output: 0

height4 = [1]
print(trap2(height4)) # Output: 0

height5 = [1, 2]
print(trap2(height5)) # Output: 0

height6 = [3, 3, 3]
print(trap2(height6)) # Output: 0

height7 = [5, 4, 3, 2, 1]
print(trap2(height7)) # Output: 0

height8 = [1, 2, 3, 4, 5]
print(trap2(height8)) # Output: 0

height9 = [2, 0, 2]
print(trap2(height9)) # Output: 2

height10 = [5,5,1,7,1,1,5,2,7,6]
print(trap2(height10)) # Output: 23