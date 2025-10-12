# LONGEST REPEATING CHARACTER REPLACEMENT

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

def characterReplacement(s, k):
    hashMap = {}
    left = 0
    result = 0
    
    for right in range(len(s)):
        hashMap[s[right]] = hashMap.get(s[right], 0) + 1
        while (right - left + 1) - max(hashMap.values()) > k:
            hashMap[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
        
    return result

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach, where `n` is the length of the input string `s`.
1. The `right` pointer iterates through the string from start to end, which takes O(n) time.
2. The `left` pointer also moves forward through the string. In total, across all iterations of the outer loop, the `left` pointer will traverse the string at most once.
3. Inside the loop, the most computationally intensive operation is `max(hashMap.values())`. Since the input string consists of uppercase English letters, the number of unique characters is constant (at most 26). Therefore, the `hashMap` will have at most 26 entries, and finding the maximum value takes constant time, O(1).
4. All other operations within the loop (dictionary updates, comparisons) are also O(1).
Since each character is processed a constant number of times by the `left` and `right` pointers, the overall time complexity is linear, O(n).

Space Complexity: O(1)
The algorithm uses a hash map (`hashMap`) to store the frequency of characters in the current sliding window.
Because the problem specifies that the string contains only uppercase English letters, the size of the `hashMap` is bounded by a constant (26).
The space required does not scale with the length of the input string `s`. Therefore, the space complexity is constant, O(1).
'''

# Test Cases
s1 = "ABAB", k1 = 2
print(characterReplacement(s1, k1)) # Output: 4

s2 = "AABABBA", k2 = 1
print(characterReplacement(s2, k2)) # Output: 4

s3 = "ABCDE", k3 = 1
print(characterReplacement(s3, k3)) # Output: 2

s4 = "AAAA", k4 = 2
print(characterReplacement(s4, k4)) # Output: 4

s5 = "ABBB", k5 = 0
print(characterReplacement(s5, k5)) # Output: 3

s6 = "IMNJJTR", k6 = 2
print(characterReplacement(s6, k6)) # Output: 4

s7 = "KRSCDCSONAJSC", k7 = 3
print(characterReplacement(s7, k7)) # Output: 5

s8 = "ABC", k8 = 100
print(characterReplacement(s8, k8)) # Output: 3

s9 = "BAAAB", k9 = 0
print(characterReplacement(s9, k9)) # Output: 3

s10 = "BAAA", k10 = 0
print(characterReplacement(s10, k10)) # Output: 3