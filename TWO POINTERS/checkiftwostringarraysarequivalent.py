# CHECK IF TWO STRING ARRAYS ARE EQUIVALENT

'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.
'''

def arrayStringsAreEqual(word1, word2):
    parray, pchar = 0
    qarray, qchar = 0
    
    while parray < len(word1) and qarray < len(word2):
        if word1[parray][pchar] != word2[qarray][qchar]:
            return False
        
        pchar += 1
        qchar += 1
        
        if pchar == len(word1[parray]):
            parray += 1
            pchar = 0
            
        if qchar == len(word2[qarray]):
            qarray += 1
            qchar = 0
            
    return parray == len(word1) and qarray == len(word2)

'''
Time Complexity: O(N + M)
Let N be the total number of characters in all strings of `word1` combined, and M be the total number of characters in all strings of `word2` combined.
The algorithm uses four pointers to iterate through the characters of the effective strings represented by `word1` and `word2`.
The `while` loop continues as long as there are characters to compare in both effective strings.
In each iteration, we perform a constant number of operations: character comparison, pointer increments, and boundary checks.
Each character from both `word1` and `word2` is visited at most once.
In the worst-case scenario (when the strings are equal or one is a long prefix of the other), we traverse all characters.
Therefore, the total time complexity is proportional to the sum of the total characters in both arrays, which is O(N + M).

Space Complexity: O(1)
The algorithm uses a constant amount of extra space.
It only requires four integer variables (`parray`, `pchar`, `qarray`, `qchar`) to act as pointers.
The space consumed by these variables does not depend on the size of the input arrays or the length of the strings.
The comparison is done in-place without creating new strings by concatenating the array elements.
Thus, the space complexity is O(1).
'''

# Test Cases
word1 = ["ab", "c"], word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1, word2)) # Output: True

word3 = ["a", "cb"], word4 = ["ab", "c"]
print(arrayStringsAreEqual(word3, word4)) # Output: False

word5 = ["abc", "d", "defg"], word6 = ["abcddefg"]
print(arrayStringsAreEqual(word5, word6)) # Output: True

word7 = ["a", "b", "c"], word8 = ["ab"]
print(arrayStringsAreEqual(word7, word8)) # Output: False

word9 = ["ab"], word10 = ["a"]
print(arrayStringsAreEqual(word9, word10)) # Output: False

word11 = ["a"], word12 = ["ab"]
print(arrayStringsAreEqual(word11, word12)) # Output: False

word13 = ["a", "", "b"], word14 = ["ab"]
print(arrayStringsAreEqual(word13, word14)) # Output: True

word15 = [], word16 = []
print(arrayStringsAreEqual(word15, word16)) # Output: True

word17 = ["a"], word18 = []
print(arrayStringsAreEqual(word17, word18)) # Output: False

word19 = ["leet", "code"], word20 = ["le", "et", "co", "de"]
print(arrayStringsAreEqual(word19, word20)) # Output: True