# CHECK IF A STRING CONTAINS ALL BINARY CODES OF SIZE K

'''
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. 
Otherwise, return false.
'''

def hasAllCodes(s, k):
    seen = set()
    
    for i in range(len(s) - k + 1):
        seen.add(s[i : i + k])
        
    return len(seen) == 2 ** k

'''
Time Complexity: O(N * K)
- Let N be the length of the input string `s`.
- Let K be the given integer.
- The loop iterates `N - K + 1` times, which is approximately O(N) times.
- Inside the loop, `s[i : i + k]` creates a substring of length K. This operation takes O(K) time.
- Adding this substring to a set `seen` takes O(K) time on average, as hashing a string of length K takes O(K) time.
- Therefore, the total time complexity is O(N * K).

Space Complexity: O(2^K * K)
- The `seen` set stores all unique binary codes of length K found in `s`.
- In the worst case, the set will store `2^K` unique binary codes.
- Each binary code string has a length of K.
- Therefore, the total space required to store these strings in the set is O(2^K * K).
- This is because `2^K` strings, each of length `K`, are stored.
'''

# Test Cases
s1 = "00110110"
k1 = 2
print(hasAllCodes(s1, k1)) # Output: True

s2 = "0110"
k2 = 1
print(hasAllCodes(s2, k2)) # Output: True

s3 = "0110"
k3 = 2
print(hasAllCodes(s3, k3)) # Output: False

s4 = "000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
k4 = 3
print(hasAllCodes(s4, k4)) # Output: False

s5 = "01"
k5 = 1
print(hasAllCodes(s5, k5)) # Output: True

s6 = "00000000"
k6 = 3
print(hasAllCodes(s6, k6)) # Output: False

s7 = "11111111111111111111111111111111"
k7 = 5
print(hasAllCodes(s7, k7)) # Output: False

s8 = "11010111011100010110"
k8 = 4
print(hasAllCodes(s8, k8)) # Output: False

s9 = "0001100101111001"
k9 = 2
print(hasAllCodes(s9, k9)) # Output: True

s10 = "101011010110"
k10 = 3
print(hasAllCodes(s10, k10)) # Output: True