# MINIMUM NUMBER OF SWAPS TO MAKE STRING BALANCED

'''
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
A string is called balanced if and only if:
- It is the empty string, or
- It can be written as AB, where both A and B are balanced strings, or
- It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.
Return the minimum number of swaps to make s balanced.
'''

def minSwaps(s):
    extraClosing = 0
    maxClosing = 0
    
    for char in s:
        if char == "[":
            extraClosing -= 1
        else:
            extraClosing += 1
        
        maxClosing = max(maxClosing, extraClosing)
        
    return (maxClosing + 1) // 2

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The algorithm iterates through the string `s` exactly once.
- Inside the loop, operations like character comparison, addition, subtraction, and `max` function calls are all constant time operations, O(1).
- Therefore, the total time complexity is directly proportional to the length of the string, making it O(N).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables (`extraClosing`, `maxClosing`, `char`, loop index) regardless of the input size.
- No additional data structures are created that grow with the input size.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
s1 = "][]["
print(minSwaps(s1)) # Output: 1

s2 = "]]][[["
print(minSwaps(s2)) # Output: 2

s3 = "[]"
print(minSwaps(s3)) # Output: 0

s4 = "[[][]]"
print(minSwaps(s4)) # Output: 0

s5 = "]]][[[][]["
print(minSwaps(s5)) # Output: 2

s6 = "[]][[]"
print(minSwaps(s6)) # Output: 1

s7 = "[[][]]][]["
print(minSwaps(s7)) # Output: 1

s8 = "][][][]["
print(minSwaps(s8)) # Output: 2

s9 = "[[][][]]"
print(minSwaps(s9)) # Output: 0

s10 = "]]][[[["
print(minSwaps(s11)) # Output: 2