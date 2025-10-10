# MAXIMUM NUMBER OF VOWELS IN A SUBSTRING OF GIVEN LENGTH

'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''

def maxVowels(s, k):
    vowels = set('aeiou')
    left = 0
    count = 0
    maxCount = 0
    
    for right in range(len(s)):
        if s[right] in vowels:
            count += 1
        if right - left + 1 > k:
            if s[left] in vowels:
                count -= 1
            left += 1
            
        maxCount = max(maxCount, count)
        
    return maxCount

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach. We iterate through the string `s` once with the `right` pointer. 
For each character, we perform a constant number of operations (checking for a vowel in a set, incrementing/decrementing a counter, updating a maximum). 
The `left` pointer also traverses the string at most once. Therefore, the time complexity is linear with respect to the length of the string, 'n'.

Space Complexity: O(1)
We use a constant amount of extra space. The `vowels` set has a fixed size (5 characters). 
The other variables (`left`, `count`, `maxCount`, `right`) also occupy a constant amount of space, regardless of the input string's length.
'''

# Test Cases
s1 = "abciiidef", k1 = 3
print(maxVowels(s1, k1)) # Output: 3

s2 = "aeiou", k2 = 2
print(maxVowels(s2, k2)) # Output: 2

s3 = "leetcode", k3 = 3
print(maxVowels(s3, k3)) # Output: 2

s4 = "rhythms", k4 = 4
print(maxVowels(s4, k4)) # Output: 0

s5 = "weallloveyou", k5 = 7
print(maxVowels(s5, k5)) # Output: 4

s6 = "tryhard", k6 = 4
print(maxVowels(s6, k6)) # Output: 1

s7 = "sun", k7 = 2
print(maxVowels(s7, k7)) # Output: 1

s8 = "aeiou", k8 = 5
print(maxVowels(s8, k8)) # Output: 5

s9 = "n", k9 = 1
print(maxVowels(s9, k9)) # Output: 0

s10 = "a", k10 = 1
print(maxVowels(s10, k10)) # Output: 1