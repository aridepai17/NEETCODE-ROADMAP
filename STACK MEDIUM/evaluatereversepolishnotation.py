# EVALUATE REVERSE POLISH NOTATION

'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''

def evalRPN(tokens):
    stack = []
    for char in tokens:
        if char == '+':
            stack.append(stack.pop() + stack.pop())
        elif char == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif char == '*':
            stack.append(stack.pop() * stack.pop())
        elif char == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(char))
            
    return stack[0]

'''
Time Complexity: O(n)
- The algorithm iterates through the input list `tokens` of length `n` exactly once.
- For each token, it performs a constant number of operations: a few comparisons, one or two stack pops, one stack append, and one arithmetic operation. All these are O(1) operations.
- Therefore, the total time complexity is directly proportional to the number of tokens, resulting in O(n).

Space Complexity: O(n)
- The space complexity is determined by the `stack` used to store operands.
- In the worst-case scenario, the stack can hold a number of elements proportional to the total number of tokens.
- For example, in an expression like ["2", "3", "4", "5", "+", "*", "-"], all the numbers are pushed onto the stack before any operators are processed.
- The maximum size of the stack is roughly `n/2 + 1`, where `n` is the number of tokens.
- Therefore, the auxiliary space required by the algorithm is O(n).
'''

# Test Cases
tokens1 = ["2","1","+","3","*"]
print(evalRPN(tokens1)) # Output: 9

tokens2 = ["4","13","5","/","+"]
print(evalRPN(tokens2)) # Output: 6

tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens3)) # Output: 22

tokens4 = ["4","2","-"]
print(evalRPN(tokens4)) # Output: 2

tokens5 = ["10","5","/"]
print(evalRPN(tokens5)) # Output: 2

tokens6 = ["-1","1","*","-1","+"]
print(evalRPN(tokens6)) # Output: -2

tokens7 = ["5"]
print(evalRPN(tokens7)) # Output: 5

tokens8 = ["1","2","3","4","5","+","+","+","*"]
print(evalRPN(tokens8)) # Output: 14

tokens9 = ["3","11","+","5","-"]
print(evalRPN(tokens9)) # Output: 9

tokens10 = ["7","8","/"]
print(evalRPN(tokens10)) # Output: 0