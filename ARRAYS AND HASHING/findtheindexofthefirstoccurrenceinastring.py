# FIND THE INDEX OF THE FIRST OCCURRENCE IN A STRING

'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def strStr(haystack, needle):
    if needle == "":
        return 0
    
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i: i + len(needle)] == needle:
            return i
        
    return -1

'''
Time Complexity: O((N-M) * M)
Let N be the length of the `haystack` string and M be the length of the `needle` string.
- The `for` loop iterates from `i = 0` to `N - M`. This gives us `N - M + 1` iterations.
- Inside the loop, a substring of `haystack` of length M is created using slicing: `haystack[i: i + len(needle)]`. This slicing operation takes O(M) time.
- This new substring is then compared to the `needle` string. This comparison also takes O(M) time.
- Therefore, the total time complexity is the product of the number of iterations and the work done in each iteration: O((N - M) * M).

Space Complexity: O(M)
- The algorithm uses a constant amount of space for variables like the loop counter `i`.
- However, inside the loop, the string slicing operation `haystack[i: i + len(needle)]` creates a new temporary substring of length M.
- This requires O(M) auxiliary space to hold the sliced string for comparison.
- Thus, the space complexity is dominated by the space needed for this temporary substring, resulting in O(M).
'''

# Test Cases
haystack1 = "sadbutsad", needle1 = "sad"
print(strStr(haystack1, needle1)) # Output: 0

haystack2 = "leetcode", needle2 = "leeto"
print(strStr(haystack2, needle2)) # Output: -1

haystack3 = "hello", needle3 = "ll"
print(strStr(haystack3, needle3)) # Output: 2

haystack4 = "aaaaa", needle4 = "bba"
print(strStr(haystack4, needle4)) # Output: -1

haystack5 = "mississippi", needle5 = "issip"
print(strStr(haystack5, needle5)) # Output: 4

haystack6 = "a", needle6 = "a"
print(strStr(haystack6, needle6)) # Output: 0

haystack7 = "abc", needle7 = ""
print(strStr(haystack7, needle7)) # Output: 0

haystack8 = "", needle8 = "a"
print(strStr(haystack8, needle8)) # Output: -1

haystack9 = "", needle9 = ""
print(strStr(haystack9, needle9)) # Output: 0

haystack10 = "bbaa", needle10 = "a"
print(strStr(haystack10, needle10)) # Output: 2