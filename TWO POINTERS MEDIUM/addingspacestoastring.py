# ADDING SPACES TO A STRING

'''
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. 
Each space should be inserted before the character at the given index.
For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. 
Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.
'''

def addSpaces(s, spaces):
    left = 0
    right = 0
    result = []
    
    while left < len(s) and right < len(spaces):
        if left < spaces[right]:
            result.append(s[left])
            left += 1
        else:
            result.append(" ")
            right += 1
            
    if left < len(s):
        result.append(s[left:])
        
    return "".join(result)

'''
Time Complexity: O(N + M)
Let N be the length of the input string `s`, and M be the length of the `spaces` array.
The algorithm uses a two-pointer approach to build the result. The `left` pointer iterates through the string `s`, and the `right` pointer iterates through the `spaces` array.
In each step of the `while` loop, we either append a character from `s` and increment `left`, or we append a space and increment `right`.
This process continues until one of the pointers has traversed its entire sequence.
The `left` pointer will traverse all N characters of `s`, and the `right` pointer will traverse all M indices in `spaces`. Each character and space is appended to the `result` list once. This build-up phase takes O(N + M) time.
The final `"".join(result)` operation concatenates the elements of the `result` list. The size of this list is N + M. The join operation takes time proportional to the final string's length, which is also O(N + M).
Therefore, the total time complexity is O(N + M).

Space Complexity: O(N + M)
The space complexity is determined by the storage required for the `result` list.
This list holds all N characters from the original string `s` plus the M spaces that are added.
The total number of elements in the `result` list will be N + M.
Thus, the space required for the `result` list is O(N + M).
The final output string also requires O(N + M) space, but typically the space for the output is not counted against the algorithm's space complexity. However, the intermediate `result` list already establishes the O(N + M) space requirement.
Other variables like `left` and `right` use constant O(1) space.
'''

# Test Cases
s1 = "LeetcodeHelpsMeLearn", spaces1 = [8, 13, 15]
print(addSpaces(s1, spaces1)) # Output: "LeetCode Helps Me Learn"

s2 = "EnjoyYourCoffee", spaces2 = [5, 9]
print(addSpaces(s2, spaces2)) # Output: "Enjoy Your Coffee"

s3 = "iLoveCoding", spaces3 = [1, 5]
print(addSpaces(s3, spaces3)) # Output: "i Love Coding"

s4 = "HelloWorld", spaces4 = []
print(addSpaces(s4, spaces4)) # Output: "HelloWorld"

s5 = "a", spaces5 = [0]
print(addSpaces(s5, spaces5)) # Output: " a"

s6 = "abc", spaces6 = [0, 1, 2]
print(addSpaces(s6, spaces6)) # Output: " a b c"

s7 = "spacing", spaces7 = [0, 1, 2, 3, 4, 5, 6]
print(addSpaces(s7, spaces7)) # Output: " s p a c i n g"

s8 = "Python", spaces8 = [6]
print(addSpaces(s8, spaces8)) # Output: "Python"

s9 = "", spaces9 = []
print(addSpaces(s9, spaces9)) # Output: ""

s10 = "test", spaces10 = [0, 0, 0]
print(addSpaces(s10, spaces10)) # Output: "   test"