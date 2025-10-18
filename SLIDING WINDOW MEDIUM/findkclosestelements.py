# FIND K CLOSEST ELEMENTS

'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
'''

def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - k
    
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
            
    return arr[left : left + k]

'''
Time Complexity: O(log(N-k) + k)
The algorithm uses binary search to find the optimal starting point for the window of k elements.
The search space for the binary search is from index 0 to N-k, where N is the length of the array.
This binary search takes O(log(N-k)) time.
After finding the starting index `left`, the algorithm slices the array to get the k closest elements.
Slicing the array to create a new list of size k takes O(k) time.
Therefore, the total time complexity is O(log(N-k) + k).

Space Complexity: O(k)
The algorithm uses a constant amount of extra space for variables like `left`, `right`, and `mid` (O(1)).
The return value is a new list of size k, created by slicing the original array.
If we consider the space required for the output, the space complexity is O(k).
'''

# Test Cases
arr1 = [1,2,3,4,5], k1 = 4, x1 = 3
print(findClosestElements(arr1, k1, x1)) # Output: [1, 2, 3, 4]

arr2 = [1,2,3,4,5], k2 = 4, x2 = -1
print(findClosestElements(arr2, k2, x2)) # Output: [1, 2, 3, 4]

arr3 = [1,2,3,4,5], k3 = 4, x3 = 6
print(findClosestElements(arr3, k3, x3)) # Output: [2, 3, 4, 5]

arr4 = [1,1,1,10,10,10], k4 = 3, x4 = 9
print(findClosestElements(arr4, k4, x4)) # Output: [10, 10, 10]

arr5 = [0,0,1,2,3,3,4,7,7,8], k5 = 3, x5 = 5
print(findClosestElements(arr5, k5, x5)) # Output: [3, 4, 7]

arr6 = [1,2,5,10], k6 = 1, x6 = 4
print(findClosestElements(arr6, k6, x6)) # Output: [5]

arr7 = [1,2,5,10], k7 = 1, x7 = 3
print(findClosestElements(arr7, k7, x7)) # Output: [2]

arr8 = [-10, -5, 0, 5, 10], k8 = 3, x8 = 1
print(findClosestElements(arr8, k8, x8)) # Output: [-5, 0, 5]

arr9 = [1, 10, 15, 20, 25, 30], k9 = 5, x9 = 18
print(findClosestElements(arr9, k9, x9)) # Output: [10, 15, 20, 25, 30]

arr10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k10 = 10, x10 = 5
print(findClosestElements(arr10, k10, x10)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]