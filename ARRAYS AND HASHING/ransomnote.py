# RANSOM NOTE 

'''
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
'''

# Solution 1: Using a Set and count method
def canConstruct1(ransomNote, magazine):
    ransom = set(ransomNote)
    
    for i in ransom:
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True

'''
Time Complexity: O(R * (R + M))
Let R be the length of the `ransomNote` string.
Let M be the length of the `magazine` string.
Let U be the number of unique characters in `ransomNote`.
- Creating the set `ransom` from `ransomNote` takes O(R) time.
- The algorithm then iterates through each unique character in the `ransom` set. The number of unique characters is U.
- Inside the loop, `ransomNote.count(i)` is called, which takes O(R) time as it has to scan the entire `ransomNote` string.
- Similarly, `magazine.count(i)` is called, which takes O(M) time.
- The total time for the loop is U * (O(R) + O(M)).
- Since U can be at most R in the worst case (if all characters in `ransomNote` are unique), the overall time complexity becomes O(R) + O(R * (R + M)), which simplifies to O(R * (R + M)).
- This approach is inefficient due to the repeated calls to the `count()` method inside a loop.

Space Complexity: O(U) or O(1)
- The primary extra space is used for the `ransom` set, which stores the unique characters from `ransomNote`.
- The size of this set is U, the number of unique characters. Therefore, the space complexity is O(U).
- If the character set is fixed and of a constant size (e.g., 26 for lowercase English letters), the space required for the set is bounded by that constant.
- In such a scenario, the space complexity is considered O(1), as it does not grow with the length of the input `ransomNote` string.
'''

# Solution 2: Using HashMap
def canConstruct2(ransomNote, magazine):
    freq = {}
    
    for char in magazine:
        freq[char] = freq.get(char, 0) + 1
        
    for char in ransomNote:
        if char not in freq:
            return False
        elif freq[char] == 1:
            del freq[char]
        else:
            freq[char] -= 1
            
    return True

'''
Time Complexity: O(M + R)
Let M be the length of the `magazine` string.
Let R be the length of the `ransomNote` string.
- The first loop iterates through the `magazine` string to build a frequency map (`freq`). This involves M insertions or updates into the hash map, where each operation takes O(1) on average. This step takes O(M) time.
- The second loop iterates through the `ransomNote` string. For each character, it performs a lookup and a potential update or deletion in the hash map, all of which are O(1) operations on average. This step takes O(R) time.
- The overall time complexity is the sum of the time to process both strings, resulting in O(M + R).

Space Complexity: O(U) or O(1)
- The algorithm uses a hash map (`freq`) to store the character counts from the `magazine` string.
- Let U be the number of unique characters in `magazine`. The space required for the hash map is proportional to U. Therefore, the space complexity is O(U).
- If the character set is fixed and of a constant size (e.g., 26 for lowercase English letters), the size of the hash map is bounded by that constant.
- In such a scenario, the space complexity is considered O(1), as the extra space used does not scale with the size of the input strings.
'''

# Solution 3: Using Single Array approach
def canConstruct3(ransomNote, magazine):
    freq = [0] * 26
    
    for char in magazine:
        freq[ord(char) - ord('a')] += 1
        
    for char in ransomNote:
        index = ord(char) - ord('a')
            
        if freq[index] <= 0:
            return False
        freq[index] -= 1
            
    return True

'''
Time Complexity: O(M + R)
Let M be the length of the `magazine` string.
Let R be the length of the `ransomNote` string.
- The first loop iterates through the `magazine` string to build a frequency array (`freq`). This involves M increments in the array, where each operation takes O(1) time. This step takes O(M) time.
- The second loop iterates through the `ransomNote` string. For each character, it performs a lookup and a decrement in the array, both of which are O(1) operations. This step takes O(R) time.
- The overall time complexity is the sum of the time to process both strings, resulting in O(M + R).

Space Complexity: O(1)
- The algorithm uses an integer array (`freq`) of a fixed size, 26, to store the character counts from the `magazine` string.
- The space required for this array is constant and does not scale with the size of the input strings.
- Therefore, the space complexity is O(1).
'''

# Test Cases
ransomNote1 = "a", magazine1 = "b"
print(canConstruct3(ransomNote1, magazine1))  # Output: False

ransomNote2 = "aa"
magazine2 = "ab"
print(canConstruct3(ransomNote2, magazine2))  # Output: False

ransomNote3 = "aa"
magazine3 = "aab"
print(canConstruct3(ransomNote3, magazine3))  # Output: True

ransomNote4 = "bg"
magazine4 = "efjbdfbdgfjhhaiigfhba"
print(canConstruct3(ransomNote4, magazine4))  # Output: True

ransomNote5 = "fihjjj"
magazine5 = "ihjfff"
print(canConstruct3(ransomNote5, magazine5))  # Output: False

ransomNote6 = ""
magazine6 = "a"
print(canConstruct3(ransomNote6, magazine6))  # Output: True

ransomNote7 = "a"
magazine7 = ""
print(canConstruct3(ransomNote7, magazine7))  # Output: False

ransomNote8 = "leetcode"
magazine8 = "leetcoded"
print(canConstruct3(ransomNote8, magazine8))  # Output: True

ransomNote9 = "apple"
magazine9 = "pale"
print(canConstruct3(ransomNote9, magazine9))  # Output: False

ransomNote10 = "aabbc"
magazine10 = "abcabc"
print(canConstruct3(ransomNote10, magazine10))  # Output: True