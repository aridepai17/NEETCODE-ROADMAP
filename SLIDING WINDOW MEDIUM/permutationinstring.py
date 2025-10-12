# PERMUTATION IN STRING

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
'''

def permutationString(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1Count = [0] * 26
    s2Count = [0] * 26
    
    for i in range(len(s1)):
        s1Count(ord(s1[i]) - ord('a')) += 1
        s2Count(ord(s2[i]) - ord('a')) += 1
        
    if s1Count == s2Count:
        return True
    
    for i in range(len(s1), len(s2)):
        s2Count[ord(s2[i - len(s1)]) - ord('a')] -= 1
        s2Count[ord(s2[i]) - ord('a')] += 1
        if s1Count == s2Count:
            return True
        
    return False

'''
Time Complexity: O(len(s2))
Let n be the length of s1 and m be the length of s2.
The algorithm uses a sliding window of size n over the string s2.
First, it takes O(n) to build the initial frequency map for s1 and the first window of s2.
Then, the window slides m - n times across the rest of s2. In each step, updating the window's frequency map and comparing it to s1's map takes constant time, O(1), because the alphabet size is fixed at 26.
The total time complexity is O(n) for the setup plus O(m - n) for sliding, which simplifies to O(m).

Space Complexity: O(1)
The algorithm uses two arrays, `s1Count` and `s2Count`, to store character frequencies.
Since the alphabet is limited to lowercase English letters, these arrays have a fixed size of 26.
The space required does not scale with the length of the input strings, so the space complexity is constant, O(1).
'''

# Test Cases
s1 = "ab", s2 = "eidbaooo"
print(permutationString(s1, s2)) # Output; True

s1, s2 = "ab", "eidboaoo"
print(permutationString(s1, s2)) # Output: False

s1, s2 = "ac", "dca"
print(permutationString(s1, s2)) # Output: True

s1, s2 = "tr", "trace"
print(permutationString(s1, s2)) # Output: True

s1, s2 = "apple", "appeal"
print(permutationString(s1, s2)) # Output: False

s1, s2 = "a", "b"
print(permutationString(s1, s2)) # Output: False

s1, s2 = "b", "b"
print(permutationString(s1, s2)) # Output: True

s1, s2 = "oop", "poop"
print(permutationString(s1, s2)) # Output: True

s1, s2 = "abc", "abxacybz"
print(permutationString(s1, s2)) # Output: False

s1, s2 = "xyz", "afdgzyxks"
print(permutationString(s1, s2)) # Output: True