# MAKE THE STRING GREAT

'''
Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
You can keep doing this until the string becomes good.
Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.
'''

def makeGood(s):
    stack = []

    for char in s:
        if stack and abs(ord(stack[-1] - ord(char))) == 32:
            stack.pop()
        else:
            stack.append(char)
            
    return "".join(stack)

'''
Time Complexity: O(n)
- The algorithm iterates through the input string `s` of length `n` exactly once.
- For each character, it performs a constant number of operations: checking the stack, accessing the last element, calculating the `ord` difference, and either pushing to or popping from the stack. These are all O(1) operations.
- After the loop, the `"".join(stack)` operation creates the final string. In the worst case, the stack can contain up to `n` characters, so this operation takes O(n) time.
- The total time complexity is dominated by the single pass through the string and the final join, resulting in O(n).

Space Complexity: O(n)
- The space complexity is determined by the `stack` used to store the characters of the "good" string.
- In the worst-case scenario, where no adjacent characters are a lower/upper case pair (e.g., "abcdef" or "abacaba"), no characters are ever popped from the stack.
- The stack can grow to a size of `n`, where `n` is the length of the input string `s`.
- Therefore, the auxiliary space required by the algorithm is O(n).
'''

# Test Cases
s1 = "leEeetcode"
print(makeGood(s1)) # Output: "leetcode"

s2 = "abBAcC"
print(makeGood(s2)) # Output: ""

s3 = "s"
print(makeGood(s3)) # Output: "s"

s4 = "Pp"
print(makeGood(s4)) # Output: ""

s5 = "mC"
print(makeGood(s5)) # Output: "mC"

s6 = ""
print(makeGood(s6)) # Output: ""

s7 = "RLlr"
print(makeGood(s7)) # Output: "RLlr"

s8 = "aAbBcD"
print(makeGood(s8)) # Output: "cD"

s9 = "abCDef"
print(makeGood(s9)) # Output: "abCDef"

s10 = "abBAcC"
print(makeGood(s10)) # Output: ""