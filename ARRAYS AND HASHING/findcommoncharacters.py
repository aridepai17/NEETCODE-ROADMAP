# FIND COMMON CHARACTERS

'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.
'''

def commonChars(words):
    hashMap = {}
    
    for char in words[0]:
        hashMap[char] = hashMap.get(char, 0) + 1
        
    for i in range(1, len(words)):
        currentFreq = {}
        for char in words[i]:
            currentFreq[char] = currentFreq.get(char, 0) + 1
            
        for char in hashMap:
            if char in currentFreq:
                hashMap[char] = min(hashMap[char], currentFreq[char])
            else:
                hashMap[char] = 0
            
    result = []
    for char, count in hashMap.items():
        result.extend([char] * count)
        
    return result

'''
Time Complexity: O(L), where L is the total number of characters in all strings.
- We iterate through every character of every string once to build the frequency maps.
- Let N be the number of words and M be the average length of a word. L is approximately N * M.
- The first loop takes O(length of first word).
- The main loop iterates N-1 times. Inside, it builds a frequency map for the current word (O(length of current word)) and then updates the main hash map (O(1) because the alphabet size is constant, 26).
- Summing up the time to process all characters across all words gives a total time complexity proportional to L.

Space Complexity: O(1).
- We use two hash maps to store character frequencies. 
- Since the input is limited to lowercase English letters, the maximum number of keys in each hash map is 26.
- Therefore, the space required for the hash maps is constant and does not depend on the size of the input words.
- The space for the result array is not typically included in space complexity analysis, but even if it were, it's also bounded.
'''

# Test Cases
words1 = ["bella", "label", "roller"]
print(commonChars(words1)) # Output: ["e","l","l"]

words2 = ["cool","lock","cook"]
print(commonChars(words2)) # Output: ["c","o"]

words3 = ["abc","def","ghi"]
print(commonChars(words3)) # Output: []

words4 = ["a"]
print(commonChars(words4)) # Output: ["a"]

words5 = ["aabb", "bbaa", "abab"]
print(commonChars(words5)) # Output: ["a", "a", "b", "b"]

words6 = ["hello", "world"]
print(commonChars(words6)) # Output: ["l", "o"]

words7 = ["mississippi", "missouri"]
print(commonChars(words7)) # Output: ["m", "i", "i", "s", "s"]

words8 = ["", "abc", "def"]
print(commonChars(words8)) # Output: []

words9 = ["z", "zz", "zzz"]
print(commonChars(words9)) # Output: ["z"]

words10 = ["programming", "progress", "program"]
print(commonChars(words10)) # Output: ["p", "r", "o", "g", "r"]