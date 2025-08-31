# IS SUBSEQUENCE

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

def isSubsequence(s, t):
    left = 0
    right = 0
    
    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
        right += 1
        
    return left == len(s)

# Test Cases
s1, t1 = "abc", "ahbgdc"
print(isSubsequence(s1, t1)) # Output: True

s2, t2 = "axc", "ahbgdc"
print(isSubsequence(s2, t2)) # Output: False

s3, t3 = "ace", "abcde"
print(isSubsequence(s3, t3)) # Output: True

s4, t4 = "aec", "abcde"
print(isSubsequence(s4, t4)) # Output: False

s5, t5 = "hello", "hello world"
print(isSubsequence(s5, t5)) # Output: True

s6, t6 = "world", "hello world"
print(isSubsequence(s6, t6)) # Output: True

s7, t7 = "python", "py th on"
print(isSubsequence(s7, t7)) # Output: True

s8, t8 = "a", "b"
print(isSubsequence(s8, t8)) # Output: False

s9, t9 = "a", "a"
print(isSubsequence(s9, t9)) # Output: True

s10, t10 = "", "anything"
print(isSubsequence(s10, t10)) # Output: True