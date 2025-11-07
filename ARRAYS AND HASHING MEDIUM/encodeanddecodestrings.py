# ENCODE AND DECODE STRINGS

'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode.
'''

def encode(strs):
    result = ""
    for word in strs:
        result += str(len(word)) + "#" + word
    return result

def decode(s):
    result = []
    i = 0
    
    while i < len(s):
        j = i
        while str[j] != "#":
            j += 1
        length = int(s[i:j])
        start = j + 1
        end = j + 1 + length
        result.append(s[start:end])
        i = end
        
    return result

'''
Time Complexity: O(N)
- Let N be the total number of characters across all strings in the input list.
- **Encode**: We iterate through each string in `strs` and concatenate its length, a delimiter "#", and the string itself. This takes O(N) time, where N is the total length of all strings combined.
- **Decode**: We iterate through the encoded string once, parsing the length prefix and extracting substrings. Each character in the encoded string is processed exactly once, taking O(N) time.
- Overall time complexity: O(N) for both encode and decode operations.

Space Complexity: O(N)
- **Encode**: We build a result string that contains all original characters plus length prefixes and delimiters. The space required is O(N), where N is the total length of all input strings.
- **Decode**: We build a result list containing all the original strings, which requires O(N) space to store the decoded strings.
- Overall space complexity: O(N) for both operations, not counting the input and output storage.
'''

# Test Cases
strs1 = ["lint", "code", "love", "you"]
print(encode(strs1)) # Output: "4#lint4#code4#love3#you"
print(decode("4#lint4#code4#love3#you")) # Output: ["lint", "code", "love", "you"]

strs2 = [""]
print(encode(strs2)) # Output: "0#"
print(decode("0#")) # Output: [""]

strs3 = ["", "", ""]
print(encode(strs3)) # Output: "0#0#0#"
print(decode("0#0#0#")) # Output: ["", "", ""]

strs4 = ["hello"]
print(encode(strs4)) # Output: "5#hello"
print(decode("5#hello")) # Output: ["hello"]

strs5 = ["a", "b", "c"]
print(encode(strs5)) # Output: "1#a1#b1#c"
print(decode("1#a1#b1#c")) # Output: ["a", "b", "c"]

strs6 = ["we", "say", ":", "yes"]
print(encode(strs6)) # Output: "2#we3#say1#:3#yes"
print(decode("2#we3#say1#:3#yes")) # Output: ["we", "say", ":", "yes"]

strs7 = ["#", "##", "###"]
print(encode(strs7)) # Output: "1##2###3####"
print(decode("1##2###3####")) # Output: ["#", "##", "###"]

strs8 = ["123", "456", "789"]
print(encode(strs8)) # Output: "3#1233#4563#789"
print(decode("3#1233#4563#789")) # Output: ["123", "456", "789"]

strs9 = ["a" * 100]
print(encode(strs9)) # Output: "100#" + "a" * 100
print(decode("100#" + "a" * 100)) # Output: ["a" * 100]

strs10 = ["hello world", "test case", "encode decode"]
print(encode(strs10)) # Output: "11#hello world9#test case13#encode decode"
print(decode("11#hello world9#test case13#encode decode")) # Output: ["hello world", "test case", "encode decode"]