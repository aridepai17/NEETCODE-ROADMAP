# CUSTOM SORT STRING

'''
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.
'''

def customSortString(order, s):
    hashMap = {}
    for char in s:
        hashMap[char] = hashMap.get(char, 0) + 1
        
    result = []

    for char in order:
        if char in hashMap:
            result.append(char * hashMap[char])
            del hashMap[char]
            
    for char, count in hashMap.items():
        result.append(char * count)
        
        
    return "".join(result)

'''
Time Complexity: O(N + M)
- Let N be the length of the string `s`.
- Let M be the length of the string `order`.
- Building the hash map by iterating through `s` takes O(N) time.
- Iterating through `order` and constructing the result takes O(M) time.
- Iterating through the remaining characters in the hash map takes O(K) time, where K is the number of unique characters in `s` (at most O(N)).
- The `"".join(result)` operation takes O(N) time as it concatenates all characters from `s`.
- Therefore, the overall time complexity is O(N + M).

Space Complexity: O(N)
- The hash map stores at most K unique characters from `s`, where K ≤ N, requiring O(K) space.
- The `result` list stores all N characters from `s`, requiring O(N) space.
- The final joined string also requires O(N) space.
- Therefore, the overall space complexity is O(N).
'''

# Test Cases
order1 = "cba", s1 = "abcd"
print(customSortString(order1, s1)) # Output: "cbad"

order2 = "bcafg", s2 = "abcd"
print(customSortString(order2, s2)) # Output: "bcad"

order3 = "kqep", s3 = "pekeq"
print(customSortString(order3, s3)) # Output: "kqeep"

order4 = "xyz", s4 = "abcxyz"
print(customSortString(order4, s4)) # Output: "xyzabc"

order5 = "a", s5 = "aaabbb"
print(customSortString(order5, s5)) # Output: "aaabbb"

order6 = "abc", s6 = "cccbbbaa"
print(customSortString(order6, s6)) # Output: "aabbbccc"

order7 = "zyx", s7 = "xyz"
print(customSortString(order7, s7)) # Output: "zyx"

order8 = "defabc", s8 = "abcdefg"
print(customSortString(order8, s8)) # Output: "defabcg"

order9 = "hgfedcba", s9 = "abcdefgh"
print(customSortString(order9, s9)) # Output: "hgfedcba"

order10 = "order", s10 = "rrddeeoo"
print(customSortString(order10, s10)) # Output: "oorrddee"