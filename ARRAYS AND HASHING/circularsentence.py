# CIRCULAR SENTENCE

'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. 
Uppercase and lowercase English letters are considered different.
A sentence is circular if:
- The last character of each word in the sentence is equal to the first character of its next word.
- The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.
Given a string sentence, return true if it is circular. Otherwise, return false.
'''

# Solution 1: Using Brute Force 
def isCircular1(sentence):
    words = sentence.split()
    
    for i in range(len(words)):
        if words[i][0] != words[i - 1][-1]:
            return False
    return True

'''
Time Complexity: O(N)
- Let N be the length of the input `sentence` string.
- The `sentence.split()` method takes O(N) time to iterate through the string and create a list of words.
- The loop iterates through the list of words. Let W be the number of words. The loop runs W times.
- Inside the loop, accessing characters at the beginning and end of words (`words[i][0]` and `words[i-1][-1]`) are O(1) operations.
- The total time complexity is O(N) for splitting + O(W) for the loop. Since W is at most N, the overall complexity is dominated by the split operation, resulting in O(N).

Space Complexity: O(N)
- The `sentence.split()` method creates a new list of words.
- The total space required to store these words is proportional to the length of the original sentence, N.
- Therefore, the space complexity is O(N).
'''

# Solution 2: Using One Pointer
def isCircular2(sentence):
    for i in range(len(sentence)):
        if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
            return False
    return sentence[0] == sentence[-1]

'''
Time Complexity: O(N)
- Let N be the length of the input `sentence` string.
- The function iterates through the entire string once using a for loop, which takes O(N) time.
- Inside the loop, all operations (character access and comparison) are O(1).
- The final check `sentence[0] == sentence[-1]` is also an O(1) operation.
- Thus, the overall time complexity is O(N).

Space Complexity: O(1)
- The function uses only a few variables to keep track of the index (`i`).
- It does not create any new data structures that scale with the size of the input sentence.
- Therefore, the space complexity is O(1) (constant space).
'''
# Test Cases
sentence1 = "leetcode exercises sound delightful"
print(isCircular1(sentence1)) # Output: True

sentence2 = "eetcode"
print(isCircular1(sentence2)) # Output: True

sentence3 = "Leetcode"
print(isCircular1(sentence3)) # Output: False

sentence4 = "Leetcode is cool"
print(isCircular1(sentence4)) # Output: False

sentence5 = "happy Leetcode"
print(isCircular1(sentence5)) # Output: False

sentence6 = "ab ba"
print(isCircular1(sentence6)) # Output: True

sentence7 = "ab bc ca"
print(isCircular1(sentence7)) # Output: True

sentence8 = "I like Leetcode"
print(isCircular1(sentence8)) # Output: False

sentence9 = "leetcode eats soul"
print(isCircular1(sentence9)) # Output: True

sentence10 = "eager rabbits sprint"
print(isCircular1(sentence10)) # Output: False