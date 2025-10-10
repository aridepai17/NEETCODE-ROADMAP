# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

# Given a string s, find the length of the longest substring without duplicate characters.

def lengthofLongestSubstring(s):
    charSet = set()
    left = 0
    longest = 0
    
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        
        longest = max(longest, right - left + 1)
        
    return longest

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach with two pointers, `left` and `right`.
Each character in the input string `s` is visited at most twice (once by the `right` pointer and once by the `left` pointer).
The operations inside the loops (set addition, removal, and checking for existence) take, on average, O(1) time.
Therefore, the overall time complexity is linear, O(n), where 'n' is the length of the string.

Space Complexity: O(min(n, m))
The space complexity is determined by the size of the `charSet`.
In the worst-case scenario, the set can store up to `n` unique characters if all characters in the string are distinct.
However, the size of the set is also limited by the size of the character set (e.g., ASCII, Unicode).
Let 'm' be the size of the character set. The space required is O(min(n, m)).
If the character set is fixed (like 26 lowercase English letters or 128 ASCII characters), the space complexity can be considered O(1).
'''

# Test Cases
s1 = "abcabcbb"
print(lengthofLongestSubstring(s1)) # Output: 3

s2 = "bbbbb"
print(lengthofLongestSubstring(s2)) # Output: 1

s3 = "pwwkew"
print(lengthofLongestSubstring(s3)) # Output: 3

s4 = ""
print(lengthofLongestSubstring(s4)) # Output: 0

s5 = "a"
print(lengthofLongestSubstring(s5)) # Output: 1

s6 = "dvdf"
print(lengthofLongestSubstring(s6)) # Output: 3

s7 = " "
print(lengthofLongestSubstring(s7)) # Output: 1

s8 = "anviaj"
print(lengthofLongestSubstring(s8)) # Output: 5

s9 = "tmmzuxt"
print(lengthofLongestSubstring(s9)) # Output: 5

s10 = "abacabad"
print(lengthofLongestSubstring(s10)) # Output: 3