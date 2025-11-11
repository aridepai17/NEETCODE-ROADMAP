# PARSING A BOOLEAN EXPRESSION

'''
A boolean expression is an expression that evaluates to either true or false. 
It can be in one of the following shapes:
- 't' that evaluates to true.
- 'f' that evaluates to false.
- '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
- '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
- '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.
It is guaranteed that the given expression is valid and follows the given rules.
'''

def parseBoolExpression(expression):
    stack = []
    
    for char in expression:
        if char == ",":
            continue
        elif char != ")":
            stack.append(char)
        else:
            seen = set()
            while stack[-1] != "(":
                seen.add(stack.pop())
            stack.pop()
            operations = stack.pop()
            
            if operations == "!":
                result = "f" if "t" in seen else "t"
            elif operations == "&":
                result = "t" if f not in seen else "f"
            else:
                result = "t" if t in seen else "f"
                
            stack.append(result)
            
    return stack[-1] == "t"

'''
Time Complexity: O(n)
Let n be the length of the input expression string.
- We iterate through the expression once, processing each character. This takes O(n) time.
- For each closing parenthesis ')', we may pop multiple elements from the stack to process a sub-expression.
- However, each character in the expression can be pushed onto the stack at most once and popped at most once across all iterations.
- Therefore, the total number of stack operations (push and pop) is O(n).
- The set operations (adding elements to 'seen' and checking membership) are O(1) on average.
- The overall time complexity is O(n).

Space Complexity: O(n)
- We use a stack to store characters from the expression. In the worst case (e.g., deeply nested expressions), the stack can contain up to n characters.
- The 'seen' set is created for each sub-expression evaluation. In the worst case, it can store a constant number of elements ('t' and 'f'), so it doesn't significantly affect the space complexity.
- Therefore, the space complexity is O(n), dominated by the stack.
'''

# Test Cases
expression1 = "&(|(f))"
print(parseBoolExpression(expression1)) # Output: False

expression2 = "!(f)"
print(parseBoolExpression(expression2)) # Output: True

expression3 = "|(f,f,f,t)"
print(parseBoolExpression(expression3)) # Output: True

expression4 = "&(t,f)"
print(parseBoolExpression(expression4)) # Output: False

expression5 = "&(t,t,t)"
print(parseBoolExpression(expression5)) # Output: True

expression6 = "!(&(f,t))"
print(parseBoolExpression(expression6)) # Output: True

expression7 = "|(&(t,f,t),!(t))"
print(parseBoolExpression(expression7)) # Output: False

expression8 = "!(t)"
print(parseBoolExpression(expression8)) # Output: False

expression9 = "!(f)"
print(parseBoolExpression(expression9)) # Output: True

expression10 = "&(|(t,f),&(t,t))"
print(parseBoolExpression(expression12)) # Output: True