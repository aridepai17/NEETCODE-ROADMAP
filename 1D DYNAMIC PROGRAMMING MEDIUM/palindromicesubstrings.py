# PALINDROMIC SUBSTRINGS

'''
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
'''

'''
ALGORITHM:

This problem uses the expand around center technique. Each palindrome has a center, and we can expand from that center to find all palindromes.

For each character in the string, we consider two types of centers:
1. Odd-length palindromes: center is a single character
2. Even-length palindromes: center is between two characters

For each center, we expand outward as long as the characters match, incrementing the count for each valid palindrome.

Algorithm:
1. Initialize total = 0 to count palindromic substrings
2. Define helper function countPalindromes(left, right):
    - While left >= 0 and right < len(s) and s[left] == s[right]:
        - Increment total by 1 (we found a palindrome)
        - Expand outward: left -= 1, right += 1
3. For each index i in the string:
    - Call countPalindromes(i, i) for odd-length palindromes
    - Call countPalindromes(i, i + 1) for even-length palindromes
4. Return total
'''

def countSubstrings(s):
    total = 0
    
    def countPalindromes(left, right):
        nonlocal total
        while left >= 0 and right < len(s) and s[left] == s[right]:
            total += 1
            left -= 1
            right += 1
            
    for i in range(len(s)):
        countPalindromes(i, i)       # Odd length palindrome
        countPalindromes(i, i + 1)   # Even length palindrome
        
    return total

'''
Time Complexity: O(N^2), where N is the length of the string. In the worst case, we expand around each center.
Space Complexity: O(1) - only using constant extra space.
'''

# Test Cases

# Test Case 1: Simple palindrome
s1 = "abc"
result1 = countSubstrings(s1)
print(result1) # Expected: 3 ("a", "b", "c")

# Test Case 2: Single character
s2 = "a"
result2 = countSubstrings(s2)
print(result2) # Expected: 1

# Test Case 3: Two same characters
s3 = "aa"
result3 = countSubstrings(s3)
print(result3) # Expected: 3 ("a", "a", "aa")

# Test Case 4: All same characters
s4 = "aaa"
result4 = countSubstrings(s4)
print(result4) # Expected: 6 ("a", "a", "a", "aa", "aa", "aaa")

# Test Case 5: Palindrome string
s5 = "aba"
result5 = countSubstrings(s5)
print(result5) # Expected: 4 ("a", "b", "a", "aba")

# Test Case 6: Mixed string
s6 = "aab"
result6 = countSubstrings(s6)
print(result6) # Expected: 4 ("a", "a", "b", "aa")

# Test Case 7: Longer palindrome
s7 = "abcba"
result7 = countSubstrings(s7)
print(result7) # Expected: 7

# Test Case 8: Even length palindrome
s8 = "abba"
result8 = countSubstrings(s8)
print(result8) # Expected: 6

# Test Case 9: Empty string
s9 = ""
result9 = countSubstrings(s9)
print(result9) # Expected: 0

# Test Case 10: Single character repeated
s10 = "aaaaa"
result10 = countSubstrings(s10)
print(result10) # Expected: 15 (n*(n+1)/2 = 5*6/2 = 15) 