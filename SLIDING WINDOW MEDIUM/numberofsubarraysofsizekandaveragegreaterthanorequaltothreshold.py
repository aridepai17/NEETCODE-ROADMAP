# NUMBER OF SUBARRAYS OF SIZE K AND AVERAGE GREATER THAN OR EQUAL TO THRESHOLD

'''
Given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.
'''

def numOfSubarrays(arr, k, threshold):
    currentSum = 0
    minSumRequired = threshold * k
    count = 0
    n = len(arr)
    left = 0
    
    for right in range(n):
        currentSum += arr[right]
        if right - left == k:
            if currentSum >= minSumRequired:
                count += 1
            currentSum -= arr[left]
            left += 1
            
    return count

'''
Time Complexity: O(n)
We iterate through the array once using a single for loop, where 'n' is the number of elements in the input array `arr`. This is a classic sliding window approach.

Space Complexity: O(1)
We only use a constant amount of extra space for variables like `currentSum`, `count`, `left`, etc., regardless of the input size.
'''

# Test Cases
arr1 = [2,2,2,2,5,5,5,8], k1 = 3, threshold1 = 4
print(numOfSubarrays(arr1, k1, threshold1)) # Output: 3

arr2 = [1,1,1,1,1], k2 = 3, threshold2 = 2
print(numOfSubarrays(arr2, k2, threshold2)) # Output: 0

arr3 = [11,13,17,23,29,31,7,5,2,3], k3 = 3, threshold3 = 5
print(numOfSubarrays(arr3, k3, threshold3)) # Output: 6

# Edge case: empty array
arr4 = [], k4 = 2, threshold4 = 10
print(numOfSubarrays(arr4, k4, threshold4)) # Output: 0

# Edge case: k is larger than the array length
arr5 = [1, 2, 3], k5 = 4, threshold5 = 1
print(numOfSubarrays(arr5, k5, threshold5)) # Output: 0

# Array with negative numbers
arr6 = [-1, -2, -3, -4, -5], k6 = 2, threshold6 = -3
print(numOfSubarrays(arr6, k6, threshold6)) # Output: 2

# Array with all zeros
arr7 = [0, 0, 0, 0, 0], k7 = 3, threshold7 = 0
print(numOfSubarrays(arr7, k7, threshold7)) # Output: 3

# k = 1
arr8 = [1, 2, 3, 4, 5], k8 = 1, threshold8 = 3
print(numOfSubarrays(arr8, k8, threshold8)) # Output: 3

# Large numbers
arr9 = [100, 200, 300, 400], k9 = 2, threshold9 = 250
print(numOfSubarrays(arr9, k9, threshold9)) # Output: 2

# All subarrays meet the threshold exactly
arr10 = [4, 4, 4, 4], k10 = 2, threshold10 = 4
print(numOfSubarrays(arr10, k10, threshold10)) # Output: 3