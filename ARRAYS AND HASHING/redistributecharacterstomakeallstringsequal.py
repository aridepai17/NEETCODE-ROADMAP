# REDISTRIBUTE CHARACTERS TO MAKE ALL STRINGS EQUAL

'''
You are given an array of strings words (0-indexed).
In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
Return true if you can make every string in words equal using any number of operations, and false otherwise.
'''

def redistributeChar(words):
    hashMap = {}
    n = len(words)
    
    for word in words:
        for char in word:
            hashMap[char] = hashMap.get(char, 0) + 1
            
    for value in hashMap.values():
        if value % n:
            return False
        
    return True

'''
Time Complexity: O(N * K)
- N is the number of words in the input list.
- K is the average length of a word.
- We iterate through each character of each word once to build the frequency map. This takes O(N * K) time.
- Then, we iterate through the values in the hash map. In the worst case, the number of unique characters is proportional to the total number of characters, but it's often much smaller (e.g., limited to 26 for lowercase English letters). This step is generally faster than building the map.
- The dominant operation is counting all the characters.

Space Complexity: O(U) or O(1)
- U is the number of unique characters across all words.
- We use a hash map to store the frequency of each character.
- If the character set is fixed (e.g., lowercase English letters), the space complexity is O(1) because the map size is bounded by a constant (26).
- If the character set is not bounded, the space complexity is O(U).
'''

# Test Cases
words1 = ["abc", "aabc", "bc"] 
print(redistributeChar(words1)) # Output: True

words2 = ["ab", "a"]
print(redistributeChar(words2)) # Output: False

words3 = ["a", "a"]
print(redistributeChar(words3)) # Output: True

words4 = ["aabb", "bbaa", "abab", "baba"]
print(redistributeChar(words4)) # Output: True

words5 = ["abc", "def", "ghi"]
print(redistributeChar(words5)) # Output: False

words6 = ["topcoder"]
print(redistributeChar(words6)) # Output: True

words7 = ["", ""]
print(redistributeChar(words7)) # Output: True

words8 = ["a", ""]
print(redistributeChar(words8)) # Output: False

words9 = ["aa", "bb"]
print(redistributeChar(words9)) # Output: True

words10 = ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]
print(redistributeChar(words10)) # Output: True