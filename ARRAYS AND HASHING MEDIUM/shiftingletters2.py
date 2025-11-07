# SHIFTING LETTERS 2

'''
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni].
For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). 
Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
Return the final string after all such shifts to s are applied.
'''

def shiftingLetters(s, shifts):
    n = len(s)
    s = list(s)
    delta = [0] * (n + 1)
    shift = 0
    
    for start, end, direction in shifts:
        if direction == 1:
            delta[start] += 1
            delta[end + 1] -= 1
        else:
            delta[start] -= 1
            delta[end + 1] += 1
            
    for i in range(n):
        shift += delta[i]
        s[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        
    return "".join(s)

'''
Time Complexity: O(N + M)
- Let N be the length of the string `s`.
- Let M be the number of shifts in the `shifts` array.
- The first loop iterates through all M shifts, performing O(1) operations for each shift. This takes O(M) time.
- The second loop iterates through all N characters of the string, performing O(1) operations for each character (addition, modulo, and character conversion). This takes O(N) time.
- Therefore, the overall time complexity is O(N + M).

Space Complexity: O(N)
- We create a list `s` from the input string, which takes O(N) space.
- We create a `delta` array of size N + 1, which takes O(N) space.
- Other variables (`shift`, loop counters) use constant space O(1).
- Therefore, the overall space complexity is O(N).
'''

# Test Cases
s1 = "dztz", shifts1 = [[0,0,0],[1,1,1]]
print(shiftingLetters(s1, shifts1)) # Output: "catz"

s2 = "abc", shifts2 = [[0,1,0],[1,2,1],[0,2,1]]
print(shiftingLetters(s2, shifts2)) # Output: "ace"

s3 = "aaa", shifts3 = [[0,2,1]]
print(shiftingLetters(s3, shifts3)) # Output: "bbb"

s4 = "zzz", shifts4 = [[0,2,0]]
print(shiftingLetters(s4, shifts4)) # Output: "yyy"

s5 = "hello", shifts5 = [[0,4,1],[2,2,0],[1,3,1]]
print(shiftingLetters(s5, shifts5)) # Output: "igopt"

s6 = "xyz", shifts6 = [[0,0,1],[1,1,1],[2,2,1]]
print(shiftingLetters(s6, shifts6)) # Output: "yza"

s7 = "abcdefg", shifts7 = [[0,6,1],[3,5,0],[1,4,1]]
print(shiftingLetters(s7, shifts7)) # Output: "bcdefgh"

s8 = "z", shifts8 = [[0,0,1]]
print(shiftingLetters(s8, shifts8)) # Output: "a"

s9 = "a", shifts9 = [[0,0,0]]
print(shiftingLetters(s9, shifts9)) # Output: "z"

s10 = "leetcode", shifts10 = [[0,7,1],[2,5,0],[4,7,1],[1,3,1]]
print(shiftingLetters(s10, shifts10)) # Output: "mffupgjf"