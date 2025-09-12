# HEIGHT CHECKER 

'''
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. 
Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
You are given an integer array heights representing the current order that the students are standing in. 
Each heights[i] is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i].
'''

# Solution 1: Using Built In Sort
def heightChecker1(heights):
    expected = sorted(heights)
    count = 0
    
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    
    return count

'''
Time Complexity: O(N log N)
Let N be the number of students (the length of the `heights` array).
- `sorted(heights)`: The sorting operation is the most time-consuming part of the algorithm. Python's built-in `sorted()` function uses Timsort, which has a time complexity of O(N log N) in the average and worst cases.
- The `for` loop iterates through the `heights` array once, which takes O(N) time.
- The comparison `heights[i] != expected[i]` inside the loop is an O(1) operation.
- The overall time complexity is dominated by the sorting step, making it O(N log N).

Space Complexity: O(N)
- `expected = sorted(heights)`: The `sorted()` function creates a new list to store the sorted version of `heights`. This new list, `expected`, requires O(N) space, where N is the length of the input array.
- The other variables, like `count` and the loop index `i`, use a constant amount of space, O(1).
- Therefore, the space complexity is O(N) due to the storage needed for the sorted copy of the array.
'''

# Solution 2: Using Bucket Sort
def heightChecker2(heights):
    count = [0] * 101
    
    for height in heights:
        count[height] += 1
        
    expected = []
    
    for height in range(1, 101):
        expected.extend([height] * count[height])
        
    result = 0
    
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            result += 1
            
    return result

'''
Time Complexity: O(N)
Let N be the number of students (the length of the `heights` array).
- The first loop iterates through the `heights` array to populate the `count` array. This takes O(N) time.
- The second loop iterates from 1 to 100. This is a constant number of iterations. Inside the loop, we build the `expected` array. The total number of elements added to `expected` across all iterations is N. Thus, the total time for this step is proportional to N, making it O(N).
- The third loop iterates through the `heights` array again to compare it with the `expected` array, which takes O(N) time.
- The overall time complexity is O(N + N + N), which simplifies to O(N). This is more efficient than the O(N log N) approach because the range of heights is limited (1 to 100), allowing for a linear time sorting algorithm like counting sort.

Space Complexity: O(N)
- `count = [0] * 101`: This array has a fixed size of 101, which is independent of the input size N. Therefore, it uses constant space, O(1).
- `expected = []`: This list is created to store the sorted version of the heights. It will contain N elements, so it requires O(N) space.
- The other variables use constant space.
- The dominant factor is the space required for the `expected` list, making the overall space complexity O(N).
'''

# Test Cases
heights1 = [1,1,4,2,1,3]
print(heightChecker1(heights1)) # Output: 3

heights2 = [5,1,2,3,4]
print(heightChecker1(heights2)) # Output: 5

heights3 = [1,2,3,4,5]
print(heightChecker1(heights3)) # Output: 0

heights4 = [1]
print(heightChecker1(heights4)) # Output: 0

heights5 = []
print(heightChecker1(heights5)) # Output: 0

heights6 = [10,6,6,10,10,9,8,8,3,3,8,2,1,5,1,9,5,2,7,4,7,7]
print(heightChecker1(heights6)) # Output: 22

heights7 = [2,1,2,1,1,2,2,1]
print(heightChecker1(heights7)) # Output: 4

heights8 = [3,3,3,3,3]
print(heightChecker1(heights8)) # Output: 0

heights9 = [5,4,3,2,1]
print(heightChecker1(heights9)) # Output: 5

heights10 = [1,5,2,4,3]
print(heightChecker1(heights10)) # Output: 4