# COUNT THE NUMBER OF CONSISTENT STRINGS

'''
You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
'''

# Solution 1: Using a HashSet
def countConsistentStrings1(allowed, words):
    allowed = set(allowed)
    count = len(words)
    
    for word in words:
        for char in word:
            if char not in allowed:
                count -= 1
                break
            
    return count

'''
Time Complexity: O(M + L)
Let M be the length of the `allowed` string.
Let L be the total number of characters across all strings in the `words` list.
- Building the `allowed` hash set takes O(M) time, as it requires iterating through each character of the `allowed` string.
- The code then iterates through each `word` in the `words` list. For each `word`, it iterates through its characters. The total number of character iterations across all words is L.
- Checking for a character's presence in the hash set (`char not in allowed`) is an O(1) operation on average.
- Therefore, the total time complexity is the sum of the time to build the set and the time to process all characters in `words`, which is O(M + L).

Space Complexity: O(M) or O(1)
- The primary extra space is used for the `allowed` hash set.
- The size of this set is equal to the number of unique characters in the `allowed` string, which is M. Thus, the space complexity is O(M).
- If the character set is fixed and of a constant size (e.g., 26 lowercase English letters), the space required for the set is bounded by that constant.
- In such a scenario, the space complexity is considered O(1), as it does not grow with the length of the input `allowed` string.
'''

# Solution 2: Using BitMask
def countConsistentStrings(allowed, words):
    bitMask = 0
    
    for char in allowed:
        bit = 1 << (ord(char) - ord('a'))
        bitMask = bitMask | bit
        
    result = len(words)
    
    for word in words:
        for char in word:
            bit = 1 << (ord(char) - ord('a'))
            if bitMask & bit == 0:
                result -= 1
                break
            
    return result

'''
Time Complexity: O(M + L)
Let M be the length of the `allowed` string.
Let L be the total number of characters across all strings in the `words` list.
- The first loop iterates through the `allowed` string to build the `bitMask`. This takes O(M) time, as each character is processed once with constant-time bitwise operations.
- The nested loops then iterate through each character of each word in the `words` list. The total number of character iterations is L.
- Inside the inner loop, checking if a character is allowed involves a few constant-time bitwise operations (`<<`, `&`).
- Therefore, the total time complexity is the sum of the time to build the bitmask and the time to check all words, which is O(M + L).

Space Complexity: O(1)
- The algorithm uses a fixed amount of extra space regardless of the input size.
- The `bitMask` is a single integer, which occupies constant space (e.g., 32 or 64 bits).
- Other variables like `result`, `bit`, and loop counters also use a constant amount of space.
- The space required does not scale with the length of `allowed` or the number of words.
- Thus, the space complexity is O(1).
'''

# Test Cases
allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed1, words1))  # Output: 2

allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]
print(countConsistentStrings(allowed2, words2))  # Output: 7

allowed3 = "c"
words3 = ["a","b","d"]
print(countConsistentStrings(allowed3, words3))  # Output: 0

allowed4 = "cad"
words4 = ["cc","acd","b","ba","bac","bad","ac","d"]
print(countConsistentStrings(allowed4, words4))  # Output: 5

allowed5 = "a"
words5 = []
print(countConsistentStrings(allowed5, words5))  # Output: 0

allowed6 = "z"
words6 = ["", "a", "z"]
print(countConsistentStrings(allowed6, words6))  # Output: 2

allowed7 = "abcdefghijklmnopqrstuvwxyz"
words7 = ["hello", "world", "leetcode"]
print(countConsistentStrings(allowed7, words7))  # Output: 3

allowed8 = "st"
words8 = ["test", "st", "string", "test"]
print(countConsistentStrings(allowed8, words8))  # Output: 3

allowed9 = "aabc"
words9 = ["a", "b", "c", "d", "ab", "ac", "bc", "abc"]
print(countConsistentStrings(allowed9, words9))  # Output: 7

allowed10 = "un"
words10 = ["u", "n", "un", "nun", "sun", "fun"]
print(countConsistentStrings(allowed10, words10))  # Output: 4