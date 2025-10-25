# REVERSE SUBSTRINGS BETWEEN EACH PAIR OF PARENTHESES

'''
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
'''

# Solution 1: Using Stack and Quadratic Time Complexity
def reverseParentheses(s):
    stack = []
    
    for char in s:
        if char == ")":
            portion = []
            while stack[-1] != "(":
                portion.append(stack.pop())
            stack.pop()
            stack.extend(portion)
        else:
            stack.append(char)
            
    return "".join(stack)

'''
Time Complexity: O(N^2), where N is the length of the input string `s`.
- We iterate through the string once, which is O(N).
- However, when we encounter a closing parenthesis ')', we pop elements from the stack, reverse them by appending to a temporary list, and then extend the stack with the reversed portion.
- A character might be part of multiple such reversal operations if it's inside nested parentheses.
- In the worst-case scenario, like s = "((...))" with deep nesting, some characters might be processed (popped and pushed) multiple times.
- For a string of length N, the number of reversals a character undergoes is proportional to its nesting depth. The maximum depth can be O(N), and the length of the substring to reverse can also be O(N).
- This leads to a total time complexity of O(N^2).

Space Complexity: O(N)
- We use a stack to store the characters of the processed string.
- In the worst case, the stack can hold all the characters of the input string (e.g., if there are no closing parentheses or they appear at the very end).
- The size of the stack is therefore proportional to the length of the input string, making the space complexity O(N).
'''


# Solution 2: Using Stack and Linear Time Complexity
def reverseParentheses(s):
    pair = {}
    stack = []
    
    index = 0
    for char in s:
        if char == "(":
            stack.append(index)
        elif char == ")":
            closing = stack.pop()
            pair[index] = closing
            pair[closing] = index
        index += 1
        
    i = 0
    direction = 1
    result = []
    
    while i >= 0 and i < len(s):
        char = s[i]
        if char == "(" or char == ")":
            i = pair[i]
            direction *= -1
        else:
            result.append(char)
            
        i += direction
        
    return "".join(result)

'''
Time Complexity: O(N), where N is the length of the input string `s`.
- The first loop iterates through the string once to find all matching pairs of parentheses. This takes O(N) time. We use a stack to keep track of the indices of open parentheses, and a dictionary `pair` to store the mapping between matching parentheses indices.
- The second loop also iterates through the string. The pointer `i` moves through the string, and although it jumps when it encounters a parenthesis, each character index is visited exactly once. This traversal builds the final result string. This part also takes O(N) time.
- Since the two loops are sequential, the total time complexity is O(N).

Space Complexity: O(N)
- We use a dictionary `pair` to store the indices of matching parentheses. In the worst case, this can store up to N entries (for a string with N/2 pairs). This is O(N) space.
- We use a `stack` to help build the `pair` map. The maximum size of the stack is determined by the maximum nesting depth of parentheses, which can be up to N/2. This is O(N) space.
- We use a `result` list to build the output string. This can store up to N characters. This is also O(N) space.
- Therefore, the total space complexity is O(N).
'''

# Test Cases
s1 = "(abcd)"
print(reverseParentheses(s1)) # Output: "dcba

s2 = "(u(love)i)"
print(reverseParentheses(s2)) # Output: "iloveu"

s3 = "(ed(et(oc))el)"
print(reverseParentheses(s3)) # Output: "leetcode"

s4 = "a(bc)de"
print(reverseParentheses(s4)) # Output: "acbde"

s5 = "ta()usw((((a))))"
print(reverseParentheses(s5)) # Output: "tauswa"

s6 = "a(bc(de)f)g"
print(reverseParentheses(s6)) # Output: "afdecbg"

s7 = "hello"
print(reverseParentheses(s7)) # Output: "hello"

s8 = ""
print(reverseParentheses(s8)) # Output: ""

s9 = "(abc)d(efg)"
print(reverseParentheses(s9)) # Output: "cbadgfe"

s10 = "((eqk((h))))"
print(reverseParentheses(s10)) # Output: "qekh"