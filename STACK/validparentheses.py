# VALID PARENTHESIS

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
'''

def isValid(s):
    stack = []
    hashMap = {')' : '(', ']' : '[', '}' : '{'}
    
    for char in s:
        if char in hashMap:
            if stack and stack[-1] == hashMap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
            
    return not stack

'''
Time Complexity: O(n)
We iterate through the string of length n once. The operations inside the loop (pushing to stack, popping from stack, checking hash map) are all O(1).

Space Complexity: O(n)
In the worst case, the string contains only opening brackets, and we would push all n characters onto the stack. For example, s = "(((((". The space used by the hash map is constant.
'''

# Test Cases
s1 = "()"
print(isValid(s1)) # Output: True

s2 = "()[]{}"
print(isValid(s2)) # Output: True

s3 = "(]"
print(isValid(s3)) # Output: False

s4 = "([)]"
print(isValid(s4)) # Output: False

s5 = "{[]}"
print(isValid(s5)) # Output: True

s6 = ""
print(isValid(s6)) # Output: True

s7 = "["
print(isValid(s7)) # Output: False

s8 = "]]"
print(isValid(s8)) # Output: False

s9 = "((()))"
print(isValid(s9)) # Output: True

s10 = "{[()]}"
print(isValid(s10)) # Output: True