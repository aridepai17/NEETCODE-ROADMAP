# COUNT ELEMENTS WITH MAXIMUM FREQUENCY

'''
You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.
'''

def maxFrequencyElements(nums):
    hashMap = {}
    count = 0
    
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        
    maxFreq = max(hashMap.values())
    
    for value in hashMap.values():
        if value == maxFreq:
            count += value
            
    return count

'''
Time Complexity: O(N)
We iterate through the input array `nums` once to build the frequency map. This takes O(N) time, where N is the number of elements in `nums`.
Then, we find the maximum frequency among the unique elements, which takes O(U) time, where U is the number of unique elements.
Finally, we iterate through the frequencies again to sum up the counts of elements with the maximum frequency, which also takes O(U) time.
Since U <= N, the total time complexity is dominated by the initial pass, making it O(N).

Space Complexity: O(U)
We use a hash map to store the frequency of each element. The space required is proportional to the number of unique elements, U.
In the worst case, all elements are unique (U = N), so the space complexity would be O(N).
'''

# Test Case
nums1 = [1,2,2,3,1,4]
print(maxFrequencyElements) # Output: 4

nums2 = [10, 20, 10, 20]
print(maxFrequencyElements(nums2)) # Output: 4

nums3 = [1, 2, 3, 4, 5]
print(maxFrequencyElements(nums3)) # Output: 5

nums4 = [5, 5, 5, 5, 5]
print(maxFrequencyElements(nums4)) # Output: 5

nums5 = [100]
print(maxFrequencyElements(nums5)) # Output: 1

nums6 = [1,2,3,1,2,1]
print(maxFrequencyElements(nums6)) # Output: 3

nums7 = [1000, 1000, 500, 500, 100, 1000]
print(maxFrequencyElements(nums7)) # Output: 3

nums8 = [1,1,1,2,2,3,3,4,4,4,5,5,5]
print(maxFrequencyElements(nums8)) # Output: 9

nums9 = [2,3,5,2,3,2]
print(maxFrequencyElements(nums9)) # Output: 3

nums10 = [8, 9, 10, 11]
print(maxFrequencyElements(nums10)) # Output: 4