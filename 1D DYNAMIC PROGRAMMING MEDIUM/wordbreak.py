# WORD BREAK

'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

'''
ALGORITHM:

This problem is solved using dynamic programming where dp[i] represents whether the substring s[0:i] can be segmented into dictionary words.

Algorithm:
1. Create a set from wordDict for O(1) lookup
2. Initialize dp array of size len(s) + 1, with dp[0] = True (empty string can always be segmented)
3. For each position i from 1 to len(s):
    a. If dp[i] is True (already reachable), skip
    b. Otherwise, check each word in wordSet:
        - If s starts with that word at position i, mark dp[i + len(word)] as True
4. Return dp[len(s)]

Key insight: We build up solutions from smaller substrings to larger ones.
'''

def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        if not dp[i]:
            continue
        
        for word in wordSet:
            if s.startswith(word, i):
                dp[i + len(word)] = True
                
    return dp[len(s)]

'''
Time Complexity: O(N × M × L), where N = len(s), M = len(wordDict), L = average length of words in wordDict.
We iterate through each position and try all dictionary words at each position.
Space Complexity: O(N + W), where N = len(s) for the dp array and W = total characters in wordDict for the set.
'''

# Test Cases

# Test Case 1: Basic case
s1 = "leetcode"
wordDict1 = ["leet", "code"]
result1 = wordBreak(s1, wordDict1)
print(result1)  # Expected: True

# Test Case 2: Multiple possible segmentations
s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
result2 = wordBreak(s2, wordDict2)
print(result2)  # Expected: True

# Test Case 3: Cannot be segmented
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
result3 = wordBreak(s3, wordDict3)
print(result3)  # Expected: False

# Test Case 4: Single word in dictionary
s4 = "helloworld"
wordDict4 = ["helloworld"]
result4 = wordBreak(s4, wordDict4)
print(result4)  # Expected: True

# Test Case 5: Empty string
s5 = ""
wordDict5 = ["a", "b", "c"]
result5 = wordBreak(s5, wordDict5)
print(result5)  # Expected: True (empty string can always be segmented)

# Test Case 6: String cannot be segmented due to character mismatch
s6 = "aaaaaaa"
wordDict6 = ["aaa", "aaaa"]
result6 = wordBreak(s6, wordDict6)
print(result6)  # Expected: True

# Test Case 7: Overlapping words
s7 = "cars"
wordDict7 = ["car", "cars", "ca", "rs"]
result7 = wordBreak(s7, wordDict7)
print(result7)  # Expected: True

# Test Case 8: Long word in dictionary
s8 = "abcd"
wordDict8 = ["ab", "abc", "abcd"]
result8 = wordBreak(s8, wordDict8)
print(result8)  # Expected: True

# Test Case 9: No matching words at all
s9 = "xyz"
wordDict9 = ["abc", "def"]
result9 = wordBreak(s9, wordDict9)
print(result9)  # Expected: False

# Test Case 10: Dictionary has single character words
s10 = "bbb"
wordDict10 = ["b", "bb", "bbb"]
result10 = wordBreak(s10, wordDict10)
print(result10)  # Expected: True