# VALIDATE STACK SEQUENCES

'''
Given two integer arrays pushed and popped each with distinct values, 
return true if this could have been the result of a sequence of push and pop operations 
on an initially empty stack, or false otherwise.
'''

def validateStackSequences(pushed, popped):
    stack = []
    i = 0
    
    for num in pushed:
        stack.append(num)
        while stack and i < len(popped) and popped[i] == stack[-1]:
            stack.pop()
            i += 1
            
    return not stack

'''
Time Complexity: O(n)
- Let `n` be the number of elements in the `pushed` and `popped` arrays.
- The algorithm iterates through the `pushed` array once.
- Each element is pushed onto the stack exactly once (n pushes).
- Each element is popped from the stack at most once (at most n pops).
- Since each element is pushed and popped at most once, the total number of operations is proportional to `n`.
- Therefore, the time complexity is O(n).

Space Complexity: O(n)
- The space complexity is determined by the auxiliary `stack`.
- In the worst-case scenario, all elements from the `pushed` array are pushed onto the stack before any pop operations can occur.
- For example, if `pushed = [1, 2, 3, 4, 5]` and `popped = [5, 4, 3, 2, 1]`, the stack will hold all `n` elements at its peak.
- Thus, the space required by the stack can be up to O(n).
'''

# Test Cases
pushed1 = [1,2,3,4,5]
popped1 = [4,5,3,2,1]
print(validateStackSequences(pushed1, popped1)) # Output: True

pushed2 = [1,2,3,4,5]
popped2 = [4,3,5,1,2]
print(validateStackSequences(pushed2, popped2)) # Output: False

pushed3 = [1,0]
popped3 = [1,0]
print(validateStackSequences(pushed3, popped3)) # Output: True

pushed4 = [2,1,0]
popped4 = [1,2,0]
print(validateStackSequences(pushed4, popped4)) # Output: False

pushed5 = []
popped5 = []
print(validateStackSequences(pushed5, popped5)) # Output: True

pushed6 = [1]
popped6 = [1]
print(validateStackSequences(pushed6, popped6)) # Output: True

pushed7 = [0,1,2]
popped7 = [0,2,1]
print(validateStackSequences(pushed7, popped7)) # Output: True

pushed8 = [1, 2, 3, 0]
popped8 = [2, 1, 3, 0]
print(validateStackSequences(pushed8, popped8)) # Output: True

pushed9 = [1, 2, 3, 4, 5]
popped9 = [1, 5, 4, 2, 3]
print(validateStackSequences(pushed9, popped9)) # Output: False

pushed10 = [4, 0, 1, 2, 3]
popped10 = [0, 1, 2, 3, 4]
print(validateStackSequences(pushed10, popped10)) # Output: True