# LONGEST SUBSTRING WITH ATMOST TWO DISTINCT CHARACTERS

'''
Given a string s, return the length of the longest substring that contains at most two distinct characters.
'''

def lengthofLongestSubstringTwoDistinct(s):
    hashMap = {}
    left = 0
    result = 0
    
    for right in range(len(s)):
        hashMap[s[right]] = hashMap.get(s[right], 0) + 1
        
        while len(hashMap) > 2:
            hashMap[s[left]] -= 1
            if hashMap[s[left]] == 0:
                hashMap.pop(s[left])
            left += 1
            
        result = max(result, right - left + 1)
        
    return result

'''
Time Complexity: O(N)
The algorithm uses a sliding window approach with two pointers, `left` and `right`.
The `right` pointer iterates through the string from the beginning to the end, which takes O(N) time, where N is the length of the string.
The `left` pointer also moves from left to right. In the worst case, both pointers traverse the entire string once.
Each character is visited by the `right` pointer once and by the `left` pointer at most once.
The hash map operations (insertion, deletion, and access) take O(1) time on average.
Therefore, the total time complexity is O(N).

Space Complexity: O(1)
The algorithm uses a hash map to store the frequency of characters within the current window.
The `while` loop ensures that the size of the hash map never exceeds 3 (as it shrinks the window when the number of distinct characters becomes 3).
Since the number of distinct characters in the hash map is bounded by a constant, the space required is constant.
Thus, the space complexity is O(1).
'''

# Test Cases
s1 = 'ninninja'
print(lengthofLongestSubstringTwoDistinct(s1)) # Output: 6

s2 = "eceba"
print(lengthofLongestSubstringTwoDistinct(s2)) # Output: 3

s3 = "ccaabbb"
print(lengthofLongestSubstringTwoDistinct(s3)) # Output: 5

s4 = ""
print(lengthofLongestSubstringTwoDistinct(s4)) # Output: 0

s5 = "a"
print(lengthofLongestSubstringTwoDistinct(s5)) # Output: 1

s6 = "ab"
print(lengthofLongestSubstringTwoDistinct(s6)) # Output: 2

s7 = "aaaaa"
print(lengthofLongestSubstringTwoDistinct(s7)) # Output: 5

s8 = "abaccc"
print(lengthofLongestSubstringTwoDistinct(s8)) # Output: 4

s9 = "abcabcabc"
print(lengthofLongestSubstringTwoDistinct(s9)) # Output: 2

s10 = "zzzyyxxww"
print(lengthofLongestSubstringTwoDistinct(s10)) # Output: 5