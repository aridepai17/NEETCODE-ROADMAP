# CONTAINER WITH MOST WATER

'''
ou are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice
'''

# Solution 1: Brute Force
def maxArea1(height):
    result = 0
    n = len(height)
    
    for left in range(n):
        for right in range(left + 1, n):
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)
            
    return result

'''
Time Complexity: O(N^2)
- The algorithm uses a nested loop to check every possible pair of lines.
- The outer loop iterates from `left = 0` to `n-1`.
- The inner loop iterates from `right = left + 1` to `n-1`.
- This results in approximately n * (n-1) / 2 pairs being checked.
- For each pair, we perform a constant number of operations (subtraction, min, multiplication, max).
- Therefore, the total time complexity is proportional to the number of pairs, which is O(N^2).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- We only need a few variables to store the maximum area found so far (`result`), the loop indices (`left`, `right`), and the calculated area.
- The space required for these variables does not depend on the size of the input array `height`.
- Therefore, the space complexity is O(1).
'''

# Solution 2: Using Two Pointers and One Pass
def maxArea2(height):
    result = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        area = (right - left) * min(height[left], height[right])
        result = max(result, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return result

'''
Time Complexity: O(N)
- The algorithm uses a two-pointer approach with one pass through the array.
- The `left` pointer starts at the beginning (index 0), and the `right` pointer starts at the end (index n-1).
- In each iteration of the `while` loop, either the `left` pointer is incremented or the `right` pointer is decremented.
- The pointers move towards each other until they meet, meaning each element is visited at most once by one of the pointers.
- This results in a single pass through the array, leading to a linear time complexity.
- Therefore, the overall time complexity is O(N).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- We only need a few variables to store the maximum area found so far (`result`), the two pointers (`left`, `right`), and the calculated area for the current pair of lines.
- The space required for these variables does not depend on the size of the input array `height`.
- Therefore, the space complexity is O(1).
'''

# Test Cases
height1 = [1,8,6,2,5,4,8,3,7]
print(maxArea2(height1)) # Output: 49

height2 = [1,1]
print(maxArea2(height2)) # Output: 1

height3 = [4,3,2,1,4]
print(maxArea2(height3)) # Output: 16

height4 = [1,2,1]
print(maxArea2(height4)) # Output: 2

height5 = [2,3,4,5,18,17,6]
print(maxArea2(height5)) # Output: 17

height6 = [1,2,3,4,5,6,7,8,9]
print(maxArea2(height6)) # Output: 20

height7 = [9,8,7,6,5,4,3,2,1]
print(maxArea2(height7)) # Output: 20

height8 = [5,5,5,5,5]
print(maxArea2(height8)) # Output: 20

height9 = [1,100,100,1,1,100,1,1,100]
print(maxArea2(height9)) # Output: 700

height10 = [2,1]
print(maxArea2(height10)) # Output: 1