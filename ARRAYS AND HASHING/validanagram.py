# VALID ANAGRAM

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
using all the original letters exactly once.
'''

def isAnagram(s, t):
    freq1 = {}
    freq2 = {}
    
    for char in s:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in t:
        freq2[char] = freq2.get(char, 0) + 1
        
    return freq1 == freq2

# Test Cases
s1, t1 = "anagram", "nagaram"
print(isAnagram(s1, t1)) # Output: True

s2, t2 = "rat", "car"
print(isAnagram(s2, t2)) # Output: False

s3, t3 = "listen", "silent"
print(isAnagram(s3, t3)) # Output: True

s4, t4 = "hello", "world"
print(isAnagram(s4, t4)) # Output: False

s5, t5 = "a", "a"
print(isAnagram(s5, t5)) # Output: True

s6, t6 = "a", "b"
print(isAnagram(s6, t6)) # Output: False

s7, t7 = "abc", "cba"
print(isAnagram(s7, t7)) # Output: True

s8, t8 = "debit card", "bad credit"
print(isAnagram(s8, t8)) # Output: True

s9, t9 = "python", "typhon"
print(isAnagram(s9, t9)) # Output: True

s10, t10 = "test", "tset"
print(isAnagram(s10, t10)) # Output: True