# REMOVE ALL ADJACENT DUPLICATES IN STRING 2

'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
'''

def removeDuplicates(s, k):
    stack = []
    
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])
        
        if stack[-1][1] == k:
            stack.pop()
            
    result = ""
    for char, count in stack:
        result += char * count
        
    return result

'''
Time Complexity: O(N), where N is the length of the input string s.
- We iterate through the input string s once.
- For each character, we perform O(1) operations: accessing the top of the stack, appending to it, or popping from it.
- After iterating through the entire string, we build the final result string. This takes time proportional to the length of the result string, which is at most N.
- Therefore, the total time complexity is dominated by the single pass through the input string, making it O(N).

Space Complexity: O(N)
- We use a stack to store pairs of [character, count].
- In the worst-case scenario, no duplicates are removed (e.g., "abcde" with k=2), and the stack will store an entry for each character in the input string.
- Thus, the space required by the stack is proportional to the length of the input string, making the space complexity O(N).
'''

# Test Cases
s1 = "abcd", k1 = 2
print(removeDuplicates(s1, k1)) # Output: "abcd"

s2 = "deeedbbcccbdaa", k2 = 3
print(removeDuplicates(s2, k2)) # Output: "aa"

s3 = "pbbcggttciiippooaais", k3 = 2
print(removeDuplicates(s3, k3)) # Output: "pcciiiis"

s4 = "abccba", k4 = 2
print(removeDuplicates(s4, k4)) # Output: ""

s5 = "aaaaa", k5 = 2
print(removeDuplicates(s5, k5)) # Output: "a"

s6 = "", k6 = 5
print(removeDuplicates(s6, k6)) # Output: ""

s7 = "zzzaaccc", k7 = 3
print(removeDuplicates(s7, k7)) # Output: "aa"

s8 = "abacaba", k8 = 2
print(removeDuplicates(s8, k8)) # Output: "abacaba"

s9 = "mississippi", k9 = 2
print(removeDuplicates(s9, k9)) # Output: "m"

s10 = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", k10 = 4
print(removeDuplicates(s10, k10)) # Output: "ybth"