# UNIQUE LENGTH 3 PALINDROMIC SUBSEQUENCES

'''
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
'''

def countPalindromicSubsequence(s):
    result = set()
    left = set()
    right = {}
    
    for char in s:
        right[char] = right.get(char, 0) + 1
        
    for i in range(len(s)):
        right[s[i]] -= 1
        if right[s[i]] == 0:
            right.pop(s[i])
            
        for char in left:
            if char in right:
                result.add(char + s[i] + char)
                
        left.add(s[i])
        
    return len(result)

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- We iterate through the string three times:
  1. First loop to populate the `right` hash map: O(N)
  2. Second loop to process each character and find palindromic subsequences: O(N)
     - Inside this loop, we iterate through the `left` set, which contains at most 26 unique characters (assuming lowercase English letters).
     - Since the size of `left` is bounded by a constant (26), the inner loop is O(1).
  3. Operations like hash map lookups, set additions, and set operations are O(1) on average.
- Therefore, the overall time complexity is O(N).

Space Complexity: O(1) or O(26) = O(1)
- The `result` set stores unique palindromic subsequences. Each palindrome is of length 3 with the first and last characters being the same.
  - There are at most 26 choices for the outer character and 26 choices for the middle character, giving at most 26 * 26 = 676 unique palindromes.
  - This is a constant bound, so `result` uses O(1) space.
- The `left` set stores at most 26 unique characters: O(1) space.
- The `right` hash map stores at most 26 unique characters with their counts: O(1) space.
- Therefore, the overall space complexity is O(1).
'''

# Test Cases
s1 = "aabca"
print(countPalindromicSubsequence(s1)) # Output: 3

s2 = "adc"
print(countPalindromicSubsequence(s2)) # Output: 0

s3 = "bbcbaba"
print(countPalindromicSubsequence(s3)) # Output: 4

s4 = "a"
print(countPalindromicSubsequence(s4)) # Output: 0

s5 = "aba"
print(countPalindromicSubsequence(s5)) # Output: 1

s6 = "aaa"
print(countPalindromicSubsequence(s6)) # Output: 1

s7 = "abcabcabc"
print(countPalindromicSubsequence(s7)) # Output: 9

s8 = "xyzxyzxyz"
print(countPalindromicSubsequence(s8)) # Output: 9

s9 = "abccba"
print(countPalindromicSubsequence(s9)) # Output: 3

s10 = "zzz"
print(countPalindromicSubsequence(s10)) # Output: 1