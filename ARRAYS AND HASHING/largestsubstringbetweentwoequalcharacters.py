# LARGEST SUBSTRING BETWEEN TWO EQUAL CHARACTERS

'''
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. 
If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.
'''

def maxLengthBetweenEqualCharacters(s):
    hashMap = {}
    result = -1
    
    for i in range(len(s)):
        char = s[i]
        if char in hashMap:
            result = max(result, i - hashMap[char] - 1)
        else:
            hashMap[char] = i
            
    return result

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The algorithm iterates through the string once with a single for loop, which runs N times.
- Inside the loop, all operations—hash map lookups (`in hashMap`), insertions (`hashMap[char] = i`), and comparisons (`max`)—take constant time on average, O(1).
- Therefore, the overall time complexity is directly proportional to the length of the string, resulting in O(N).

Space Complexity: O(U) or O(1)
- U is the number of unique characters in the string `s`.
- The algorithm uses a hash map to store the first index at which each character appears.
- In the worst case, if all characters in the string are unique, the hash map will store U entries.
- Thus, the space complexity is O(U).
- If the character set is bounded by a constant size (e.g., 26 for lowercase English letters), the space complexity can be considered O(1).
'''

# Test Cases
s1 = "aa"
print(maxLengthBetweenEqualCharacters(s1)) # Output: 0

s2 = "abca"
print(maxLengthBetweenEqualCharacters(s2)) # Output: 2

s3 = "cbzxy"
print(maxLengthBetweenEqualCharacters(s3)) # Output: -1

s4 = "abccba"
print(maxLengthBetweenEqualCharacters(s4)) # Output: 4

s5 = "scayofestival"
print(maxLengthBetweenEqualCharacters(s5)) # Output: 7

s6 = ""
print(maxLengthBetweenEqualCharacters(s6)) # Output: -1

s7 = "a"
print(maxLengthBetweenEqualCharacters(s7)) # Output: -1

s8 = "mgntdygtxnc"
print(maxLengthBetweenEqualCharacters(s8)) # Output: 6

s9 = "aaaa"
print(maxLengthBetweenEqualCharacters(s9)) # Output: 2

s10 = "joj"
print(maxLengthBetweenEqualCharacters(s10)) # Output: 1