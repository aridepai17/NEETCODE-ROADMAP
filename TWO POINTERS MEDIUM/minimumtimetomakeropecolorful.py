# MINIMUM TIME TO MAKE ROPE COLORFUL

'''
Alice has n balloons arranged on a rope. 
You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
Alice wants the rope to be colorful. 
She does not want two consecutive balloons to be of the same color, so she asks Bob for help.
Bob can remove some balloons from the rope to make it colorful. 
You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
Return the minimum time Bob needs to make the rope colorful.
'''

def minCost(colors, neededTime):
    time = 0
    left = 0
    
    for right in range(1, len(colors)):
        if colors[left] == colors[right]:
            if neededTime[left] < neededTime[right]:
                time += neededTime[left]
                left = right
            else:
                time += neededTime[right]
        else:
            left = right
            
    return time

'''
Time Complexity: O(N)
- The algorithm uses a two-pointer approach (`left` and `right`) to iterate through the input arrays.
- The `right` pointer traverses the `colors` array from the second element to the end, making a single pass. The `left` pointer is updated based on the comparisons but does not cause additional loops.
- The `for` loop runs `N-1` times, where N is the number of balloons.
- Inside the loop, all operations (comparisons, additions, and assignments) take constant time, O(1).
- Since the work done is proportional to the number of elements, the overall time complexity is O(N).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- It only requires a few variables to store the total time (`time`), the left pointer (`left`), and the right pointer (`right` from the loop).
- The space needed for these variables does not depend on the size of the input arrays.
- No new data structures that scale with the input size are created.
- Therefore, the space complexity is O(1).
'''

# Test Cases
colors1 = "abaac", neededTime1 = [1,2,3,4,5]
print(minCost(colors1, neededTime1)) # Output: 3

colors2 = "abc", neededTime2 = [1,2,3]
print(minCost(colors2, neededTime2)) # Output: 0

colors3 = "aabaa", neededTime3 = [1,2,3,4,1]
print(minCost(colors3, neededTime3)) # Output: 2

colors4 = "aaaaa", neededTime4 = [1,2,3,4,5]
print(minCost(colors4, neededTime4)) # Output: 10

colors5 = "aaabbbabbbb", neededTime5 = [3,5,10,6,5,10,10,1,1,1]
print(minCost(colors5, neededTime5)) # Output: 22

colors6 = "", neededTime6 = []
print(minCost(colors6, neededTime6)) # Output: 0

colors7 = "a", neededTime7 = [100]
print(minCost(colors7, neededTime7)) # Output: 0

colors8 = "bbbaaa", neededTime8 = [4,9,3,8,8,9]
print(minCost(colors8, neededTime8)) # Output: 23

colors9 = "cddcd", neededTime9 = [1,2,1,4,3]
print(minCost(colors9, neededTime9)) # Output: 1

colors10 = "abacaba", neededTime10 = [1,2,1,2,1,2,1]
print(minCost(colors10, neededTime10)) # Output: 0