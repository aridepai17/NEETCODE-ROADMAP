# MAXIMUM NUMBER OF BALLOONS

'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed
'''

def maximumnumberofBalloons(text):
    balloonfreq = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': '1'}
    textfreq = {}
    
    for char in text:
        textfreq[char] = textfreq.get(char, 0) + 1
    
    result = float("inf")
    
    for char in balloonfreq:
        result = min(result, textfreq.get(char, 0) // balloonfreq[char])
        
    return result

'''
Time Complexity: O(N)
Let N be the length of the input string `text`.
- The first loop iterates through the `text` string once to build the `textfreq` frequency map. This takes O(N) time, as hash map operations (insertion and access) are O(1) on average.
- The second loop iterates through the keys of `balloonfreq`. The number of unique characters in "balloon" is constant (5: 'b', 'a', 'l', 'o', 'n'). Therefore, this loop runs a constant number of times.
- Inside the second loop, all operations (dictionary lookups, integer division, `min`) are O(1).
- The overall time complexity is dominated by the first loop, resulting in O(N).

Space Complexity: O(1)
- We use a hash map `textfreq` to store the frequency of characters in the input string.
- The number of unique characters is limited by the size of the character set (e.g., 26 for lowercase English letters). Therefore, the space required for `textfreq` is constant, O(1), as it cannot grow indefinitely with the input size N.
- The `balloonfreq` map also uses constant space.
- The other variables use constant space.
- Thus, the overall space complexity is O(1).
'''

# Test Cases
text1 = "nlaebolko"
print(maximumnumberofBalloons(text1)) # Output: 1

# Test Case 2: Multiple balloons can be formed
text2 = "loonbalxballpoon"
print(maximumnumberofBalloons(text2)) # Output: 2

# Test Case 3: Zero balloons due to missing characters
text3 = "leetcode"
print(maximumnumberofBalloons(text3)) # Output: 0

# Test Case 4: Zero balloons because 'l' is insufficient (only one 'l')
text4 = "balon"
print(maximumnumberofBalloons(text4)) # Output: 0

# Test Case 5: Empty string
text5 = ""
print(maximumnumberofBalloons(text5)) # Output: 0

# Test Case 6: String with no relevant characters
text6 = "xyz"
print(maximumnumberofBalloons(text6)) # Output: 0

# Test Case 7: Exactly enough characters for one balloon
text7 = "balloon"
print(maximumnumberofBalloons(text7)) # Output: 1

# Test Case 8: 'l' and 'o' are the limiting factors
text8 = "bbaallnnooo"
print(maximumnumberofBalloons(text8)) # Output: 1

# Test Case 9: A long string with many repeated "balloon"s
text9 = "balloonballoonballoonballoonballoon"
print(maximumnumberofBalloons(text9)) # Output: 5

# Test Case 10: Abundant characters but 'b' is the limiting factor
text10 = "baaaalllllooonnn"
print(maximumnumberofBalloons(text10)) # Output: 1