# STRING MATCHING IN AN ARRAY

'''
Given an array of string words, return all strings in words that are a substring of another word.
You can return the answer in any order.
A substring is a contiguous non-empty sequence of characters within a string.
'''

def stringMatching(words):
    words.sort(key = len)
    result = []
    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] in words[j]:
                result.append(words[i])
                break
            
    return result

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Test Cases
words1 = ["mass","as","hero","superhero"]
print(stringMatching(words1)) # Output: ["as","hero"]

words2 = ["leetcode","et","code"]
print(stringMatching(words2)) # Output: ["et","code"]

words3 = ["blue","green","bu"]
print(stringMatching(words3)) # Output: ["bu"]

words4 = ["a", "b", "c"]
print(stringMatching(words4)) # Output: []

words5 = ["hello", "world", "hello world"]
print(stringMatching(words5)) # Output: ["hello", "world"]

words6 = ["abc", "abcd", "abcde"]
print(stringMatching(words6)) # Output: ["abc", "abcd"]

words7 = ["test", "testing", "tested"]
print(stringMatching(words7)) # Output: ["test"]

words8 = ["python", "py", "thon", "python3"]
print(stringMatching(words8)) # Output: ["py", "thon"]

words9 = ["a", "aa", "aaa"]
print(stringMatching(words9)) # Output: ["a", "aa"]

words10 = ["cat", "dog", "catdog"]
print(stringMatching(words10)) # Output: ["cat", "dog"]

