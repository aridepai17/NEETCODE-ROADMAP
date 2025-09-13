# REVERSE STRING

'''
Write a function that reverses a string. 
The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory
'''

def reverseString(s):
    left = 0
    right = len(s) - 1
    
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

'''
Time Complexity: O(N)
Let N be the length of the input array `s`.
- The algorithm uses a two-pointer approach, with `left` starting at the beginning and `right` at the end of the array.
- The `while` loop runs as long as `left` is less than or equal to `right`.
- In each iteration, the pointers move one step closer to the center. The loop runs approximately N / 2 times.
- Since the number of iterations is proportional to the size of the input array, the time complexity is O(N).

Space Complexity: O(1)
- The reversal is performed in-place, modifying the input array directly without allocating a new one.
- The algorithm uses a constant amount of extra space for the `left` and `right` pointers, regardless of the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
s1 = ["h","e","l","l","o"]
print(reverseString(s1)) # Output: ["o", "l", "l", "e", "h"]

s2 = ["H","a","n","n","a","h"]
reverseString(s2)
print(s2) # Output: ["h","a","n","n","a","H"]

s3 = ["a"]
reverseString(s3)
print(s3) # Output: ["a"]

s4 = []
reverseString(s4)
print(s4) # Output: []

s5 = ["1", "2", "!", "@"]
reverseString(s5)
print(s5) # Output: ["@", "!", "2", "1"]

s6 = ["p", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g"]
reverseString(s6)
print(s6) # Output: ["g","n","i","m","m","a","r","g","o","r","p"]

s7 = ["r", "a", "c", "e", "c", "a", "r"]
reverseString(s7)
print(s7) # Output: ["r","a","c","e","c","a","r"]

s8 = ["a", "b"]
reverseString(s8)
print(s8) # Output: ["b", "a"]

s9 = [" ", "a", " ", "b", " "]
reverseString(s9)
print(s9) # Output: [" ","b"," ","a"," "]

s10 = ["A", "p", "p", "L", "e"]
reverseString(s10)
print(s10) # Output: ["e","L","p","p","A"]