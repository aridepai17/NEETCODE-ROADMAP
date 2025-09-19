# VALID PALINDROME

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''

# Solution 1: Using In-Built Functions
def isPalindrome1(s):
    newString = ""
    
    for char in s:
        if char.isalnum():
            newString += char.lower()
            
    return newString == newString[::-1]

'''
Time Complexity: O(n)
The loop iterates through the string once, which is O(n). Inside the loop, `isalnum()` and `lower()` are constant time operations for a character. 
The process of building `newString` takes O(n) time as we iterate through each character of the input string.
The slicing `newString[::-1]` creates a reversed copy of the string, which also takes O(n) time.
The final comparison `==` takes O(n) time in the worst case.
Thus, the total time complexity is dominated by these linear operations, resulting in O(n), where n is the length of the input string s.

Space Complexity: O(n)
We create a new string `newString` to store the filtered alphanumeric characters. In the worst case, if all characters in s are alphanumeric, the length of `newString` will be n.
Additionally, `newString[::-1]` creates another string of length n for the comparison.
Therefore, the space required is proportional to the length of the input string, making the space complexity O(n).
'''

# Solution 2: Using Two Pointers
def isPalindrome2(s):
    left = 0
    right = len(s) - 1
    
    while left <= right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() == s[right].lower():
                return False
            
            left += 1
            right -= 1
            
    return True

'''
Time Complexity: O(n)
The two pointers, `left` and `right`, start at the beginning and end of the string, respectively.
In each iteration of the `while` loop, at least one of the pointers moves towards the center.
The `left` pointer only moves forward, and the `right` pointer only moves backward.
This means each character in the string is visited at most once by either the `left` or `right` pointer.
The operations inside the loop (`isalnum()`, `lower()`, comparison) are all constant time.
Therefore, the time complexity is linear, O(n), where n is the length of the string.

Space Complexity: O(1)
This solution modifies pointers and performs comparisons in-place.
It does not use any extra data structures whose size depends on the length of the input string.
The memory used for the `left` and `right` pointers is constant.
Thus, the space complexity is O(1).
'''

# Test Cases
s1 = "A man, a plan, a canal: Panama"
print(isPalindrome2(s1)) # Output: True

s2 = "race a car"
print(isPalindrome2(s2)) # Output: False

s3 = ""
print(isPalindrome2(s3)) # Output: True

s4 = "a"
print(isPalindrome2(s4)) # Output: True

s5 = ",."
print(isPalindrome2(s5)) # Output: True

s6 = "Was it a car or a cat I saw?"
print(isPalindrome2(s6)) # Output: True

s7 = "Noon"
print(isPalindrome2(s7)) # Output: True

s8 = "0P"
print(isPalindrome2(s8)) # Output: False

s9 = "ab_a"
print(isPalindrome2(s9)) # Output: True

s10 = ".,"
print(isPalindrome2(s10)) # Output: True