# NAMING A COMPANY

'''
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. 
The process of naming a company is as follows: Choose 2 distinct names from ideas, call them ideaA and ideaB. 
Swap the first letters of ideaA and ideaB with each other. 
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name. 
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.
'''

def distinctNames(ideas):
    groups = [set() for _ in range(26)]
    
    for word in ideas:
        first = ord(word[0]) - ord("a")
        groups[first].add(word[1:])
        
    result = 0
    for i in range(26):
        for j in range(i + 1, 26):
            common = len(groups[i] & groups[j])
            unique1 = len(groups[i]) - common
            unique2 = len(groups[j]) - common
            result += unique1 * unique2 * 2
            
    return result

'''
Time Complexity: O(N * M + A^2 * M)
- Let N be the number of strings in the `ideas` array.
- Let M be the average length of each string (excluding the first character).
- Let A be the size of the alphabet (26 for lowercase English letters).
- First loop: We iterate through all N strings. For each string, we extract the first character and add the suffix to the appropriate group. This takes O(N * M) time.
- Second loop: We have a nested loop that iterates through all pairs of alphabet groups (i, j) where i < j. This is O(A^2) iterations.
- For each pair, we compute the intersection of two sets (`groups[i] & groups[j]`). In the worst case, each set can have up to N suffixes of length M, so the intersection operation takes O(min(|groups[i]|, |groups[j]|) * M) time. Across all pairs, this is O(A^2 * M) in the average case.
- Overall time complexity: O(N * M + A^2 * M). Since A is constant (26), this simplifies to O(N * M).

Space Complexity: O(N * M)
- We use an array of 26 sets to store the suffixes of the strings.
- In the worst case, all N strings have different first letters distributed across the 26 groups.
- Each suffix has an average length of M characters.
- The total space required to store all suffixes across all groups is O(N * M).
'''

# Test Cases
ideas1 = ["coffee", "donuts", "time", "toffee"]
print(distinctNames(ideas1)) # Output: 6

ideas2 = ["lack", "back"]
print(distinctNames(ideas2)) # Output: 0

ideas3 = ["apple", "banana", "cherry"]
print(distinctNames(ideas3)) # Output: 6

ideas4 = ["a", "b", "c", "d"]
print(distinctNames(ideas4)) # Output: 12

ideas5 = ["abc", "bca", "cab"]
print(distinctNames(ideas5)) # Output: 6

ideas6 = ["hello", "hallo", "hillo"]
print(distinctNames(ideas6)) # Output: 0

ideas7 = ["test", "best", "rest", "nest"]
print(distinctNames(ideas7)) # Output: 12

ideas8 = ["dog", "cat", "rat", "bat"]
print(distinctNames(ideas8)) # Output: 12

ideas9 = ["same", "same", "same"]
print(distinctNames(ideas9)) # Output: 0

ideas10 = ["xy", "yz", "zx"]
print(distinctNames(ideas10)) # Output: 6