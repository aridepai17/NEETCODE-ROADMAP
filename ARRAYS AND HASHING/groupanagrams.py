# GROUP ANAGRAMS

'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
'''

from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)
    
    for word in strs:
        count = [0] * 26
        
        for char in word:
            count[ord(char) - ord('a')] += 1
            
        result[tuple(count)].append(word)
        
    return list(result.values())

# Time Complextiy
# For each word (n words) we count characters in O(k) where k is the word length, and map by a 26-sized key.
# Overall Time Complexity: O(n * k)
# Space Complexity
# We store the groups and a 26-length count per distinct anagram class. Output dominates.
# Overall Space Complexity: O(n * k) including the output (auxiliary ~ O(n)).

# Test Cases
strs1 = ["a"]
print(groupAnagrams(strs1)) # Output: [["a"]]

strs2 = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs2)) # Output (order may vary): [["eat","tea","ate"],["tan","nat"],["bat"]]

strs3 = [""]
print(groupAnagrams(strs3)) # Output: [[""]]

strs4 = ["",""]
print(groupAnagrams(strs4)) # Output: [["",""]]

strs5 = ["ab","ba","abc","bca","cab"]
print(groupAnagrams(strs5)) # Output (order may vary): [["ab","ba"],["abc","bca","cab"]]

strs6 = ["dddddddddd","d"]
print(groupAnagrams(strs6)) # Output: [["dddddddddd"],["d"]]

strs7 = ["listen","silent","enlist","google","gooegl"]
print(groupAnagrams(strs7)) # Output (order may vary): [["listen","silent","enlist"],["google","gooegl"]]

strs8 = ["abc","def","ghi"]
print(groupAnagrams(strs8)) # Output (order may vary): [["abc"],["def"],["ghi"]]

strs9 = ["aaaa","aaa","aa","a"]
print(groupAnagrams(strs9)) # Output: [["aaaa"],["aaa"],["aa"],["a"]]

strs10 = ["rat","tar","art","star","tars","cheese"]
print(groupAnagrams(strs10)) # Output (order may vary): [["rat","tar","art"],["star","tars"],["cheese"]]

strs11 = ["abcabc","cbacba","bcaabc","xyz"]
print(groupAnagrams(strs11)) # Output (order may vary): [["abcabc","cbacba","bcaabc"],["xyz"]]

strs12 = ["noanagram"]
print(groupAnagrams(strs12)) # Output: [["noanagram"]]

strs13 = ["abc","cba","bac","cab","acb","bca"]
print(groupAnagrams(strs13)) # Output (order may vary): [["abc","cba","bac","cab","acb","bca"]]

strs14 = ["z","zz","zzz","zzzz"]
print(groupAnagrams(strs14)) # Output (order may vary): [["z"],["zz"],["zzz"],["zzzz"]]

strs15 = ["loop","pool","polo","lopo","olop"]
print(groupAnagrams(strs15)) # Output (order may vary): [["loop","pool","polo","lopo","olop"]]