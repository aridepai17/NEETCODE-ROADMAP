# BACKSPACE STRING COMPARE

'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
'''

def backspaceCompare(s, t):
    p = len(s) - 1
    q = len(t) - 1
    
    while p >= 0 or q >= 0:
        backspaceS = 0
        while p >= 0:
            if s[p] == "#":
                backspaceS += 1
            elif backspaceS > 0:
                backspaceS -= 1
            else:
                break
            p -= 1
            
        backspaceQ = 0
        while q >= 0:
            if t[q] == "#":
                backspaceQ += 1
            elif backspaceQ > 0:
                backspaceQ -= 1
            else:
                break
            q -= 1
            
        if p >= 0 and q >= 0:
            if s[p] != t[q]:
                return False
        elif p >= 0 or q >= 0:
            return False
        
        p -= 1
        q -= 1
        
    return True

'''
Time Complexity: O(N + M)
Let N be the length of string `s` and M be the length of string `t`.
The algorithm uses two pointers, `p` and `q`, to traverse the strings from right to left.
Each pointer, `p` and `q`, moves from the end of its respective string towards the beginning.
In each iteration of the main `while` loop, the inner loops find the next valid character to compare by skipping over backspace characters and the characters they delete.
Each character in both strings is visited at most a constant number of times (once by the inner loop and once by the main loop's pointer decrement).
Therefore, the total time taken is proportional to the sum of the lengths of the two strings, resulting in a time complexity of O(N + M).

Space Complexity: O(1)
The algorithm uses a constant amount of extra space.
It only requires a few variables to store the pointers (`p`, `q`) and the backspace counters (`backspaceS`, `backspaceQ`).
The amount of space used does not scale with the size of the input strings `s` and `t`.
The comparison is performed in-place without creating any new data structures, so the space complexity is O(1).
'''

# Test Cases
s1 = "ab#c", t1 = "ad#c"
print(backspaceCompare(s1, t1)) # Output: True

s2 = "ab##", t2 = "c#d#"
print(backspaceCompare(s2, t2)) # Output: True

s3 = "a##c", t3 = "#a#c"
print(backspaceCompare(s3, t3)) # Output: True

s4 = "a#c", t4 = "b"
print(backspaceCompare(s4, t4)) # Output: False

s5 = "bxj##tw", t5 = "bxo#j##tw"
print(backspaceCompare(s5, t5)) # Output: True

s6 = "y#fo##f", t6 = "y#f#o##f"
print(backspaceCompare(s6, t6)) # Output: True

s7 = "", t7 = ""
print(backspaceCompare(s7, t7)) # Output: True

s8 = "a", t8 = "b"
print(backspaceCompare(s8, t8)) # Output: False

s9 = "##", t9 = "#"
print(backspaceCompare(s9, t9)) # Output: True

s10 = "abc###", t10 = ""
print(backspaceCompare(s10, t10)) # Output: True