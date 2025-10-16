# MINIMUM NUMBER OF FLIPS TO MAKE THE BINARY STRING ALTERNATING

'''
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
- Type-1: Remove the character at the start of the string s and append it to the end of the string.
- Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
The string is called alternating if no two adjacent characters are equal.
'''

def minFlips(s):
    n = len(s)
    s = s + s
    alternate0 = ""
    alternate1 = ""
    
    for i in range(len(s)):
        alternate0 += "0" if i % 2 == 0 else "1"
        alternate1 += "1" if i % 2 == 0 else "0"
        
    result = float('inf')
    diff0 = ""
    diff1 = ""
    left = 0
    
    for right in range(len(s)):
        if s[right] != alternate0[right]:
            diff0 += 1
        if s[right] != alternate1[right]:
            diff1 += 1
            
        if (right - left + 1) > n:
            if s[left] != alternate0[left]:
                diff0 -= 1
            if s[left] != alternate1[left]:
                diff1 -= 1
            left += 1
            
        if (right - left + 1) == n:
            result = min(result, diff0, diff1)
            
    return result

'''
Time Complexity: O(n)
The algorithm iterates through the doubled string of length 2n once.
- Doubling the string `s = s + s` takes O(n) time.
- Creating the two alternating target strings (`alternate0`, `alternate1`) of length 2n takes O(n) time.
- The sliding window loop runs 2n times, and each operation inside the loop (comparisons, additions, subtractions) is O(1).
Therefore, the total time complexity is O(n) + O(n) + O(n) = O(n).

Space Complexity: O(n)
We create several new strings whose lengths are proportional to the original string's length n.
- The doubled string `s` takes O(n) space.
- The two alternating strings `alternate0` and `alternate1` each take O(n) space.
The other variables use constant space.
Therefore, the total space complexity is O(n).
'''

# Test Cases
s1 = "111000"
print(minFlips(s1)) # Output: 2

s2 = "010"
print(minFlips(s2)) # Output: 0

s3 = "1010"
print(minFlips(s3)) # Output: 0

s4 = "000"
print(minFlips(s4)) # Output: 1

s5 = "1111"
print(minFlips(s5)) # Output: 2

s6 = "0010"
print(minFlips(s6)) # Output: 1

s7 = "1110"
print(minFlips(s7)) # Output: 1

s8 = "1"
print(minFlips(s8)) # Output: 0

s9 = "00"
print(minFlips(s9)) # Output: 1

s10 = "0110101100"
print(minFlips(s10)) # Output: 4