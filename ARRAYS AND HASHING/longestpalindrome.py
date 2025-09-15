# LONGEST PALINDROME

'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
A palindrome is a string that reads the same forward and backward.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.
'''
# Solution 1: Using A HashMap
def longestPalindrome1(s):
    hashMap = {}
    result = 0
    
    for char in s:
        hashMap[char] = hashMap.get(char, 0) + 1       
        if hashMap[char] % 2 == 0:
            result += 2
    
    for value in hashMap.values():
        if value % 2 == 1:
            result += 1
            break
        
    return result

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The first loop iterates through each character of the string `s` once, which takes O(N) time.
- Inside this loop, hash map operations (insertion, lookup) take average O(1) time.
- The second loop iterates through the values of the hash map. The number of unique characters (U) is at most N and is often bounded by the size of the character set (e.g., 52 for English letters). This loop takes O(U) time.
- Therefore, the total time complexity is O(N + U), which simplifies to O(N) because U <= N.

Space Complexity: O(U) or O(1)
- U is the number of unique characters in the string `s`.
- We use a hash map to store the frequency of each character.
- The space required for the hash map is proportional to the number of unique characters.
- If the character set is fixed and of a constant size (e.g., ASCII or English alphabet), the space complexity can be considered O(1).
- Otherwise, in the worst case where all characters are unique, the space complexity is O(U), which can be up to O(N).
'''

# Solution 2: Using a HashSet
def longestPalindrome2(s):
    hashSet = set()
    result = 0
    
    for char in s:
        if char in hashSet:
            hashSet.remove(char)
            result += 2
        else:
            hashSet.add(char)
            
    if hashSet:
        result += 1
        
    return result

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The code iterates through each character of the string `s` once, which takes O(N) time.
- Inside the loop, hash set operations (add, remove, check for existence) take average O(1) time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(U) or O(1)
- U is the number of unique characters in the string `s`.
- We use a hash set to store characters that have appeared an odd number of times.
- The space required for the hash set is proportional to the number of unique characters.
- If the character set is fixed and of a constant size (e.g., ASCII or English alphabet), the space complexity can be considered O(1).
- Otherwise, in the worst case where all characters are unique, the space complexity is O(U), which can be up to O(N).
'''

# Test Cases
s1 = "abccccdd"
print(longestPalindrome2(s1)) # Output: 7

s2 = "a"
print(longestPalindrome2(s2)) # Output: 1

s3 = "bb"
print(longestPalindrome2(s3)) # Output: 2

s4 = "ccc"
print(longestPalindrome2(s4)) # Output: 3

s5 = "bananas"
print(longestPalindrome2(s5)) # Output: 5

s6 = "racecar"
print(longestPalindrome2(s6)) # Output: 7

s7 = ""
print(longestPalindrome2(s7)) # Output: 0

s8 = "abcdefg"
print(longestPalindrome2(s8)) # Output: 1

s9 = "Aa"
print(longestPalindrome2(s9)) # Output: 1

s10 = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendure"
print(longestPalindrome2(s10)) # Output: 65