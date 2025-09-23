# TWO SUM 2

'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
'''

def twoSum2(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1

'''
Time Complexity: O(N)
We use a two-pointer approach. The `left` pointer starts at the beginning of the array, and the `right` pointer starts at the end.
In each iteration of the while loop, we either increment `left` or decrement `right`.
In the worst-case scenario, the pointers will traverse the entire array once.
This means the number of operations is proportional to the number of elements in the array, N.
Thus, the time complexity is O(N).

Space Complexity: O(1)
The algorithm uses only a few variables to store the pointers (`left`, `right`) and the result.
The amount of extra space required does not scale with the size of the input array.
Therefore, 
'''

# Test Cases
numbers1 = [2,7,11,15], target1 = 9
print(twoSum2(numbers1, target1)) # Output: [1, 2]

numbers2 = [2,3,4], target2 = 6
print(twoSum2(numbers2, target2)) # Output: [1, 3]

numbers3 = [-1,0], target3 = -1
print(twoSum2(numbers3, target3)) # Output: [1, 2]

numbers4 = [5,25,75], target4 = 100
print(twoSum2(numbers4, target4)) # Output: [2, 3]

numbers5 = [1, 3, 4, 5, 7, 10, 11], target5 = 9
print(twoSum2(numbers5, target5)) # Output: [3, 4]

numbers6 = [3,3], target6 = 6
print(twoSum2(numbers6, target6)) # Output: [1, 2]

numbers7 = [3, 24, 50, 79, 88, 150, 345], target7 = 200
print(twoSum2(numbers7, target7)) # Output: [3, 6]

numbers8 = [0,0,3,4], target8 = 0
print(twoSum2(numbers8, target8)) # Output: [1, 2]

numbers9 = [-10, -8, -6, -2, -1], target9 = -8
print(twoSum2(numbers9, target9)) # Output: [3, 4]

numbers10 = [-3, 1, 2, 5, 8], target10 = 5
print(twoSum2(numbers10, target10)) # Output: [1, 5]