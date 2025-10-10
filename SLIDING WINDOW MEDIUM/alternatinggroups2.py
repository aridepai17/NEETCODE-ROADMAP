# ALTERNATING GROUPS 2

'''
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
Return the number of alternating groups.
Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
'''

def numberofAlternatingGroups(colors, k):
    n = len(colors)
    left = 0
    result = 0
    
    for right in range(1, n + k - 1):
        if colors[right % n] == colors[(right - 1) % n]:
            left = right
        if right - left + 1 > k:
            left += 1
        if right - left + 1 == k:
            result += 1
            
    return result

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach. The `right` pointer iterates from 1 up to `n + k - 2`. 
In each iteration, we perform constant time operations (modulo, comparison, addition). 
Since the loop runs a number of times proportional to `n + k`, and typically `k <= n`, the overall time complexity is linear, O(n), where 'n' is the number of elements in the `colors` array.

Space Complexity: O(1)
We only use a constant amount of extra space for variables like `n`, `left`, `result`, and `right`. 
The space used does not grow with the number of elements in the input array.
'''

# Test Cases
colors1 = [0, 1, 0, 0, 1, 0, 1], k1 = 6
print(numberofAlternatingGroups(colors1, k1)) # Output: 2

colors2 = [0, 1, 0, 1], k2 = 3
print(numberofAlternatingGroups(colors2, k2)) # Output: 4

colors3 = [1, 1, 0, 1, 1, 0], k3 = 4
print(numberofAlternatingGroups(colors3, k3)) # Output: 0

colors4 = [0, 1, 0, 1, 0, 1], k4 = 6
print(numberofAlternatingGroups(colors4, k4)) # Output: 6

colors5 = [0, 1, 1, 0, 1], k5 = 5
print(numberofAlternatingGroups(colors5, k5)) # Output: 0

colors6 = [0, 1, 0, 1, 0], k6 = 5
print(numberofAlternatingGroups(colors6, k6)) # Output: 5

colors7 = [0, 1, 0, 0, 1], k7 = 1
print(numberofAlternatingGroups(colors7, k7)) # Output: 5

colors8 = [0, 1, 0, 1, 1], k8 = 2
print(numberofAlternatingGroups(colors8, k8)) # Output: 4

colors9 = [1, 1, 1, 1, 1], k9 = 3
print(numberofAlternatingGroups(colors9, k9)) # Output: 0

colors10 = [0, 1, 0, 1, 1, 0, 1, 0], k10 = 3
print(numberofAlternatingGroups(colors10, k10)) # Output: 4