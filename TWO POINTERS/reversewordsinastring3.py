# REVERSE WORDS IN STRING 3

'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

def reverseWords(s):
    s = list(s)
    n = len(s)
    left = 0
    
    for right in range(n + 1):
        if right == n or s[right] == " ":
            start = left 
            end = right - 1
            
            while start <= end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            
            left = right + 1
            
    return "".join(s)

'''
Time Complexity: O(n)
Let n be the length of the input string `s`.
The algorithm iterates through the string (or its list representation) a constant number of times.
1. Converting the string to a list `list(s)` takes O(n) time.
2. The main `for` loop runs from `0` to `n`, which is O(n).
3. The inner `while` loop reverses each word. Over the entire execution, each character is visited and swapped at most once by the `start` and `end` pointers. Thus, the total work for all reversals is O(n).
4. Joining the list back into a string `"".join(s)` also takes O(n) time.
Therefore, the total time complexity is linear with respect to the length of the string.

Space Complexity: O(n)
The space complexity is determined by the extra space used to store the list of characters.
Since strings are immutable in Python, the input string `s` is converted to a list of characters to allow for in-place reversal of words.
This list has a size of n, so it requires O(n) space.
The pointers and other variables use a constant amount of space, O(1).
Thus, the space complexity is O(n).
'''

# Test Cases
s1 = "Let's take LeetCode contest"
print(reverseWords(s1)) # Output: "s'teL ekat edoCteeL tsetnoc"

s2 = "God Ding"
print(reverseWords(s2)) # Output: "doG gniD"

s3 = "Hello World"
print(reverseWords(s3)) # Output: "olleH dlroW"

s4 = "a"
print(reverseWords(s4)) # Output: "a"

s5 = ""
print(reverseWords(s5)) # Output: ""

s6 = "  "
print(reverseWords(s6)) # Output: "  "

s7 = "  hello world  "
print(reverseWords(s7)) # Output: "  olleh dlrow  "

s8 = "Python is fun"
print(reverseWords(s8)) # Output: "nohtyP si nuf"

s9 = "123 456 789"
print(reverseWords(s9)) # Output: "321 654 987"

s10 = "single"
print(reverseWords(s10)) # Output: "elgnis"