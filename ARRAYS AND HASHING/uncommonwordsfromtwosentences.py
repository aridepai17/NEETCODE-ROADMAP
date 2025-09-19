# UNCOMMON WORDS FROM TWO SENTENCES

'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
'''

def uncommonFromSentences(s1, s2):
    hashMap = {}
    list1 = s1.split(" ")
    list2 = s2.split(" ")
    result = []
    
    for word in list1 + list2:
        hashMap[word] = hashMap.get(word, 0) + 1
        
    for key, value in hashMap.items():
        if value == 1:
            result.append(key)
            
    return result

'''
Time Complexity: O(N + M)
Let N be the length of string `s1` and M be the length of string `s2`.
- Splitting `s1` and `s2` into lists of words takes O(N) and O(M) time, respectively.
- Concatenating the two lists of words (`list1 + list2`) takes time proportional to the total number of words, which is related to O(N + M).
- The first `for` loop iterates through every word from both sentences. For each word, it performs a hash map insertion/update. The total time for this loop is proportional to the total number of characters in both sentences, which is O(N + M).
- The second `for` loop iterates through the items in the hash map. The number of unique words is at most the total number of words. This loop also takes time proportional to the total number of characters in the unique words, which is at most O(N + M).
- The overall time complexity is the sum of these operations, which simplifies to O(N + M).

Space Complexity: O(N + M)
- The space required to store the lists of words from `s1` and `s2` is O(N + M).
- The hash map stores each unique word. In the worst case, where all words are unique, the space required for the hash map is proportional to the total number of characters in both sentences, which is O(N + M).
- The `result` list also stores words, and in the worst case, it could store all words, requiring O(N + M) space.
- Therefore, the total space complexity is dominated by the storage of words in the lists, hash map, and result, resulting in O(N + M).
'''

# Test Cases
s1 = "this apple is sweet", s2 = "this apple is sour"
print(uncommonFromSentences(s1, s2)) # Output: ["sweet", "sour"]

s1, s2 = "apple apple", "banana"
print(uncommonFromSentences(s1, s2)) # Output: ["banana"]

s1, s2 = "d b c", "a b c"
print(uncommonFromSentences(s1, s2)) # Output: ["d", "a"]

s1, s2 = "the quick brown fox", "the lazy dog"
print(uncommonFromSentences(s1, s2)) # Output: ["quick", "brown", "fox", "lazy", "dog"]

s1, s2 = "a b", "a b c"
print(uncommonFromSentences(s1, s2)) # Output: ["c"]

s1, s2 = "s z z", "s z z"
print(uncommonFromSentences(s1, s2)) # Output: []

s1, s2 = "a", "b"
print(uncommonFromSentences(s1, s2)) # Output: ["a", "b"]

s1, s2 = "this is fun", "this is also fun"
print(uncommonFromSentences(s1, s2)) # Output: ["also"]

s1, s2 = "i love coding", "coding is my passion"
print(uncommonFromSentences(s1, s2)) # Output: ["i", "love", "is", "my", "passion"]

s1, s2 = "one two three", "four five six"
print(uncommonFromSentences(s1, s2)) # Output: ["one", "two", "three", "four", "five", "six"]