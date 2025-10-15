# COUNT OF SUBSTRINGS CONTAINING EVERY VOWEL AND K CONSONANTS 2

'''
You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
'''

def countSubstrings(word, k):
    def atLeast(k):
        vowels = {}
        consonants = 0
        result = 0
        left = 0
        
        for right in range(len(word)):
            if word[right] in 'aeiou':
                vowels[word[right]] = vowels.get(word[right], 0) + 1
            else:
                consonants += 1
            
            while len(vowels) == 5 and consonants >= k:
                result += len(word) - right
                if word[left] in 'aeiou':
                    vowels[word[left]] -= 1
                    if vowels[word[left]] == 0:
                        del vowels[word[left]]
                else:
                    consonants -= 1
                left += 1
                
        return result
    
    return atLeast(k) - atLeast(k + 1)

'''
Time Complexity: O(N)
The overall time complexity is determined by the helper function `atLeast`, which is called twice. The `countSubstrings` function solves the "exactly k" problem by computing "at least k" and subtracting "at least k+1".
The `atLeast` function uses a sliding window approach with two pointers, `left` and `right`.
1. The `right` pointer iterates through the string `word` from beginning to end, which takes O(N) steps, where N is the length of the word.
2. The `left` pointer also moves forward, and across all iterations of the outer loop, it will traverse the string at most once.
3. Inside the loops, operations like dictionary access and arithmetic are done in constant time (O(1)) because the number of vowels is constant (at most 5).
Since each character of the string is visited by the `right` and `left` pointers at most a constant number of times, the time complexity of one call to `atLeast` is O(N).
The main function `countSubstrings` calls `atLeast` twice, so the total time complexity is O(N) + O(N) = O(N).

Space Complexity: O(1)
The algorithm uses a fixed amount of extra space regardless of the input size.
1. The `vowels` dictionary stores counts for at most 5 vowels. Its size is constant.
2. Other variables like `consonants`, `result`, `left`, and `right` occupy a constant amount of space.
Therefore, the space complexity is O(1).
'''

# Test Cases
word1 = "aeioqq", k1 = 1
print(countSubstrings(word1, k1)) # Output: 0

word2 = "aeiou", k2 = 0
print(countSubstrings(word2, k2)) # Expected: 1

word3 = "caeioubc", k3 = 1
print(countSubstrings(word3, k3)) # Expected: 2

word4 = "bcdfgh", k4 = 2
print(countSubstrings(word4, k4)) # Expected: 0

word5 = "cuaieuouac", k5 = 1
print(countSubstrings(word5, k5)) # Expected: 6

word6 = "aeioubcdfgh", k6 = 5
print(countSubstrings(word6, k6)) # Expected: 1

word7 = "aaaeioubbb", k7 = 2
print(countSubstrings(word7, k7)) # Expected: 3

word8 = "", k8 = 0
print(countSubstrings(word8, k8)) # Expected: 0

word9 = "aeiouaeiou", k9 = 0
print(countSubstrings(word9, k9)) # Expected: 21

word10 = "aaeiouu", k10 = 0
print(countSubstrings(word10, k10)) # Expected: 4