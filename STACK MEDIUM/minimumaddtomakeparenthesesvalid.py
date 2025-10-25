# MINIMUM ADD TO MAKE PARENTHESES VALID

'''
A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.
- You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
'''

def minAddToMakeValid(s):
    openCount = 0
    result = 0
    
    for char in s:
        if char == "(":
            openCount += 1
        else:
            openCount -= 1
            if openCount < 0:
                result += 1
                openCount = 0
                
    return result + openCount

'''
Time Complexity: O(N), where N is the length of the input string s.
- We iterate through the string s once from left to right.
- Inside the loop, we perform O(1) constant time operations (comparisons and arithmetic operations).
- Therefore, the total time complexity is directly proportional to the length of the string.

Space Complexity: O(1)
- We use a constant amount of extra space for variables like `openCount` and `result`.
- The space required does not grow with the size of the input string s.
- Thus, the space complexity is constant.
'''

# Test Cases
s1 = "())"
print(minAddToMakeValid(s1)) # Output: 1,

s2 = "((("
print(minAddToMakeValid(s2)) # Output: 3

s3 = "()"
print(minAddToMakeValid(s3)) # Output: 0

s4 = "()))(("
print(minAddToMakeValid(s4)) # Output: 4

s5 = ""
print(minAddToMakeValid(s5)) # Output: 0

s6 = ")))"
print(minAddToMakeValid(s6)) # Output: 3

s7 = "()()()"
print(minAddToMakeValid(s7)) # Output: 0

s8 = "(()())"
print(minAddToMakeValid(s8)) # Output: 0

s9 = "())(()"
print(minAddToMakeValid(s9)) # Output: 2

s10 = "((()))())"
print(minAddToMakeValid(s10)) # Output: 1