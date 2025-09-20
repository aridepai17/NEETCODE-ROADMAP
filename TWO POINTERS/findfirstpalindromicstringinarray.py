# FIND FIRST PALINDROMIC STRING IN THE ARRAY

'''
Given an array of strings words, return the first palindromic string in the array. 
If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.
'''

# Solution 1: Using Slicing
def firstPalindrome1(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

'''
Time Complexity: O(n * k)
Let n be the number of strings in the input array `words`, and k be the maximum length of a string in the array.
The algorithm iterates through each word in the `words` array. This takes O(n) iterations.
For each word, it checks if the word is a palindrome by comparing it with its reverse (`word == word[::-1]`).
Creating the reversed string `word[::-1]` takes O(k) time, and comparing the two strings also takes O(k) time.
In the worst-case scenario, we might have to check every word in the array.
Therefore, the total time complexity is O(n * k).

Space Complexity: O(k)
The space complexity is determined by the extra space used to check for a palindrome.
Inside the loop, the slicing operation `word[::-1]` creates a reversed copy of the current word.
This reversed string requires O(k) space, where k is the length of the word.
Since this is the maximum extra space used at any point in the algorithm, the space complexity is O(k).
'''

# Solution 2: Using Two Pointers
def firstPalindrome2(words):
    for word in words:
        left = 0
        right = len(word) - 1
        
        while word[left] == word[right]:
            if left >= right:
                return word
            left += 1
            right -= 1

    return ""

'''
Time Complexity: O(n * k)
Let n be the number of strings in the input array `words`, and k be the maximum length of a string in the array.
The algorithm iterates through each word in the `words` array, which takes O(n) time.
For each word, it uses a two-pointer approach to check if it's a palindrome. The `left` pointer starts at the beginning, and the `right` pointer starts at the end.
The pointers move towards each other, and in the worst case, they traverse half of the word. This check takes O(k) time for a word of length k.
In the worst-case scenario, the algorithm might have to check every word in the array.
Therefore, the total time complexity is O(n * k).

Space Complexity: O(1)
The algorithm uses a constant amount of extra space.
The two pointers, `left` and `right`, require O(1) space.
Unlike the slicing method, this approach does not create a reversed copy of the string. The palindrome check is performed in-place.
Thus, the space complexity is constant, O(1).
'''

# Test Cases
words1 = ["abc","car","ada","racecar","cool"]
print(firstPalindrome2(words1)) # Output: 1

words2 = ["notapalindrome","racecar"]
print(firstPalindrome2(words2)) # Output: "racecar"

words3 = ["def","ghi"]
print(firstPalindrome2(words3)) # Output: ""

words4 = []
print(firstPalindrome2(words4)) # Output: ""

words5 = ["", "a", "b"]
print(firstPalindrome2(words5)) # Output: ""

words6 = ["a", "b", "c"]
print(firstPalindrome2(words6)) # Output: "a"

words7 = ["hello", "world", "level"]
print(firstPalindrome2(words7)) # Output: "level"

words8 = ["racecar", "ada", "level"]
print(firstPalindrome2(words8)) # Output: "racecar"

words9 = ["Noon", "noon"]
print(firstPalindrome2(words9)) # Output: "noon"

words10 = ["12321", "12345"]
print(firstPalindrome2(words10)) # Output: "12321"