# LENGTH OF LAST WORD

# Given a string s consisting of words and spaces, return the length of the last word in the string.

def lengthofLastWord(s):
    words = s.split()
    lastWord = words[-1]
    return len(lastWord)

# Test Cases
s1 = "Hello World"
print(lengthofLastWord(s1)) # Output: 5

s2 = "   fly me   to   the moon  "
print(lengthofLastWord(s2)) # Output: 4

s3 = "luffy is still joyboy"
print(lengthofLastWord(s3)) # Output: 6

s4 = "a"
print(lengthofLastWord(s4)) # Output: 1

s5 = "   a   "
print(lengthofLastWord(s5)) # Output: 1

s6 = "python programming"
print(lengthofLastWord(s6)) # Output: 11

s7 = "test"
print(lengthofLastWord(s7)) # Output: 4

s8 = "   hello   world   "
print(lengthofLastWord(s8)) # Output: 5

s9 = "one two three four"
print(lengthofLastWord(s9)) # Output: 4

s10 = "supercalifragilisticexpialidocious"
print(lengthofLastWord(s10)) # Output: 34