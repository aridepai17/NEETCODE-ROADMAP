# TAKE K OF EACH CHARACTER FROM LEFT AND RIGHT

'''
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. 
Each minute, you may take either the leftmost character of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
'''

def takeCharacters(s, k):
    hashMap = {'a': 0, 'b': 0, 'c': 0}
    for char in s:
        hashMap[char] += 1
        
    if min(hashMap.values()) < k:
        return -1
    
    result = float('inf')
    left = 0
    
    for right in range(len(s)):
        hashMap[s[right]] -= 1
        
        while min(hashMap.values()) < k:
            hashMap[s[left]] += 1
            left += 1
            
        result = min(result, len(s) - (right - left + 1))
        
    return result

'''
Time Complexity: O(n)
The algorithm involves a few main steps:
1. Initial Count: We first iterate through the string `s` once to count the total occurrences of 'a', 'b', and 'c'. This takes O(n) time, where n is the length of the string.
2. Sliding Window: We use a sliding window approach with two pointers, `left` and `right`. The `right` pointer iterates through the string from beginning to end (n steps). The `left` pointer also moves forward, and across all iterations of the outer loop, it will traverse the string at most once.
Since each character is visited by the `right` and `left` pointers at most a constant number of times, the time complexity of the sliding window part is O(n).
Combining these, the total time complexity is O(n) + O(n) = O(n).

Space Complexity: O(1)
The algorithm uses a hash map (`hashMap`) to store the counts of the characters 'a', 'b', and 'c'. The size of this hash map is constant (3) and does not depend on the length of the input string `s`.
Other variables like `result`, `left`, and `right` also occupy constant space.
Therefore, the space complexity is O(1).
'''

# Test Cases
s1 = "aabacbebebe", k1 = 2
print(takeCharacters(s1, k1)) # Expected: 5 ("aab" from left, "be" from right)

s2 = "abc", k2 = 1
print(takeCharacters(s2, k2)) # Expected: 3

s3 = "abacaba", k3 = 1
print(takeCharacters(s3, k3)) # Expected: 3

s4 = "a", k4 = 1
print(takeCharacters(s4, k4)) # Expected: -1

s5 = "cba", k5 = 1
print(takeCharacters(s5, k5)) # Expected: 3

s6 = "ccbabcc", k6 = 2
print(takeCharacters(s6, k6)) # Expected: 4 

s7 = "acba", k7 = 1
print(takeCharacters(s7, k7)) # Expected: 3

s8 = "aabcaba", k8 = 0
print(takeCharacters(s8, k8)) # Expected: 0

s9 = "abacabacaba", k9 = 2
print(takeCharacters(s9, k9)) # Expected: 8

s10 = "abccbaabccba", k10 = 3
print(takeCharacters(s10, k10)) # Expected: 9