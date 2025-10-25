# DECODE STRING

'''
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.
'''

def decodeString(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            substring = ""
            while stack[-1] != "[":
                substring = stack.pop() + substring
            stack.pop()
            
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
                
            stack.append(int(k) * substring)
            
    return "".join(stack)

'''
Time Complexity: O(M), where M is the length of the decoded string.
- We iterate through the input string s of length N once.
- The dominant operations are string concatenations and multiplications (e.g., `int(k) * substring`).
- The total work done to build the final string is proportional to its length, M.
- For example, in a case like "10[a10[b]]", the work done is not just related to the input length but to the output length (1 + 10 * (1 + 10)) = 111.
- Thus, the complexity is bounded by the size of the output string.

Space Complexity: O(M), where M is the length of the decoded string.
- The space is used by the stack.
- The stack stores characters and intermediate decoded strings.
- In the worst-case scenario of nested structures, the total length of strings stored on the stack can be proportional to the length of the final decoded string.
- For example, for "a[b[c...[z]...]]", the stack would hold parts of the final string at each level of nesting. The sum of the lengths of these parts determines the space, which is bounded by M.
'''

# Test Cases
s1 = "3[a]2[bc]"
print(decodeString(s1)) # Output: "aaabcbc"

s2 = "3[a2[c]]"
print(decodeString(s2)) # Output: "accaccacc"

s3 = "2[abc]3[cd]ef"
print(decodeString(s3)) # Output: "abcabccdcdcdef"

s4 = "10[a]"
print(decodeString(s4)) # Output: "aaaaaaaaaa"

s5 = "leetcode"
print(decodeString(s5)) # Output: "leetcode"

s6 = ""
print(decodeString(s6)) # Output: ""

s7 = "1[a1[b1[c1[d]]]]"
print(decodeString(s7)) # Output: "abcd"

s8 = "2[a3[b]]"
print(decodeString(s8)) # Output: "abbbabbb"

s9 = "abc3[a]xyz"
print(decodeString(s9)) # Output: "abcaaaxyz"

s10 = "3[z]2[2[y]pq4[a]e]f"
print(decodeString(s10)) # Output: "zzzyypqaaaaeyypqaaaaef"