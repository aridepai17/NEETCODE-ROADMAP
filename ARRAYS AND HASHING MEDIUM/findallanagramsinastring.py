# FIND ALL ANAGRAMS IN A STRING

'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.
'''

def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    
    sCount = {}
    pCount = {}
    
    for i in range(len(p)):
        pCount[p[i]] = pCount.get(p[i], 0) + 1
        sCount[s[i]] = sCount.get(s[i], 0) + 1
        
    result = [0] if sCount == pCount else []
    
    left = 0
    for right in range(len(p), len(s)):
        sCount[s[right]] = sCount.get(s[right], 0) + 1
        sCount[s[left]] -= 1
        if sCount[s[left]] == 0:
            sCount.pop(s[left])
        left += 1
        if sCount == pCount:
            result.append(left)
            
    return result   

'''
Time Complexity: O(N)
- Let N be the length of the string s and M be the length of string p.
- Initializing pCount and sCount takes O(M).
- The for loop sliding the window runs (N - M) times, and each time the dictionary comparison sCount == pCount takes O(26) (since only lowercase letters are used, which is constant), and updating the dictionaries is O(1).
- Therefore, the overall time complexity is O(N), where N = len(s).

Space Complexity: O(1)
- Both sCount and pCount dictionaries store counts for lowercase English letters (maximum 26 entries each), so their sizes are bounded by a constant.
- Result array may store up to O(N) indices in the unlikely case every substring is an anagram, but the auxiliary space for frequency dictionaries is O(1).
So, total space complexity is O(1) (excluding the output).
'''

# Test Cases
s1 = "cbaebabacd"
p1 = "abc"
print(findAnagrams(s1, p1)) # Output: [0, 6]

s2 = "abab"
p2 = "ab"
print(findAnagrams(s2, p2)) # Output: [0, 1, 2]

s3 = "af"
p3 = "be"
print(findAnagrams(s3, p3)) # Output: []

s4 = "aaaaa"
p4 = "aa"
print(findAnagrams(s4, p4)) # Output: [0, 1, 2, 3]

s5 = "abcde"
p5 = "edcba"
print(findAnagrams(s5, p5)) # Output: [0]

s6 = "abacbabc"
p6 = "abc"
print(findAnagrams(s6, p6)) # Output: [1, 2, 3, 5]

s7 = ""
p7 = ""
print(findAnagrams(s7, p7)) # Output: [0]

s8 = "a"
p8 = "a"
print(findAnagrams(s8, p8)) # Output: [0]

s9 = "abc"
p9 = "abcd"
print(findAnagrams(s9, p9)) # Output: []

s10 = "bacdgabcda"
p10 = "abcd"
print(findAnagrams(s10, p10)) # Output: [0, 5, 6]