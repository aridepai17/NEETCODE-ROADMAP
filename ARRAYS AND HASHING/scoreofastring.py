# SCORE OF A STRING

'''
You are given a string s. 
The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
Return the score of s.
'''

def scoreOfString(s):
    score = 0
    
    for i in range(1, len(s)):
        score += abs(ord(s[i]) - ord(s[i - 1]))
        
    return score

# Test Cases
s1 = "zaz"
print(scoreOfString(s1)) # Output: 50

s2 = "hello"
print(f"Score of '{s2}': {scoreOfString(s2)}") # Expected: 13

s3 = "abc"
print(f"Score of '{s3}': {scoreOfString(s3)}") # Expected: 2

s4 = "xyz"
print(f"Score of '{s4}': {scoreOfString(s4)}") # Expected: 2

s5 = "a"
print(f"Score of '{s5}': {scoreOfString(s5)}") # Expected: 0

s6 = "aa"
print(f"Score of '{s6}': {scoreOfString(s6)}") # Expected: 0

s7 = "AZ"
print(f"Score of '{s7}': {scoreOfString(s7)}") # Expected: 25

s8 = "123"
print(f"Score of '{s8}': {scoreOfString(s8)}") # Expected: 2

s9 = "!@#"
print(f"Score of '{s9}': {scoreOfString(s9)}") # Expected: 2

s10 = "Aa"
print(f"Score of '{s10}': {scoreOfString(s10)}") # Expected: 32