# VALID PALINDROME 2

'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''

def validPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left <= right:
        if s[left] != s[right]:
            skipLeft = s[left + 1 : right + 1]
            skipRight = s[left : right]
            return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
        
        left += 1
        right -= 1
        
    return True

'''
Time Complexity: O(n)
The main `while` loop runs at most n/2 times, where n is the length of the string.
When a mismatch is found, we create two substrings, `skipLeft` and `skipRight`.
The length of these substrings can be at most n.
Checking if a substring is a palindrome by slicing and reversing (`[::-1]`) takes time proportional to the length of the substring.
In the worst case, this check takes O(n) time.
Since this palindrome check happens at most once, the total time complexity is dominated by this linear operation, resulting in O(n).

Space Complexity: O(n)
When a mismatch is found, we create two new substrings, `skipLeft` and `skipRight`, by slicing the original string.
In the worst case, the length of these substrings is proportional to n.
For example, if the mismatch is at the ends of the string, the slices will be of length n-1.
The reversal operation `[::-1]` also creates a temporary copy of the substring.
Therefore, the space required is proportional to the length of the input string, making the space complexity O(n).
'''

# Test Cases
s1 = "aba"
print(validPalindrome(s1)) # Output: True

s2 = "abca"
print(validPalindrome(s2)) # Output: True

s3 = "abc"
print(validPalindrome(s3)) # Output: False

s4 = "deeee"
print(validPalindrome(s4)) # Output: True

s5 = "raceacar"
print(validPalindrome(s5)) # Output: True

s6 = "tebbem"
print(validPalindrome(s6)) # Output: False

s7 = ""
print(validPalindrome(s7)) # Output: True

s8 = "a"
print(validPalindrome(s8)) # Output: True

s9 = "ab"
print(validPalindrome(s9)) # Output: True

s10 = "aydmda"
print(validPalindrome(s10)) # Output: True