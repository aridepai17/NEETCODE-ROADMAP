# FIND LUCKY INTEGER IN AN ARRAY

'''
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. 
If there is no lucky integer return -1.
'''

def findLucky(arr):
    freq = {}
    lucky = -1
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
    for key in freq.keys():
        if key == freq[key]:
            lucky = max(lucky, key)
            
    return lucky

'''
Time Complexity: O(n)
We iterate through the array once to build the frequency map, which takes O(n) time, where n is the number of elements in the array.
Then, we iterate through the keys of the frequency map. In the worst case, all elements are unique, so this also takes O(n) time.
Thus, the total time complexity is O(n) + O(n) = O(n).

Space Complexity: O(n)
We use a hash map (dictionary) to store the frequency of each number. In the worst case, if all numbers in the array are unique, the hash map will store n key-value pairs.
Therefore, the space complexity is O(n).
'''

# Test Cases
arr1 = [2,2,3,4]
print(findLucky(arr1)) # Output: 2

arr2 = [1,2,2,3,3,3]
print(findLucky(arr2)) # Output: 3

arr3 = [1,1,1,2,2]
print(findLucky(arr3)) # Output: 2

arr4 = [5]
print(findLucky(arr4)) # Output: -1

arr5 = [7,7,7,7,7,7,7]
print(findLucky(arr5)) # Output: 7

arr6 = [4,4,4,4]
print(findLucky(arr6)) # Output: 4

arr7 = [2,2,2]
print(findLucky(arr7)) # Output: -1

arr8 = [1]
print(findLucky(arr8)) # Output: 1

arr9 = []
print(findLucky(arr9)) # Output: -1

arr10 = [5,5,5,2,2,8,8,8,8,8,8,8,8]
print(findLucky(arr10)) # Output: 8