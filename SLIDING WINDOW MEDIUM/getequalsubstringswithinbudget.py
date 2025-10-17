# GET EQUAL SUBSTRINGS WITHIN BUDGET

'''
You are given two strings s and t of the same length and an integer maxCost.
You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. 
If there is no substring from s that can be changed to its corresponding substring from t, return 0.
'''

def equalSubstring(s, t, maxCost):
    currentCost = 0
    result = 0
    left = 0
    
    for right in range(len(s)):
        currentCost += abs(ord(s[right] - ord(t[right])))
        while currentCost > maxCost:
            currentCost -= abs(ord(s[left] - ord(t[left])))
            left += 1
        result = max(result, right - left + 1)
        
    return result

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach.
- The `right` pointer iterates through the string from beginning to end, which takes O(n) steps, where n is the length of the strings s and t.
- The `left` pointer also moves from left to right. Although it's inside a `while` loop, it never moves backward.
- Each character in the string is visited by the `right` pointer once and by the `left` pointer at most once.
- The operations inside the loop are all constant time.
- Therefore, the total time complexity is O(n).

Space Complexity: O(1)
The algorithm uses a few variables (`currentCost`, `result`, `left`, `right`) to keep track of the current window's cost, the maximum length found so far, and the window boundaries.
- The space required for these variables is constant and does not depend on the size of the input strings.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
s1 = "abcd", t1 = "bcdf", maxCost1 = 3
print(equalSubstring(s1, t1, maxCost1)) # Output: 3

s2 = "krpgjbjjsp", t2 = "krpgjbjjsp", maxCost2 = 0
print(equalSubstring(s2, t2, maxCost2)) # Output: 10

s3 = "abc", t3 = "xyz", maxCost3 = 2
print(equalSubstring(s3, t3, maxCost3)) # Output: 0

s4 = "abcd", t4 = "bcdf", maxCost4 = 10
print(equalSubstring(s4, t4, maxCost4)) # Output: 4

s5 = "a", t5 = "b", maxCost5 = 0
print(equalSubstring(s5, t5, maxCost5)) # Output: 0

s6 = "a", t6 = "b", maxCost6 = 1
print(equalSubstring(s6, t6, maxCost6)) # Output: 1

s7 = "abcdef", t7 = "zyxwvu", maxCost7 = 1000
print(equalSubstring(s7, t7, maxCost7)) # Output: 6

s8 = "krrgw", t8 = "zjxss", maxCost8 = 19
print(equalSubstring(s8, t8, maxCost8)) # Output: 2

s9 = "fkfnkrfunni", t9 = "jjeftrmnvvj", maxCost9 = 40
print(equalSubstring(s9, t9, maxCost9)) # Output: 8

s10 = "t", t10 = "t", maxCost10 = 100
print(equalSubstring(s10, t10, maxCost10)) # Output: 1