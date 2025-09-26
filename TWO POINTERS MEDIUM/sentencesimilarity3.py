# SENTENCE SIMILARITY 3

'''
You are given two strings sentence1 and sentence2, each representing a sentence composed of words. 
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of only uppercase and lowercase English characters.
Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. 
Note that the inserted sentence must be separated from existing words by spaces.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. 
Otherwise, return false.
'''

def areSentencesSimilar(sentence1, sentence2):
    w1 = sentence1.split()
    w2 = sentence2.split()
    
    n1 = len(w1)
    n2 = len(w2)
    
    prefix = 0
    while prefix < n1 and prefix < n2 and w1[prefix] == w2[prefix]:
        prefix += 1
        
    s1 = n1 - 1
    s2 = n2 - 1
    
    while s1 <= prefix and s1 <= prefix and w1[s1] == w2[s2]:
        s1 -= 1
        s2 -= 1
        
    return s1 < prefix or s2 < prefix

'''
Time Complexity: O(N + M)
- N is the length of sentence1 and M is the length of sentence2.
- The `split()` operation takes O(N + M) time to create the lists of words.
- The two while loops iterate through the words. The first loop finds the common prefix, and the second loop finds the common suffix.
- In total, each word is visited at most once by the pointers, so the loops take time proportional to the number of words.
- Since comparing words also takes time proportional to their length, the total time for the loops is also bounded by O(N + M).
- Therefore, the overall time complexity is dominated by the length of the sentences.

Space Complexity: O(N + M)
- We store the words of both sentences in two separate lists, `w1` and `w2`.
- The space required for these lists is proportional to the total length of the sentences.
'''

# Test Cases
sentence1 = "My name is Haley", sentence2 = "My Haley"
print(areSentencesSimilar(sentence1, sentence2)) # Output: True

sentence1, sentence2 = "a b c", "a b c"
print(areSentencesSimilar(sentence1, sentence2)) # Output: True

sentence1, sentence2 = "of", "A lot of words"
print(areSentencesSimilar(sentence1, sentence2)) # Output: False

sentence1, sentence2 = "Eating right is important", "Eating right is very important"
print(areSentencesSimilar(sentence1, sentence2)) # Output: True

sentence1, sentence2 = "a", "a b a"
print(areSentencesSimilar(sentence1, sentence2)) # Output: True

sentence1, sentence2 = "a b", "a c b"
print(areSentencesSimilar(sentence1, sentence2)) # Output: True

sentence1, sentence2 = "a", "b"
print(areSentencesSimilar(sentence1, sentence2)) # Output: False

sentence1, sentence2 = "a b c", "d e f"
print(areSentencesSimilar(sentence1, sentence2)) # Output: False

sentence1, sentence2 = "a b c", "a b d"
print(areSentencesSimilar(sentence1, sentence2)) # Output: False

sentence1, sentence2 = "a", ""
print(areSentencesSimilar(sentence1, sentence2)) # Output: True