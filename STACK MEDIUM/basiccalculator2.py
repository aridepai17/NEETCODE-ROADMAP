# BASIC CALCULATOR 2

'''
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''

# Solution 1: Using Stack
def calculate(s):
    stack = []
    currentNumber = 0
    operator = "+"
    
    for i in range(len(s)):
        char = s[i]
        if char.isdigit():
            currentNumber = currentNumber * 10 + int(char)
            
        if not char.isdigit() and not char.isspace() or i == len(s) - 1:
            if operator == "+":
                stack.append(currentNumber)
            elif operator == "-":
                stack.append(-currentNumber)
            elif operator == "*":
                stack.append(stack.pop() * currentNumber)
            else:
                stack.append(int(stack.pop() / currentNumber))
                
            operator = char 
            currentNumber = 0
            
    return sum(stack)

'''
Time Complexity: O(N), where N is the length of the input string `s`.
- We iterate through the input string `s` once, which takes O(N) time.
- Inside the loop, we perform constant time operations: checking if a character is a digit, updating `currentNumber`, and performing stack operations (`append`, `pop`), which are amortized O(1).
- Multiplication and division are handled immediately by popping the last element, calculating, and pushing the result back. Addition and subtraction simply push the number (or its negative) onto the stack.
- After the loop, `sum(stack)` is called. In the worst case (e.g., an expression with only '+' and '-' operators), the stack can contain up to O(N) numbers. Summing them up takes O(N) time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(N)
- We use a `stack` to store numbers. In the worst-case scenario, such as an expression with only additions and subtractions (e.g., "1+2+3+4"), the stack will store every number. The number of operands can be proportional to the length of the string N.
- Thus, the space required for the stack is O(N).
- Other variables like `currentNumber` and `operator` use constant O(1) space.
- The overall space complexity is dominated by the stack, making it O(N).
'''

# Solution 2: No Extra Space. Two Variables Only.
def calculate(s):
    currentNumber = 0
    lastNumber = 0
    result = 0
    operation = "+"
    
    for i in range(len(s)):
        char = s[i]
        if char.isdigit():
            currentNumber = currentNumber * 10 + int(char)
            
        if not char.isdigit() and not char.isspace() or i == len(s) - 1:
            if operation == "+":
                result += lastNumber
                lastNumber = currentNumber
            elif operation == "-":
                result += lastNumber
                lastNumber = -currentNumber
            elif operation == "*":
                lastNumber *= currentNumber
            else:
                lastNumber = int(lastNumber / currentNumber)
                
            operation = char
            currentNumber = 0
            
    result += lastNumber
    return result

'''
Time Complexity: O(N), where N is the length of the input string `s`.
- We iterate through the input string `s` once from beginning to end. This takes O(N) time.
- Inside the loop, we perform constant time operations: checking if a character is a digit, updating `currentNumber`, and performing arithmetic operations.
- All the variables used (`currentNumber`, `lastNumber`, `result`, `operation`) are updated in constant time.
- Thus, the overall time complexity is linear with respect to the length of the input string.

Space Complexity: O(1)
- This solution uses a constant amount of extra space.
- We only use a few variables (`currentNumber`, `lastNumber`, `result`, `operation`) to keep track of the state of the calculation.
- The space required by these variables does not depend on the length of the input string `s`.
- Therefore, the space complexity is O(1).
'''

# Test Cases
s1 = "3+2*2"
print(calculate(s1)) # Output: 7

s2 = " 3/2 "
print(calculate(s2)) # Output: 1

s3 = " 3+5 / 2 "
print(calculate(s3)) # Output: 5

s4 = "1-1+1"
print(calculate(s4)) # Output: 1

s5 = "2*3-4"
print(calculate(s5)) # Output: 2

s6 = "14-3*4"
print(calculate(s6)) # Output: 2

s7 = "1*2-3/4+5*6-7*8+9/10"
print(calculate(s7)) # Output: -24

s8 = "0"
print(calculate(s8)) # Output: 0

s9 = "1337"
print(calculate(s9)) # Output: 1337

s10 = "0-2147483647"
print(calculate(s10)) # Output: -2147483647