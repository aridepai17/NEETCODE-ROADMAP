# BASEBALL GAME

'''
You are keeping the scores for a baseball game with strange rules. 
At the beginning of the game, you start with an empty record.
You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
'''

def calcPoints(ops):
    stack = []
    
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(stack[-1] * 2)
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))
            
    return sum(stack)

'''
Time Complexity: O(n)
- The algorithm iterates through the input list `ops` once, where `n` is the number of operations.
- Inside the loop, each operation (`append`, `pop`, accessing the last elements) takes constant time, O(1), on average.
- After the loop, the `sum()` function is called on the `stack`. In the worst case, the stack can contain up to `n` elements. Summing these elements takes O(n) time.
- The total time complexity is the sum of the loop's time and the sum function's time, which is O(n) + O(n) = O(n).

Space Complexity: O(n)
- The primary data structure used is the `stack` to store the scores.
- In the worst-case scenario, where most operations add elements to the stack (integers, '+', 'D'), the size of the stack can grow to be proportional to the number of operations, `n`.
- Therefore, the space required by the algorithm is O(n).
'''

# Test Cases
ops1 = ["5","2","C","D","+"]
print(calcPoints(ops1)) # Output: 30

ops2 = ["5","-2","4","C","D","9","+","+"]
print(calcPoints(ops2)) # Output: 27

ops3 = ["1","C"]
print(calcPoints(ops3)) # Output: 0

ops4 = ["1"]
print(calcPoints(ops4)) # Output: 1

ops5 = []
print(calcPoints(ops5)) # Output: 0

ops6 = ["10", "20", "C", "30", "+", "C"]
print(calcPoints(ops6)) # Output: 40

ops7 = ["1", "D", "D", "D"]
print(calcPoints(ops7)) # Output: 15

ops8 = ["6", "D", "9", "+", "C", "10", "D", "+"]
print(calcPoints(ops8)) # Output: 87

ops9 = ["10", "20", "30", "40", "50"]
print(calcPoints(ops9)) # Output: 150

ops10 = ["-10", "D", "-5", "+", "C"]
print(calcPoints(ops10)) # Output: -35