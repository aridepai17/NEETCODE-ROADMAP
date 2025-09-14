# MAXIMUM SCORE AFTER SPLITTING A STRING

'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
'''

def maxScore(s):
    zero = 0
    one = s.count('1')
    result = 0
    
    for i in range(len(s) - 1):
        if s[i] == '0':
            zero += 1
        else:
            one -= 1
        result = max(result, zero + one)
    
    return result

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The initial `s.count('1')` operation iterates through the entire string once, which takes O(N) time.
- The `for` loop iterates from the first character up to the second-to-last character of the string, which is N - 1 iterations. This is O(N).
- Inside the loop, all operations (character access, comparison, addition, subtraction, and `max`) are performed in constant time, O(1).
- The total time complexity is O(N) + O(N), which simplifies to O(N).

Space Complexity: O(1)
- The algorithm uses a few variables (`zero`, `one`, `result`, `i`) to store counts and the maximum score.
- The amount of extra space used is constant and does not scale with the length of the input string `s`.
- Therefore, the space complexity is O(1).
'''

# Test Cases
s1 = "00111"
print(maxScore(s1)) # Output: 5

s2 = "0000"
print(maxScore(s2)) # Output: 3

s3 = "1111"
print(maxScore(s3)) # Output: 3

s4 = "010101"
print(maxScore(s4)) # Output: 4

s5 = "101010"
print(maxScore(s5)) # Output: 3

s6 = "1110111"
print(maxScore(s6)) # Output: 5

s7 = "0001000"
print(maxScore(s7)) # Output: 5

s8 = "01"
print(maxScore(s8)) # Output: 2

s9 = "10"
print(maxScore(s9)) # Output: 0

s10 = "110010110"
print(maxScore(s10)) # Output: 5
