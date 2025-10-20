# CRAWLER LOG FOLDER

'''
The Leetcode file system keeps a log each time some user performs a change folder operation.
The operations are described below:
"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
The file system starts in the main folder, then the operations in logs are performed.
Return the minimum number of operations needed to go back to the main folder after the change folder operations.
'''

def miniOperations(logs):
    total = 0
    
    for log in logs:
        if log == './':
            continue
        elif log == '../':
            if total > 0:
                total -= 1
        else:
            total += 1
    
    return total

'''
Time Complexity: O(n)
- The algorithm iterates through the `logs` array exactly once.
- Let `n` be the number of elements in the `logs` array.
- Inside the loop, all operations performed are constant time operations: string comparisons (`log == './'`, `log == '../'`) and integer arithmetic (`total -= 1`, `total += 1`).
- Since the loop runs `n` times and each iteration takes O(1) time, the total time complexity is O(n).

Space Complexity: O(1)
- The algorithm uses a single integer variable, `total`, to keep track of the current depth.
- The space required for this variable is constant and does not grow with the size of the input `logs` array.
- No other data structures that scale with the input size are used.
- Therefore, the auxiliary space complexity is O(1).
'''

# Test Cases
logs1 = ["d1/","d2/","../","d21/","./"]
print(miniOperations(logs1)) # Output: 2

logs2 = ["d1/","d2/","./","d3/","../","d31/"]
print(miniOperations(logs2)) # Output: 3

logs3 = ["d1/","../","../","../"]
print(miniOperations(logs3)) # Output: 0

logs4 = []
print(miniOperations(logs4)) # Output: 0

logs5 = ["./","./","./"]
print(miniOperations(logs5)) # Output: 0

logs6 = ["a/","b/","c/","../","../","../"]
print(miniOperations(logs6)) # Output: 0

logs7 = ["./","../","a/","b/","../","c/","./"]
print(miniOperations(logs7)) # Output: 2

logs8 = ["folder1/","longfoldername2/","../","another_folder_with_a_very_long_name/"]
print(miniOperations(logs8)) # Output: 2

logs9 = ["x/","y/","z/","w/"]
print(miniOperations(logs9)) # Output: 4

logs10 = ["../","../","../"]
print(miniOperations(logs10)) # Output: 0