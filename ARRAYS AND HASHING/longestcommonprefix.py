# LONGEST COMMON PREFIX

'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

def longestCommonPrefix(strs):
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        for word in strs[1:]:
            if i == len(word) or word[i] != char:
                return strs[0][:i]
            
    return strs[0]

# Test Cases
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))  # Output: "fl"

strs2 = ["dog","racecar","car"]
print(longestCommonPrefix(strs2))  # Output: ""

strs3 = ["interspecies","interstellar","interstate"]
print(longestCommonPrefix(strs3))  # Output: "inters"

strs4 = ["throne","throne"]
print(longestCommonPrefix(strs4))  # Output: "throne"

strs5 = ["a"]
print(longestCommonPrefix(strs5))  # Output: "a"

strs6 = ["", "b"]
print(longestCommonPrefix(strs6))  # Output: ""

strs7 = ["hello", "help", "helicopter"]
print(longestCommonPrefix(strs7))  # Output: "he"

strs8 = ["python", "programming", "practice"]
print(longestCommonPrefix(strs8))  # Output: "p"

strs9 = ["test", "testing", "tested"]
print(longestCommonPrefix(strs9))  # Output: "test"

strs10 = ["abc", "def", "ghi"]
print(longestCommonPrefix(strs10))  # Output: ""