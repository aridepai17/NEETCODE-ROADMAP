# MINIMUM STRING LENGTH AFTER REMOVING SUBSTRINGS

'''
You are given a string s consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.
Return the minimum possible length of the resulting string that you can obtain.
Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.
'''

def minimumLength(s):
    stack = []
    for char in s:
        if stack and (stack[-1] == "A" and char == "B") or (stack[-1] == "C" and char == "D"):
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack)

'''
Time Complexity: O(n)
- The algorithm iterates through the input string `s` of length `n` exactly once.
- For each character, it performs a constant number of operations: checking if the stack is not empty, accessing the last element of the stack, and either pushing to or popping from the stack. These are all O(1) operations.
- The total time complexity is dominated by the single pass through the string, resulting in O(n).

Space Complexity: O(n)
- The space complexity is determined by the `stack` used to store the characters.
- In the worst-case scenario, where no "AB" or "CD" substrings are formed (e.g., "ACBDACBD"), no characters are ever popped from the stack.
- The stack can grow to a size of `n`, where `n` is the length of the input string `s`.
- Therefore, the auxiliary space required by the algorithm is O(n).
'''

# Test Cases
s1 = "ABFCACDB"
print(minimumLength(s1)) # Output: 2

s2 = "CABD"
print(minimumLength(s2)) # Output: 0

s3 = "ACBD"
print(minimumLength(s3)) # Output: 4

s4 = "CACDB"
print(minimumLength(s4)) # Output: 1

s5 = ""
print(minimumLength(s5)) # Output: 0

s6 = "AABABBA"
print(minimumLength(s6)) # Output: 3

s7 = "CCDD"
print(minimumLength(s7)) # Output: 0

s8 = "ADBC"
print(minimumLength(s8)) # Output: 4

s9 = "ABACDCDABABCD"
print(minimumLength(s9)) # Output: 1

s10 = "ACCABD"
print(minimumLength(s10)) # Output: 2