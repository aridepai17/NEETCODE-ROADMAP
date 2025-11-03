# REPEATED DNA SEQUENCES

'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule. You may return the answer in any order.
'''

def repeatedDNASequences(s):
    seen = set()
    result = set()
    
    for i in range(len(s) - 9):
        current = s[i: i + 10]
        if current in seen:
            result.add(current)
        seen.add(current)
        
    return list(result)

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The algorithm iterates through the string with a single loop that runs `len(s) - 9` times, which is approximately O(N).
- In each iteration, we perform the following operations:
  - Creating a substring `s[i: i + 10]` takes O(10) = O(1) time since the substring length is constant (10 characters).
  - Checking if `current` exists in the `seen` set is O(1) on average due to hash set operations.
  - Adding `current` to either `result` or `seen` set is O(1) on average.
- Therefore, the overall time complexity is O(N).

Space Complexity: O(N)
- The `seen` set stores all unique 10-letter substrings encountered. In the worst case, if all substrings are unique, the set will contain approximately N - 9 substrings, each of length 10.
- The `result` set stores all 10-letter substrings that appear more than once. In the worst case, this could also contain up to N - 9 substrings.
- Each substring stored requires O(10) = O(1) space, but the number of substrings can be up to O(N).
- Therefore, the space complexity is O(N) in the worst case.
'''

# Test Cases
s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(repeatedDNASequences(s1)) # Output: ["AAAAACCCCC", "CCCCCAAAAA"]

s2 = "AAAAAAAAAAAAA"
print(repeatedDNASequences(s2)) # Output: ["AAAAAAAAAAAA"]

s3 = "AAAAAAAAAAA"
print(repeatedDNASequences(s3)) # Output: ["AAAAAAAAAA"]

s4 = "ACGTACGTAC"
print(repeatedDNASequences(s4)) # Output: []

s5 = "ACGTACGTACGTACGTACGT"
print(repeatedDNASequences(s5)) # Output: ["ACGTACGTAC"]

s6 = "GAGAGAGAGAGAGAGAGAGA"
print(repeatedDNASequences(s6)) # Output: ["GAGAGAGAGA", "AGAGAGAGAG"]

s7 = "ATCGATCGATCGATCGATCG"
print(repeatedDNASequences(s7)) # Output: ["ATCGATCGAT", "TCGATCGATC", "CGATCGATCG"]

s8 = "TTTTTTTTTT"
print(repeatedDNASequences(s8)) # Output: []

s9 = "ACGTACGTACGTACGT"
print(repeatedDNASequences(s9)) # Output: ["ACGTACGTAC"]

s10 = "GGGGGGGGGGGGGGGGGGGG"
print(repeatedDNASequences(s10)) # Output: ["GGGGGGGGGG"]