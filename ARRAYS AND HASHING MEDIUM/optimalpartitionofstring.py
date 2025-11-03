# OPTIMAL PARTITION OF STRING

'''
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
That is, no letter appears in a single substring more than once.
Return the minimum number of substrings in such a partition.
Note that each character should belong to exactly one substring in a partition.
'''

def optimalPartition(s):
    hashSet = set()
    result = 1
    
    for char in s:
        if char in hashSet:
            result += 1
            hashSet = set()
            hashSet.add(char)
        hashSet.add(char)
        
    return result

'''
Time Complexity: O(N)
Let N be the length of the input string `s`.
- The algorithm iterates through the string `s` once with a single `for` loop, processing each character exactly once.
- Inside the loop, all operations are constant time:
  - Checking if a character exists in the hash set (`char in hashSet`) is O(1) on average.
  - Adding a character to the hash set (`hashSet.add(char)`) is O(1) on average.
  - Creating a new empty set (`hashSet = set()`) is O(1).
- Therefore, the total time complexity is O(N).

Space Complexity: O(min(N, K))
- The algorithm uses a hash set `hashSet` to store characters from the current substring.
- In the worst case, if all characters in the string are unique, the set will grow to contain all N characters before the loop ends.
- However, the maximum size of the set is limited by the size of the character set K (e.g., 26 for lowercase English letters, 128 for ASCII).
- Therefore, the space complexity is O(min(N, K)).
- If the character set is fixed and constant (e.g., lowercase English letters), this simplifies to O(1).
'''

# Test Cases
s1 = "ssssss"
print(optimalPartition(s1)) # Output: 6

s2 = "abacaba"
print(optimalPartition(s2)) # Output: 4

s3 = "abcabc"
print(optimalPartition(s3)) # Output: 2

s4 = "a"
print(optimalPartition(s4)) # Output: 1

s5 = "abcdefghij"
print(optimalPartition(s5)) # Output: 1

s6 = "aabbcc"
print(optimalPartition(s6)) # Output: 3

s7 = "abacabad"
print(optimalPartition(s7)) # Output: 4

s8 = "aaabbbccc"
print(optimalPartition(s8)) # Output: 3

s9 = "abcdefabcdef"
print(optimalPartition(s9)) # Output: 2

s10 = "xyza"
print(optimalPartition(s10)) # Output: 1