# LONGEST PALINDROMIC SUBSTRING

'''
Given a string s, return the longest palindromic substring in s.
'''

'''
ALGORITHM:

This problem can be solved using the expand around center technique. A palindrome mirrors around its center, 
so we can expand around each center to find the longest palindrome.

For each character (or pair of characters for even-length palindromes), we expand outward as long as the 
characters match. The key insight is that there are 2N-1 possible centers for palindromes in a string of length N:
- N odd-length centers (each single character)
- N-1 even-length centers (each gap between characters)

The algorithm:
1. For each character in the string (i from 0 to n-1):
    a. Expand around character i as center (for odd-length palindromes)
    b. Expand around the gap between i and i+1 (for even-length palindromes)
2. For each expansion, check if the characters at left and right match
3. If they match, continue expanding; if not, stop
4. Track the longest palindrome found
'''

# Using Two Pointers and Sliding Window (has a bug - returns early)
def longestPalindromeBroken(s):
    result = ""
    resultLength = 0
    n = len(s)
    
    
    for i in range(n):
        # Odd Palindromes
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            if (right - left + 1) > resultLength:
                result = s[left : right + 1]
                resultLength = right - left + 1
            left -= 1
            right += 1
            
        # Even Palindromes
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if (right - left + 1) > resultLength:
                result = s[left : right + 1]
                resultLength = right - left + 1
            left -= 1
            right += 1
            
        return result  # BUG: Returns too early!
    

# Using Helper function (Correct version)
def longestPalindrome(s):
    if not s:
        return ""
    
    result = ""
    resultLength = 0
    n = len(s)
    
    def expansion(left, right):
        nonlocal result, resultLength
        while left >= 0 and right < n and s[left] == s[right]:
            if (right - left + 1) > resultLength:
                result = s[left : right + 1]
                resultLength = right - left + 1
            left -= 1
            right += 1
            
        return result
    
    for i in range(n):
        expansion(i, i)        # Odd length palindrome (single character center)
        expansion(i, i + 1)    # Even length palindrome (between two characters)
        
    return result

'''
Time Complexity: O(N^2), where N is the length of the string. In the worst case, we expand around each center.
Space Complexity: O(1) - only using constant extra space.
'''

# Test Cases

# Test Case 1: Simple palindrome
s1 = "babad"
result1 = longestPalindrome(s1)
print(result1) # Expected: "bab" or "ada"

# Test Case 2: Single character
s2 = "a"
result2 = longestPalindrome(s2)
print(result2) # Expected: "a"

# Test Case 3: Two characters (same)
s3 = "aa"
result3 = longestPalindrome(s3)
print(result3) # Expected: "aa"

# Test Case 4: Two characters (different)
s4 = "ab"
result4 = longestPalindrome(s4)
print(result4) # Expected: "a" or "b"

# Test Case 5: Entire string is palindrome
s5 = "racecar"
result5 = longestPalindrome(s5)
print(result5) # Expected: "racecar"

# Test Case 6: Multiple palindromes
s6 = "cbbd"
result6 = longestPalindrome(s6)
print(result6) # Expected: "bb"

# Test Case 7: Empty string
s7 = ""
result7 = longestPalindrome(s7)
print(result7) # Expected: ""

# Test Case 8: Repeated characters
s8 = "aaaa"
result8 = longestPalindrome(s8)
print(result8) # Expected: "aaaa"

# Test Case 9: Palindrome at beginning
s9 = "abacdfgdcaba"
result9 = longestPalindrome(s9)
print(result9) # Expected: "aba" or "aca"

# Test Case 10: Long string
s10 = "forgeeksskeegfor"
result10 = longestPalindrome(s10)
print(result10) # Expected: "geeksskeeg"
