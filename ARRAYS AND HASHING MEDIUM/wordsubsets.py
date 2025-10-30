# WORD SUBSETS

'''
You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order.
'''

def wordSubsets(words1, words2):
    maxCount = [0] * 26
    
    for word in words2:
        currentCount = [0] * 26
        for char in word:
            currentCount[ord(char) - ord('a')] += 1
            
        for i in range(26):
            maxCount[i] = max(maxCount[i], currentCount[i])
            
    universalStrings = []
    for word in words1:
        currentCharCount = [0] * 26
        for char in word:
            currentCharCount[ord(char) - ord('a')] += 1
            
        isUniversal = True
        for i in range(26):
            if currentCharCount[i] < maxCount[i]:
                isUniversal = False
                break
            
        if isUniversal:
            universalStrings.append(word)
            
    return universalStrings

'''
Time Complexity: O(M + N)
- Let M be the total length of all words in words1.
- Let N be the total length of all words in words2.
- It takes O(N) time to build the maxCount list from words2 because every character of every word in words2 is counted once.
- It takes O(M) time to process each word in words1, counting characters and comparing to maxCount.

Space Complexity: O(1)
- The space for maxCount and currentCharCount is constant (size 26).
- The output list universalStrings takes up to O(len(words1)) space in the worst case, but this is for output.
- There is no extra space used proportional to the input size (beyond the result).
'''

# Test Cases
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
print(wordSubsets(words1, words2)) # Output: ["facebook","google"]

words1 = ["a", "b", "ab", "ba"]
words2 = ["a"]
print(wordSubsets(words1, words2))  # Output: ["a", "ab", "ba"]

words1 = ["amazon", "leetcode", "apple", "plea", "plead"]
words2 = ["e", "a"]
print(wordSubsets(words1, words2))  # Output: ["leetcode", "apple", "plead"]

words1 = ["aa", "aaa", "aab", "ab", "baaa"]
words2 = ["a", "a"]
print(wordSubsets(words1, words2))  # Output: ["aa", "aaa", "aab", "baaa"]

words1 = ["abc", "def", "ghi"]
words2 = ["z"]
print(wordSubsets(words1, words2))  # Output: []

words1 = ["abc", "abcd", "abcefg", "abcdefg"]
words2 = []
print(wordSubsets(words1, words2))  # Output: ["abc", "abcd", "abcefg", "abcdefg"]

words1 = ["abd", "abdce", "cdeab", "bdaec", "cead"]
words2 = ["a", "b", "e"]
print(wordSubsets(words1, words2))  # Output: ["abdce", "cdeab", "bdaec"]

words1 = []
words2 = ["a"]
print(wordSubsets(words1, words2))  # Output: []

words1 = ["apple", "pleeea", "appllee", "eapplleee"]
words2 = ["e", "e", "l"]
print(wordSubsets(words1, words2))  # Output: ["pleeea", "appllee", "eapplleee"]

words1 = ["hello", "world", "hold", "helloworld"]
words2 = ["h", "o", "l", "d"]
print(wordSubsets(words1, words2))  # Output: ["hold", "helloworld"]