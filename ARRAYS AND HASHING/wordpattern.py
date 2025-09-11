# WORD PATTERN

'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. 
Specifically:
- Each letter in pattern maps to exactly one unique word in s.
- Each unique word in s maps to exactly one letter in pattern.
- No two letters map to the same word, and no two words map to the same letter.
'''

def wordPattern(pattern, s):
    words = s.split()
    if len(words) != len(pattern):
        return False
    
    hashMap1 = {}
    hashMap2 = {}
    
    
    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]
        
        if char in hashMap1 and hashMap1[char] != word:
            return False
        if word in hashMap2 and hashMap2[word] != char:
            return False
        
        hashMap1[char] = word
        hashMap2[word] = char
        
    return True

'''
Time Complexity: O(P + M)
Let P be the length of the `pattern` string and M be the length of the string `s`.
- `s.split()`: This operation splits the string `s` into a list of words. It takes O(M) time as it needs to iterate through the entire string `s`.
- The code then checks if the number of words (`N`) equals the length of the pattern (`P`). If not, it returns. For the rest of the analysis, we assume `N = P`.
- The `for` loop iterates `P` times.
- Inside the loop, we perform hash map operations.
  - For `hashMap1`, the keys are characters, so lookups, insertions, and comparisons are O(1) on average.
  - For `hashMap2`, the keys are words. Hashing a word and comparing it takes time proportional to the length of the word.
- The total time for all hash map operations across the loop is proportional to the sum of the lengths of all words, which is O(M).
- Therefore, the overall time complexity is dominated by the string split and the loop, resulting in O(M) + O(P + M), which simplifies to O(P + M).

Space Complexity: O(P + M)
- `words = s.split()`: This creates a new list of words, which requires O(M) space to store all the characters of `s`.
- `hashMap1`: Stores mappings from characters in `pattern` to words. In the worst case, it stores `P` entries. The space for keys is O(P), and the values are references to the words stored in the `words` list. So, this map takes O(P) space.
- `hashMap2`: Stores mappings from words to characters. In the worst case, it stores `N` unique words (where `N=P`). The space required for the keys is proportional to the sum of the lengths of the unique words, which can be up to O(M). The space for values is O(N) or O(P).
- The dominant factor is the space for the `words` list and the keys of `hashMap2`.
- Thus, the overall space complexity is O(M + P).
'''

# Test Cases
pattern1 = "abba", s1 = "dog cat cat dog"
print(wordPattern(pattern1, s1)) # Output: True

pattern2 = "abba", s2 = "dog cat cat fish"
print(wordPattern(pattern2, s2)) # Output: False

pattern3 = "aaaa", s3 = "dog cat cat dog"
print(wordPattern(pattern3, s3)) # Output: False

pattern4 = "abba", s4 = "dog dog dog dog"
print(wordPattern(pattern4, s4)) # Output: False

pattern5 = "abc", s5 = "b c a"
print(wordPattern(pattern5, s5)) # Output: True

pattern6 = "ab", s6 = "dog cat"
print(wordPattern(pattern6, s6)) # Output: True

pattern7 = "aa", s7 = "dog dog"
print(wordPattern(pattern7, s7)) # Output: True

pattern8 = "jquery", s8 = "jquery"
print(wordPattern(pattern8, s8)) # Output: False

pattern9 = "a", s9 = "a"
print(wordPattern(pattern9, s9)) # Output: True

pattern10 = "he", s10 = "unit"
print(wordPattern(pattern10, s10)) # Output: True
