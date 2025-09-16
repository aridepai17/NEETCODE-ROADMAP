# FIRST UNIQUE CHARACTER IN A STRING

'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

def firstUniqChar(s):
    hashMap = {}
    
    for char in s:
        hashMap[char] = hashMap.get(char, 0) + 1
        
    for i in range(len(s)):
        if hashMap[s[i]] == 1:
            return i
        
    return -1

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The first loop iterates through the string to build a frequency map of characters. This takes O(N) time, as each character is processed once.
- The second loop iterates through the string again to find the first character with a frequency of 1 in the map. In the worst case, this also takes O(N) time (if the unique character is at the end or no unique character exists).
- The total time complexity is O(N) + O(N), which simplifies to O(N).

Space Complexity: O(1)
- The algorithm uses a hash map to store the frequency of each character.
- The maximum number of entries in the hash map is limited by the size of the character set (e.g., 26 for lowercase English letters).
- Since the character set is finite and its size does not depend on the length of the input string `s`, the space required for the hash map is constant.
- Therefore, the space complexity is O(1).
'''

# Test Cases
s1 = "leetcode"
print(firstUniqChar(s1)) # Output: 0

s2 = "loveleetcode"
print(firstUniqChar(s2)) # Output: 2

s3 = "aabb"
print(firstUniqChar(s3)) # Output: -1

s4 = "z"
print(firstUniqChar(s4)) # Output: 0

s5 = "dddccdbba"
print(firstUniqChar(s5)) # Output: 8

s6 = ""
print(firstUniqChar(s6)) # Output: -1

s7 = "statistics"
print(firstUniqChar(s7)) # Output: 3

s8 = "abacabad"
print(firstUniqChar(s8)) # Output: 4

s9 = "aabbccddeeffg"
print(firstUniqChar(s9)) # Output: 12

s10 = "zzzyyxxwwv"
print(firstUniqChar(s10)) # Output: 9