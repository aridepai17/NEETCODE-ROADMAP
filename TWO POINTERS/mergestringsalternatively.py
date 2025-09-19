# MERGE STRINGS ALTERNATIVELY

'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
'''

def mergeAlternatively(word1, word2):
    mergedString = []
    left = 0
    right = 0
    
    while left < len(word1) and right < len(word2):
        mergedString.append(word1[left])
        mergedString.append(word2[right])
        
        left += 1
        right += 1
        
    mergedString.append(word1[left:])
    mergedString.append(word2[right:])
    
    return "".join(mergedString)

'''
Time Complexity: O(N + M)
Let N be the length of `word1` and M be the length of `word2`.
The `while` loop runs `min(N, M)` times, iterating through the shorter of the two strings.
After the loop, the remaining parts of the longer string are sliced and appended. Slicing takes time proportional to the length of the slice.
The `"".join(mergedString)` operation at the end creates the final string. This operation takes time proportional to the total length of the strings to be joined, which is N + M.
Since all operations combined process each character from both strings once, the total time complexity is linear with respect to the sum of the lengths of the input strings, O(N + M).

Space Complexity: O(N + M)
A list `mergedString` is used to build the result.
In the worst case, this list will store all characters from both `word1` and `word2`.
The final `"".join()` operation also creates a new string of length N + M.
Therefore, the space required is proportional to the sum of the lengths of the input strings, making the space complexity O(N + M).
'''

# Test Cases
word1 = "abc", word2 = "pqr"
print(mergeAlternatively(word1, word2)) # Output: "apbqcr"

word1 = "ab"
word2 = "pqrs"
print(mergeAlternatively(word1, word2)) # Output: "apbqrs"

word1 = "abcd"
word2 = "pq"
print(mergeAlternatively(word1, word2)) # Output: "apbqcd"

word1 = ""
word2 = "pqr"
print(mergeAlternatively(word1, word2)) # Output: "pqr"

word1 = "abc"
word2 = ""
print(mergeAlternatively(word1, word2)) # Output: "abc"

word1 = ""
word2 = ""
print(mergeAlternatively(word1, word2)) # Output: ""

word1 = "a"
word2 = "p"
print(mergeAlternatively(word1, word2)) # Output: "ap"

word1 = "z"
word2 = "abcdef"
print(mergeAlternatively(word1, word2)) # Output: "zabcdef"

word1 = "123"
word2 = "456"
print(mergeAlternatively(word1, word2)) # Output: "142536"

word1 = "ace"
word2 = "bdfg"
print(mergeAlternatively(word1, word2)) # Output: "abcdefg"