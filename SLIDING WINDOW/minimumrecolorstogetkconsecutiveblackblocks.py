# MINIMUM RECOLORS TO GET K CONSECUTIVE BLACK BLOCKS

'''
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. 
The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
'''

def minimumRecolors(blocks, k):
    left = 0
    recolor = 0
    result = k
    
    for right in range(len(blocks)):
        if blocks[right] == "W":
            recolor += 1
        if right - left + 1 == k:
            result = min(result, recolor)
            if blocks[left] == "W":
                recolor -= 1
            left += 1
            
    return result

'''
Time Complexity: O(n)
The code iterates through the `blocks` string once using a single for loop. 
The operations inside the loop are all constant time. 
Therefore, the time complexity is linear with respect to the length of the input string `n`.

Space Complexity: O(1)
The algorithm uses a fixed number of variables (`left`, `recolor`, `result`, `right`) to keep track of the sliding window and the minimum recolors. 
The space required does not grow with the size of the input string, so the space complexity is constant.
'''

# Test Cases
blocks1 = "WBBWWBBWBW", k1 = 7
print(minimumRecolors(blocks1, k1)) # Output: 3

blocks2 = "BBBBBBB", k2 = 3
print(minimumRecolors(blocks2, k2)) # Output: 0

blocks3 = "WWWW", k3 = 4
print(minimumRecolors(blocks3, k3)) # Output: 4

blocks4 = "WBWBW", k4 = 2
print(minimumRecolors(blocks4, k4)) # Output: 1

blocks5 = "BWWWBB", k5 = 4
print(minimumRecolors(blocks5, k5)) # Output: 2

blocks6 = "WWWWBBWWWW", k6 = 4
print(minimumRecolors(blocks6, k6)) # Output: 2

blocks7 = "WWWW", k7 = 1
print(minimumRecolors(blocks7, k7)) # Output: 1

blocks8 = "BWBWBW", k8 = 1
print(minimumRecolors(blocks8, k8)) # Output: 0

blocks9 = "WBBWWWWBBWBB", k9 = 5
print(minimumRecolors(blocks9, k9)) # Output: 1

blocks10 = "B", k10 = 1
print(minimumRecolors(blocks10, k10)) # Output: 0