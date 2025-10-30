# SORT CHARACTERS BY FREQUENCY

'''
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
'''

def frequencySort(s):
    hashMap = {}
    for char in s:
        hashMap[char] = hashMap.get(char, 0) + 1
        
    buckets = [[] for _ in range(len(s) + 1)]
    
    for char, count in hashMap.items():
        buckets[count].append(char)
        
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for char in buckets[i]:
            result.append(char * i)
            
    return "".join(result)

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- Counting character frequencies using a hash map takes O(N) time.
- Building the buckets array takes O(N) time (initializing buckets and populating them).
- Constructing the result string by iterating through buckets takes O(N) time in total, as each character is processed exactly once.
- Therefore, the overall time complexity is O(N).

Space Complexity: O(N)
- The hash map uses O(k) space where k is the number of unique characters (at most O(N)).
- The buckets array uses O(N) space (size len(s) + 1).
- The result list uses O(N) space for the output.
- Therefore, the overall space complexity is O(N).
'''

# Test Cases
s1 = "tree"
print(frequencySort(s1)) # Output: "eert"

s2 = "cccaaa"
print(frequencySort(s2)) # Output: "cccaaa" or "aaaccc"

s3 = "Aabb"
print(frequencySort(s3)) # Output: "bbAa" or "bbaA"

s4 = "loveleetcode"
print(frequencySort(s4)) # Output: "eeeeoollvtdc"

s5 = "abcabcabc"
print(frequencySort(s5)) # Output: "aaabbbccc"

s6 = "a"
print(frequencySort(s6)) # Output: "a"

s7 = ""
print(frequencySort(s7)) # Output: ""

s8 = "112233"
print(frequencySort(s8)) # Output: "332211" or "223311" etc.

s9 = "!@#$%^&*()"
print(frequencySort(s9)) # Output: "!@#$%^&*()" (all unique characters)

s10 = "mississippi"
print(frequencySort(s10)) # Output: "ssssppiiii" or "iiiippssss"