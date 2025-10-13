# NUMBER OF SUBSTRINGS CONTAINING ALL THREE CHARACTERS

'''
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.
'''

def numberOfSubstrings(s):
    hashMap = {}
    result = 0
    left = 0
    
    for right in range(len(s)):
        hashMap[s[right]] = hashMap.get(s[right], 0) + 1
        
        while len(hashMap) == 3:
            result += len(s) - right
            hashMap[s[left]] -= 1
            if hashMap[s[left]] == 0:
                hashMap.pop(s[left])
            left += 1
            
    return result

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach with two pointers, `left` and `right`.
The `right` pointer iterates through the string from the beginning to the end, which takes O(n) time, where n is the length of the string `s`.
The `left` pointer also moves from left to right. Over the entire execution of the function, the `left` pointer will not traverse the string more than once.
Since each character of the string is visited at most once by the `right` pointer and at most once by the `left` pointer, the total number of operations within the loops is proportional to n.
The operations on the `hashMap` (insertion, deletion, lookup) take O(1) time because the number of keys is at most 3.
Therefore, the overall time complexity is O(n).

Space Complexity: O(1)
The algorithm uses a `hashMap` to store the frequency of characters in the current window.
Since the input string `s` only consists of characters 'a', 'b', and 'c', the `hashMap` will store at most 3 key-value pairs.
The space required for the `hashMap` and other variables (`result`, `left`, `right`) is constant and does not depend on the length of the input string.
Thus, the space complexity is O(1).
'''

# Test Cases
s1 = 'abcabc'
print(numberOfSubstrings(s1)) # Output: 10

s2 = 'aaacb'
print(numberOfSubstrings(s2)) # Output: 3

s3 = 'abc'
print(numberOfSubstrings(s3)) # Output: 1

s4 = 'ababbc'
print(numberOfSubstrings(s4)) # Output: 3

s5 = 'bcaacb'
print(numberOfSubstrings(s5)) # Output: 7

s6 = 'ab'
print(numberOfSubstrings(s6)) # Output: 0

s7 = 'aaaaa'
print(numberOfSubstrings(s7)) # Output: 0

s8 = ''
print(numberOfSubstrings(s8)) # Output: 0

s9 = 'cbacba'
print(numberOfSubstrings(s9)) # Output: 10

s10 = 'cccaaabbb'
print(numberOfSubstrings(s10)) # Output: 9