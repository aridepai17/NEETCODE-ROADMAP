# KTH DISTINCT ELEMENT IN AN ARRAY

'''
A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array.
'''

def kthDistinct(arr, k):
    freq = {}
    
    for word in arr:
        freq[word] = freq.get(word, 0) + 1
        
    distinctCount = 0
    
    for word in freq:
        if freq[word] == 1:
            distinctCount += 1
            if distinctCount == k:
                return word
    return ""

'''
Time Complexity: O(n)
Let n be the number of strings in the input array `arr`.
- Building the frequency map: We iterate through the `arr` once. This involves n hash map insertions/updates, each taking O(1) on average. Total time for this step is O(n).
- Finding the k-th distinct string: We iterate through the keys of the frequency map. Let m be the number of unique strings (m <= n). This loop runs m times. Total time for this step is O(m).
- The overall time complexity is O(n) + O(m), which simplifies to O(n) as m <= n.

Space Complexity: O(m)
Let m be the number of unique strings in `arr`.
- We use a hash map `freq` to store the counts of each unique string.
- The space required is proportional to the number of unique strings, m.
- In the worst case, all strings are unique (m = n), so the space complexity can be O(n). A more precise bound is O(m).
'''

# Test Cases
arr1 = ["d","b","c","b","c","a"], k1 = 2
print(kthDistinct(arr1, k1))  # Output: "a"

arr2 = ["a","a","a"], k2 = 1
print(kthDistinct(arr2, k2))  # Output: ""

arr3 = ["a","b","a"], k3 = 2
print(kthDistinct(arr3, k3))  # Output: ""

arr4 = ["aaa","aa","a"], k4 = 1
print(kthDistinct(arr4, k4))  # Output: "aaa"

arr5 = ["a", "b", "c"], k5 = 3
print(kthDistinct(arr5, k5))  # Output: "c"

arr6 = [], k6 = 1
print(kthDistinct(arr6, k6))  # Output: ""

arr7 = ["d","b","c","b","c","a"], k7 = 3
print(kthDistinct(arr7, k7))  # Output: ""

arr8 = ["a", "b", "c", "d", "a", "b", "e"], k8 = 2
print(kthDistinct(arr8, k8))  # Output: "d"

arr9 = ["b", "b", "c", "a"], k9 = 1
print(kthDistinct(arr9, k9))  # Output: "c"

arr10 = ["1", "2", "1", "3", "4", "2"], k10 = 2
print(kthDistinct(arr10, k10)) # Output: "4"