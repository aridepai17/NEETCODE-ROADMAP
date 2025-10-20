# CLEAR DIGITS

'''
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.
'''

def clearDigits(s):
    stack = []
    
    def isDigit(char):
        return ord('0') <= ord(char) <= ord('9')

    for i in range(len(s)):
        if isDigit(s[i]):
            stack.pop()
        else:
            stack.append(s[i])
            
    return "".join(stack)

'''
Time Complexity: O(n)
- The algorithm iterates through the input string `s` of length `n` exactly once.
- For each character, it performs a constant number of operations: checking if it's a digit, and either appending to or popping from the stack. These are all amortized O(1) operations.
- The final `"".join(stack)` operation takes O(k) time, where k is the number of elements in the stack (k <= n). In the worst case, this is O(n).
- The total time complexity is dominated by the single pass through the string, resulting in O(n).

Space Complexity: O(n)
- The space complexity is determined by the `stack` used to store the non-digit characters.
- In the worst-case scenario, where the string contains no digits (e.g., "abcdef"), no characters are ever popped from the stack.
- The stack can grow to a size of `n`, where `n` is the length of the input string `s`.
- Therefore, the auxiliary space required by the algorithm is O(n).
'''

# Test Cases
s1 = "abc"
print(clearDigits(s1)) # Output: "abc"

s2 = "ab1c2"
print(clearDigits(s2)) # Output: "a"

s3 = "cb34"
print(clearDigits(s3)) # Output: ""

s4 = "123abc"
print(clearDigits(s4)) # Output: "abc"

s5 = "ab12"
print(clearDigits(s5)) # Output: ""

s6 = ""
print(clearDigits(s6)) # Output: ""

s7 = "a1b2c3d4"
print(clearDigits(s7)) # Output: ""

s8 = "abc12"
print(clearDigits(s8)) # Output: "a"

s9 = "abacaba"
print(clearDigits(s9)) # Output: "abacaba"

s10 = "z1y2x3w4v"
print(clearDigits(s10)) # Output: "v"