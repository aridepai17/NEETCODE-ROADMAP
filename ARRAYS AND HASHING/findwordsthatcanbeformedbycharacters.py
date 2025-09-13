# FIND WORDS THAT CAN BE FORMED BY CHARACTERS

'''
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).
Return the sum of lengths of all good strings in words.
'''

def countCharacters(words, chars):
    freq = {}
    result = 0
    
    for char in chars:
        freq[char] = freq.get(char, 0) + 1
        
    for word in words:
        currentWord = {}
        good = True
        for char in word:
            currentWord[char] = currentWord.get(char, 0) + 1
            if char not in freq or currentWord[char] > freq[char]:
                good = False
                break
        if good:
            result += len(word)
            
    return result

'''
Time Complexity: O(M + L)
Let M be the length of the `chars` string.
Let L be the total number of characters in all words combined (i.e., the sum of the lengths of all strings in the `words` list).

- First, we build a frequency map of the characters in `chars`. This requires iterating through `chars` once, which takes O(M) time.
- Then, we iterate through each `word` in the `words` list. For each `word`, we iterate through its characters to check if it can be formed.
- The inner loop, which processes each character of a word, runs a total of L times across all words. For each character, we perform constant-time hash map operations.
- Therefore, the total time complexity is the sum of the time to process `chars` and the time to process all words, which is O(M + L).

Space Complexity: O(1)
- The algorithm uses two hash maps: `freq` to store the character counts of `chars`, and `currentWord` to store the character counts for each word being checked.
- Since the problem is typically constrained to lowercase English letters, the number of unique characters is at most 26.
- The size of both hash maps is therefore bounded by a constant (26).
- Thus, the space complexity is O(1), as the extra space used does not scale with the size of the input strings.
'''

# Test Cases
words1 = ["cat", "bt", "hat", "tree"]
chars1 = "atach"
print(countCharacters(words1, chars1)) # Output: 6

words2 = ["hello", "world", "leetcode"]
chars2 = "welldonehoneyr"
print(countCharacters(words2, chars2)) # Output: 10 (hello + world)

words3 = ["apple"]
chars3 = "aple"
print(countCharacters(words3, chars3)) # Output: 0

words4 = []
chars4 = "abc"
print(countCharacters(words4, chars4)) # Output: 0

words5 = ["a", "b", "c"]
chars5 = ""
print(countCharacters(words5, chars5)) # Output: 0

words6 = ["a", "aa", "aaa"]
chars6 = "a"
print(countCharacters(words6, chars6)) # Output: 1

words7 = ["a", "aa", "aaa"]
chars7 = "aa"
print(countCharacters(words7, chars7)) # Output: 3 (a + aa)

words8 = ["abc", "def", "ghi"]
chars8 = "abcdefghi"
print(countCharacters(words8, chars8)) # Output: 9

words9 = ["z", "y", "x"]
chars9 = "abc"
print(countCharacters(words9, chars9)) # Output: 0

words10 = ["master", "piece", "leetcode"]
chars10 = "masterpiecel"
print(countCharacters(words10, chars10)) # Output: 11 (master + piece)