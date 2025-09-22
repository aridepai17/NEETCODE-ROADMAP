# STRING COMPRESSION

'''
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.
Note: The characters in the array beyond the returned length do not matter and should be ignored.
'''

def stringCompress(chars):
    read = 0
    write = 0
    n = len(chars)
    
    while read < n:
        currentChar = chars[read]
        groupStart = read
        
        while read < n and chars[read] == currentChar:
            read += 1
            
        groupLength = read - groupStart
        
        chars[write] = currentChar
        write += 1
        
        if groupLength > 1:
            for digit in str(groupLength):
                chars[write] = digit
                write += 1
                
    return write

'''
Time Complexity: O(N)
Let N be the length of the input array `chars`.
The algorithm uses a `read` pointer that traverses the entire array from left to right exactly once.
For each group of consecutive characters, we perform a constant number of operations to write the character and its count.
The `write` pointer also moves from left to right and never exceeds N.
Although converting the group length to a string and iterating through its digits takes time proportional to the number of digits (logarithmic in the group length), this operation is part of the single pass.
Each character is read once by the `read` pointer. Therefore, the total time complexity is dominated by this single pass, resulting in O(N).

Space Complexity: O(1)
The algorithm modifies the input array in-place, as required.
The extra space used is for a fixed number of variables (`read`, `write`, `n`, `currentChar`, `groupStart`, `groupLength`), which do not depend on the size of the input array.
The space required to store the string representation of `groupLength` (e.g., `str(groupLength)`) is `O(log k)` where `k` is the group length. Since `k <= N`, the maximum space for this temporary string is `O(log N)`.
In the context of algorithm analysis, space that is logarithmic with respect to the input size is often considered negligible and is grouped under the O(1) or constant space complexity category, especially when the primary goal is to avoid using space proportional to the input size (O(N)). 
Thus, the space complexity is considered O(1).
'''

# Test Cases
chars1 = ["a","a","b","b","c","c","c"]
print(stringCompress(chars1)) # Output: 6

chars2 = ["a"]
print(stringCompress(chars2)) # Output: 1

chars3 = ["a","b","c"]
print(stringCompress(chars3)) # Output: 3

chars4 = ["a","a","a","a","a","a"]
print(stringCompress(chars4)) # Output: 2

chars5 = ["a","a","a","b","b","a","a"]
print(stringCompress(chars5)) # Output: 6

chars6 = ["o","o","o","o","o","o","o","o","o","o"]
print(stringCompress(chars6)) # Output: 3

chars7 = []
print(stringCompress(chars7)) # Output: 0

chars8 = ["z"] * 15
print(stringCompress(chars8)) # Output: 3

chars9 = ["a"] + ["b"] * 12
print(stringCompress(chars9)) # Output: 4

chars10 = ["a"]*2 + ["b"]*10 + ["c"]*3
print(stringCompress(chars10)) # Output: 7