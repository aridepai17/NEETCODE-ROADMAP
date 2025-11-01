# MINIMUM NUMBER OF OPERATIONS TO MOVE ALL BALLS TO EACH BOX

'''
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. 
Note that after doing so, there may be more than one ball in some boxes.
Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
Each answer[i] is calculated considering the initial state of the boxes.
'''

def minOperations(boxes):
    result = [0] * len(boxes)
    balls = 0
    moves = 0
    
    for i in range(len(boxes)):
        result[i] = balls + moves
        moves += balls
        balls += int(boxes[i])
        
    balls = 0
    moves = 0
    
    for i in range(len(boxes) - 1, -1, -1):
        result[i] += balls + moves
        moves += balls
        balls += int(boxes[i])
        
    return result

'''
Time Complexity: O(N)
- Let N be the length of the input string `boxes`.
- The algorithm consists of two passes through the array: one forward and one backward.
- Each pass is O(N). Therefore, the total time complexity is O(N).

Space Complexity: O(N)
- The algorithm uses an auxiliary list `result` of size N.
- Other variables (`balls`, `moves`, `i`) require constant space.
- The total space complexity is O(N).
'''

# Test Cases
boxes1 = "110"


boxes2 = "001011"
print(minOperations(boxes2)) # Output: [11,8,5,4,3,4]

boxes3 = "000"
print(minOperations(boxes3)) # Output: [0,0,0]

boxes4 = "100"
print(minOperations(boxes4)) # Output: [0,1,2]

boxes5 = "010"
print(minOperations(boxes5)) # Output: [1,0,1]

boxes6 = "111"
print(minOperations(boxes6)) # Output: [3,2,3]

boxes7 = "10101"
print(minOperations(boxes7)) # Output: [6,5,4,5,6]

boxes8 = "00001"
print(minOperations(boxes8)) # Output: [4,3,2,1,0]

boxes9 = "1"
print(minOperations(boxes9)) # Output: [0]

boxes10 = "10000001"
print(minOperations(boxes10)) # Output: [6,5,4,3,2,1,1,6]