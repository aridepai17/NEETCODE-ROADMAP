# ASSIGN COOKIES

'''
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.
'''

def assignCookies(g, s):
    g.sort()
    s.sort()
    
    left = 0
    right = 0
    
    while left < len(g) and right < len(s):
        if s[right] >= g[left]:
            left += 1
            right += 1
        else:
            right += 1
            
    return left

'''
Time Complexity: O(N log N + M log M)
Let N be the length of the greed factor array `g` and M be the length of the cookie size array `s`.
The dominant part of the algorithm is sorting the two input arrays. Sorting `g` takes O(N log N) time, and sorting `s` takes O(M log M) time.
After sorting, the algorithm uses a two-pointer approach to iterate through the arrays. The `while` loop runs at most N + M times, as in each iteration at least one of the pointers is incremented. This linear scan takes O(N + M) time.
Therefore, the total time complexity is O(N log N + M log M).

Space Complexity: O(1)
The algorithm sorts the input arrays in-place. The space required for the sorting depends on the implementation, but it's typically O(log N) or O(1) for in-place sorts.
Beyond the space used for sorting, the algorithm only uses a few variables to store pointers (`left`, `right`) and the count of content children. This requires a constant amount of extra space.
Thus, the space complexity is considered O(1), as it does not scale with the size of the input arrays.
'''

# Test Cases
g1 = [1, 2, 3], s1 = [1, 1]
print(assignCookies(g1, s1)) # Output: 1

g2 = [1, 2], s2 = [1, 2, 3]
print(assignCookies(g2, s2)) # Output: 2

g3 = [10, 9, 8, 7], s3 = [5, 6, 7, 8]
print(assignCookies(g3, s3)) # Output: 2

g4 = [], s4 = [1, 2, 3]
print(assignCookies(g4, s4)) # Output: 0

g5 = [1, 2, 3], s5 = []
print(assignCookies(g5, s5)) # Output: 0

g6 = [], s6 = []
print(assignCookies(g6, s6)) # Output: 0

g7 = [5, 6, 7], s7 = [1, 2, 3]
print(assignCookies(g7, s7)) # Output: 0

g8 = [1, 2], s8 = [10, 20]
print(assignCookies(g8, s8)) # Output: 2

g9 = [1, 1, 3], s9 = [1, 1, 2]
print(assignCookies(g9, s9)) # Output: 2

g10 = [3, 1, 4], s10 = [1, 5, 9, 2, 6]
print(assignCookies(g10, s10)) # Output: 3