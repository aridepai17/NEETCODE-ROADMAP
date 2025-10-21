# REMOVING STARS FROM A STRING

'''
You are given a string s, which contains stars *.
In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.
Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
'''

def removeStars(s):
    stack = []
    
    for char in s:
        if char == '*':
            stack.pop()
        else:
            stack.append(char)
            
    return "".join(stack)

'''
Time Complexity: O(n)
- The algorithm iterates through the input string `s` of length `n` exactly once.
- For each character, it performs a constant number of operations: a comparison, and either an append or a pop from the stack. These are amortized O(1) operations.
- The final `"".join(stack)` operation takes O(k) time, where k is the number of elements remaining in the stack (k <= n). In the worst case, this is O(n).
- Therefore, the total time complexity is dominated by the single pass through the string, resulting in O(n).

Space Complexity: O(n)
- The space complexity is determined by the `stack` used to store the non-star characters.
- In the worst-case scenario, where the string contains no stars (e.g., "abcdef"), no characters are ever popped from the stack.
- The stack can grow to a size of `n`, where `n` is the length of the input string `s`.
- Therefore, the auxiliary space required by the algorithm is O(n).
'''

# Test Cases
s1 = "leet**cod*e"
print(removeStars(s1)) # Output: "lecoe"

s2 = "erase*****"
print(removeStars(s2)) # Output: ""

s3 = "abc*de*f"
print(removeStars(s3)) # Output: "abdf"

s4 = "a*b*c*d*e*"
print(removeStars(s4)) # Output: ""

s5 = "abcdef"
print(removeStars(s5)) # Output: "abcdef"

s6 = ""
print(removeStars(s6)) # Output: ""

s7 = "ab**c"
print(removeStars(s7)) # Output: "c"

s8 = "therainin*spain*"
print(removeStars(s8)) # Output: "therainispai"

s9 = "a*b*cde**f"
print(removeStars(s9)) # Output: "cf"

s10 = "z*z*z*z*"
print(removeStars(s10)) # Output: ""