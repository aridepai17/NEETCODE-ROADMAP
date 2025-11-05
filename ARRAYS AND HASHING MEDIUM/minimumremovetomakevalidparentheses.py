# MINIMUM REMOVE TO MAKE VALID PARENTHESES

'''
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.
'''

def minimumRemove(s):
    result = []
    count = 0
    
    for char in s:
        if char == "(":
            result.append(char)
            count += 1
        elif char == ")" and count > 0:
            result.append(char)
            count -= 1
        elif char != ")":
            result.append(char)
            
    filtered = []
    for char in result[::-1]:
        if char == "(" and count > 0:
            count -= 1
        else:
            filtered.append(char)
            
    return "".join(filtered[::-1])

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The first loop iterates through each character in `s` once, performing constant-time operations (append, increment/decrement), which takes O(N).
- The second loop iterates through the `result` list in reverse, which has at most N elements, performing constant-time operations, which takes O(N).
- The `join` operation on the `filtered` list takes O(N) time.
- Therefore, the overall time complexity is O(N).

Space Complexity: O(N)
- The `result` list stores characters from the input string and can contain up to N elements in the worst case.
- The `filtered` list also stores characters and can contain up to N elements in the worst case.
- Both lists together require O(N) space.
- The final string returned by `join` also takes O(N) space.
- Therefore, the overall space complexity is O(N).
'''

# Test Cases
s1 = "lee(t(c)o)de)"
print(minimumRemove(s1)) # Output: "lee(t(c)o)de"

s2 = "a)b(c)d"
print(minimumRemove(s2)) # Output: "ab(c)d"

s3 = "))(("
print(minimumRemove(s3)) # Output: ""

s4 = "(a(b(c)d)"
print(minimumRemove(s4)) # Output: "a(b(c)d)"

s5 = "((((("
print(minimumRemove(s5)) # Output: ""

s6 = ")))))"
print(minimumRemove(s6)) # Output: ""

s7 = "()()"
print(minimumRemove(s7)) # Output: "()()"

s8 = "a(b)c(d)e"
print(minimumRemove(s8)) # Output: "a(b)c(d)e"

s9 = "(a(b(c(d(e)))))"
print(minimumRemove(s9)) # Output: "(a(b(c(d(e)))))"

s10 = "()()((("
print(minimumRemove(s10)) # Output: "()()"