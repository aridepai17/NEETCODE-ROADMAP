# SIMPLIFY PATH

'''
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.
The rules of a Unix-style file system are as follows:
A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. 
For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:
The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.
'''

def simplifyPath(path):
    stack = []
    current = ""
    
    for char in path + "/":
        if char == "/":
            if current == "..":
                if stack:
                    stack.pop()
            elif current != "" and current != ".":
                stack.append(current)
            current = ""
        else:
            current += char
            
    return "/" + "/".join(stack)

'''
Time Complexity: O(N), where N is the length of the input string `path`.
- We iterate through the input path once. The loop runs N+1 times.
- Inside the loop, we perform operations like string concatenation (`current += char`), string comparisons, and stack manipulations (`append`, `pop`).
- While string concatenation in a loop can be inefficient, each character from the original path is appended to `current` only once before `current` is either pushed to the stack or reset. Thus, the total work done for building all `current` strings across the entire loop is proportional to N.
- The `stack.append` and `stack.pop` operations take O(1) time on average.
- After the loop, `"/".join(stack)` creates the final string. This operation takes time proportional to the total length of the elements in the stack, which is at most O(N).
- Therefore, the overall time complexity is O(N).

Space Complexity: O(N)
- We use a `stack` to store the directory names of the canonical path. In the worst case, the stack can store components that, when combined, have a length proportional to N. For example, a path like "/a/b/c/..." with no ".." or "." components.
- The `current` string variable can also grow up to a length of N in the worst case (e.g., a path with no slashes after the initial one).
- The final output string also requires O(N) space.
- Thus, the space complexity is O(N).
'''

# Test Cases
path1 = "/home/"
print(simplifyPath(path1)) # Output: "/home"

path2 = "/../"
print(simplifyPath(path2)) # Output: "/"

path3 = "/home//foo/"
print(simplifyPath(path3)) # Output: "/home/foo"

path4 = "/a/./b/../../c/"
print(simplifyPath(path4)) # Output: "/c"

path5 = "/a/../../b/../c//.//"
print(simplifyPath(path5)) # Output: "/c"

path6 = "/a//b////c/d//././/.."
print(simplifyPath(path6)) # Output: "/a/b/c"

path7 = "/"
print(simplifyPath(path7)) # Output: "/"

path8 = "/..."
print(simplifyPath(path8)) # Output: "/..."

path9 = "/.hidden"
print(simplifyPath(path9)) # Output: "/.hidden"

path10 = "/a/b/c/."
print(simplifyPath(path10)) # Output: "/a/b/c"