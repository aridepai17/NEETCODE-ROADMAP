# ISOMORPHIC STRINGS

'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''

def isIsomorphic(s, t):
    freq1 = {}
    freq2 = {}
    
    for i in range(len(s)):
        char1, char2 = s[i], t[i]
        
        if char1 in freq1 and freq1[char1] != char2:
            return False
        
        if char2 in freq2 and freq2[char2] != char1:
            return False
        
        freq1[char1] = char2
        freq2[char2] = char1
        
    return True

'''
Time Complexity: O(n) where n is the length of the strings s and t.
We iterate through the strings once.
    
Space Complexity: O(k) where k is the number of unique characters in the strings.
In the worst case, this can be O(n) if all characters are unique.
We use two hashmaps to store the mappings between characters.
'''

# Test Cases
s1 = "egg", t1 = "add"
print(isIsomorphic(s1, t1)) # Output: True

s2, t2 = "foo", "bar"
print(isIsomorphic(s2, t2)) # Output: False

s3, t3 = "paper", "title"
print(isIsomorphic(s3, t3)) # Output: True

s4, t4 = "ab", "aa"
print(isIsomorphic(s4, t4)) # Output: False

s5, t5 = "a", "a"
print(isIsomorphic(s5, t5)) # Output: True

s6, t6 = "badc", "baba"
print(isIsomorphic(s6, t6)) # Output: False

s7, t7 = "aba", "baa"
print(isIsomorphic(s7, t7)) # Output: False

s8, t8 = "bbbaaaba", "aaabbbba"
print(isIsomorphic(s8, t8)) # Output: False

s9, t9 = "abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"
print(isIsomorphic(s9, t9)) # Output: True

s10, t10 = "", ""
print(isIsomorphic(s10, t10)) # Output: True