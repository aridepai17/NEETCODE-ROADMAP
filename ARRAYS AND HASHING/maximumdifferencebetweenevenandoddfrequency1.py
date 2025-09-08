# MAXIMUM DIFFERENCE BETWEEN EVEN AND ODD FREQUENCY 1

'''
You are given a string s consisting of lowercase English letters.
Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:
- a1 has an odd frequency in the string.
- a2 has an even frequency in the string.
Return this maximum difference.
'''

def maxDifference(s):
    hashMap = {}
    
    for char in s:
        hashMap[char] = hashMap.get(char, 0) + 1
        
    odd = 0
    even = len(s)
    
    for count in hashMap.values():
        if count % 2 == 1:
            odd = max(odd, count)
        elif count != 0:
            even = min(even, count)
            
    return odd - even

'''
Time Complexity: O(n) where n is the length of the string s.
We iterate through the string once to build the frequency map, which takes O(n) time.
Then, we iterate through the values of the map. The number of unique characters is at most 26 (a constant for lowercase English letters), so this takes O(1) time.
Thus, the total time complexity is dominated by the first loop, making it O(n).

Space Complexity: O(1)
We use a hash map to store the frequency of characters. Since there are only 26 possible lowercase English letters,
the size of the hash map is bounded by a constant. Therefore, the space complexity is O(1).
If the character set were not fixed, the space complexity would be O(k) where k is the number of unique characters.
'''

# Test Cases
s1 = "aaaaabbc"
print(maxDifference(s1))  # Output: 3

s2 = "abcde"
print(maxDifference(s2))  # Output: -4

s3 = "aabbcc"
print(maxDifference(s3))  # Output: -2

s4 = ""
print(maxDifference(s4))  # Output: 0

s5 = "a"
print(maxDifference(s5))  # Output: 0

s6 = "aa"
print(maxDifference(s6))  # Output: -2

s7 = "zzzyyxxw"
print(maxDifference(s7))  # Output: 1

s8 = "abacaba"
print(maxDifference(s8))  # Output: -1

s9 = "banana"
print(maxDifference(s9))  # Output: 1

s10 = "zzzzz"
print(maxDifference(s10)) # Output: 0
