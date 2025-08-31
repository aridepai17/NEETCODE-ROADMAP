# APPEND CHARACTERS TO STRING TO MAKE SUBSEQUENCE 

'''
You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
'''

def appendCharacters(s, t):
    left = 0
    right = 0
    
    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            right += 1
        left += 1
        
    return len(t) - right

# Test Cases
s1, t1 = "coaching", "coding"
print(appendCharacters(s1, t1)) # Output: 4

s2, t2 = "abcde", "a"
print(appendCharacters(s2, t2)) # Output: 0

s3, t3 = "z", "abcde"
print(appendCharacters(s3, t3)) # Output: 5

s4, t4 = "hello", "world"
print(appendCharacters(s4, t4)) # Output: 5

s5, t5 = "python", "py"
print(appendCharacters(s5, t5)) # Output: 0

s6, t6 = "abc", "abc"
print(appendCharacters(s6, t6)) # Output: 0

s7, t7 = "xyz", "abc"
print(appendCharacters(s7, t7)) # Output: 3

s8, t8 = "programming", "gram"
print(appendCharacters(s8, t8)) # Output: 0

s9, t9 = "test", "testing"
print(appendCharacters(s9, t9)) # Output: 3

s10, t10 = "a", "a"
print(appendCharacters(s10, t10)) # Output: 0