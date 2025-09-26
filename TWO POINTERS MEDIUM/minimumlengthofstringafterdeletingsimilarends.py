# MINIMUM LENGTH OF STRING AFTER DELETING SIMILAR ENDS

'''
Given a string s consisting only of characters 'a', 'b', and 'c'. 
You are asked to apply the following algorithm on the string any number of times:
- Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
- Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
- The prefix and the suffix should not intersect at any index.
- The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).
'''

def minimumLength(s):
    left = 0
    right = len(s) - 1
    
    while left < right and s[left] == s[right]:
        target = s[left]
        while left <= right and s[left] == target:
            left += 1
        while left <= right and s[right] == target:
            right -= 1
            
    return right - left + 1

'''
Time Complexity: O(N)
- We use a two-pointer approach with `left` and `right` pointers.
- The `left` pointer only moves forward, and the `right` pointer only moves backward.
- In the worst case, each character is visited once by either the `left` or `right` pointer.
- Therefore, the time complexity is linear with respect to the length of the string, N.

Space Complexity: O(1)
- We only use a few variables to store the pointers (`left`, `right`) and the target character.
- The space required does not grow with the size of the input string.
- Thus, the space complexity is constant.
'''

# Test Cases
s1 = "ca"
print(minimumLength(s1)) # Output: 2

s2 = "cabaabac"
print(minimumLength(s2)) # Output: 0

s3 = "aabccabba"
print(minimumLength(s3)) # Output: 3

s4 = "bbbbbbbbbbbbbbbbbbbbbbbbbbb"
print(minimumLength(s4)) # Output: 0

s5 = "abccba"
print(minimumLength(s5)) # Output: 0

s6 = "a"
print(minimumLength(s6)) # Output: 1

s7 = ""
print(minimumLength(s7)) # Output: 0

s8 = "b"
print(minimumLength(s8)) # Output: 1

s9 = "abcde"
print(minimumLength(s9)) # Output: 5

s10 = "aabccba"
print(minimumLength(s10)) # Output: 0