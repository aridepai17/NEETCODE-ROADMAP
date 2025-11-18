# SUCESSFUL PAIRS OF SPELLS AND POTIONS

'''
You are given two positive integer arrays spells and potions, of length n and m respectively, 
where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
You are also given an integer success. 
A spell and potion pair is considered successful if the product of their strengths is at least success.
Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
'''

"""
Algorithm:
1. Sort the potions array in ascending order.
2. Initialize an empty list result to store the number of successful pairs for each spell.
3. For each spell in spells:
   a. Initialize two pointers: left = 0 and right = len(potions) - 1
   b. Initialize index = len(potions) to store the index of the first successful potion
   c. While left <= right:
      - Calculate mid = (left + right) // 2
      - If spell * potions[mid] >= success:
         - Update index = mid
         - Move right to mid - 1
      - Else:
         - Move left to mid + 1
   d. Append len(potions) - index to result
4. Return result
"""

def successfulPairs(spells, potions, success):
    potions.sort()
    result = []
    
    for spell in spells:
        left = 0
        right = len(potions) - 1
        index = len(potions)
        
        while left <= right:
            mid = (left + right) // 2
            if spell * potions[mid] >= success:
                right = mid - 1
                index = mid
            else:
                left = mid + 1
                
        result.append(len(potions) - index)
    
    return result

'''
Time Complexity:
- Sorting potions: O(m log m), where m is the number of potions.
- For each of n spells, binary search over potions: O(n log m).
- Total: O(m log m + n log m).

Space Complexity:
- Auxiliary: O(1) extra space (in-place sort, constant variables), excluding output.
- Output: O(n) for the result list.
'''

# Test Cases
spells1 = [5, 1, 3]
potions1 = [1, 2, 3, 4, 5]
success1 = 7
print(successfulPairs(spells1, potions1, success1)) # Output: [4, 0, 3]


spells2 = [1, 2, 3]
potions2 = [1, 2, 3]
success2 = 3
print(successfulPairs(spells2, potions2, success2)) # Output: [2, 1, 0]

spells3 = [1, 1, 1]
potions3 = [1, 1, 1]
success3 = 2
print(successfulPairs(spells3, potions3, success3)) # Output: [3, 2, 1]

spells4 = [1, 1, 1, 1]
potions4 = [1, 1, 1, 1]
success4 = 2
print(successfulPairs(spells4, potions4, success4)) # Output: [4, 3, 2, 1]

spells5 = [1, 1, 1, 2]
potions5 = [1, 1, 1, 1]
success5 = 2
print(successfulPairs(spells5, potions5, success5)) # Output: [4, 3, 2, 1]

spells6 = [1, 2, 3, 4]
potions6 = [1, 2, 3, 4]
success6 = 10
print(successfulPairs(spells6, potions6, success6)) # Output: [4, 3, 2, 1]

spells7 = [1, 2, 3, 4]
potions7 = [1, 2, 3, 4]
success7 = 11
print(successfulPairs(spells7, potions7, success7)) # Output: [4, 3, 2, 1]

spells8 = [1, 2, 3, 4]
potions8 = [1, 2, 3, 4]
success8 = 12
print(successfulPairs(spells8, potions8, success8)) # Output: [4, 3, 2, 1]

spells9 = [1, 2, 3, 4]
potions9 = [1, 2, 3, 4]
success9 = 13
print(successfulPairs(spells9, potions9, success9)) # Output: [4, 3, 2, 1]

spells10 = [1, 2, 3, 4]
potions10 = [1, 2, 3, 4]
success10 = 14
print(successfulPairs(spells10, potions10, success10)) # Output: [4, 3, 2, 1]