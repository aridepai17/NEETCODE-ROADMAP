# SORT AN ARRAY

'''
Given an array of integers nums, sort the array in ascending order and return it.

Constraints:
- Solve without built-in sort; target O(n log n) time.
- Use the minimum extra space possible.

Complexity:
- Time  : O(n log n)
- Space : O(n) auxiliary (temporary slices) + O(log n) recursion stack (≈ O(n))
'''

def sortArray(nums):
    def merge(arr, left, mid, right):
        L = arr[left: mid + 1]
        R = arr[mid + 1: right + 1]
        
        i = left
        j = 0
        k = 0
        
        while j < len(L) and k < len(R):
            if L[j] <= R[k]:
                arr[i] = L[j]
                j += 1
            else:
                arr[i] = R[k]
                k += 1
            i += 1
            
        while j < len(L):
            arr[i] = L[j]
            j += 1
            i += 1
            
        while k < len(R):
            arr[i] = R[k]
            k += 1
            i += 1
            
        return arr
    def mergeSort(arr, left, right):
        if left == right:
            return arr
        
        mid = (left + right) // 2
        
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        
        return arr
    
    return mergeSort(nums, 0, len(nums) - 1)


'''
Time Complexity: O(N * logN)
- Let N be the number of elements in the input array `nums`.
- The merge sort algorithm divides the array into two halves recursively until each subarray contains a single element.
- The depth of the recursion tree is O(logN), as we repeatedly divide the array in half.
- At each level of recursion, we perform O(N) work in total across all merge operations.
- The merge function processes each element once at each level, taking O(N) time per level.
- Therefore, the overall time complexity is O(N * logN).

Space Complexity: O(N)
- The merge function creates temporary arrays L and R to hold the left and right subarrays.
- At any given level of recursion, the total size of all temporary arrays is O(N).
- The recursion stack depth is O(logN), which stores the function call frames.
- The dominant space factor is the temporary arrays, giving us O(N) auxiliary space.
- Therefore, the overall space complexity is O(N).
'''

# Test Cases
nums1 = [5, 2, 3, 1]
print(sortArray(nums1)) # Output: [1, 2, 3, 5]

nums2 = [5, 1, 1, 2, 0, 0]
print(sortArray(nums2)) # Output: [0, 0, 1, 1, 2, 5]

nums3 = [3, 1, 4, 1, 5, 9, 2, 6]
print(sortArray(nums3)) # Output: [1, 1, 2, 3, 4, 5, 6, 9]

nums4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sortArray(nums4)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums5 = [1]
print(sortArray(nums5)) # Output: [1]

nums6 = []
print(sortArray(nums6)) # Output: []

nums7 = [3, 3, 3, 3, 3]
print(sortArray(nums7)) # Output: [3, 3, 3, 3, 3]

nums8 = [-5, -1, -3, -2, -4]
print(sortArray(nums8)) # Output: [-5, -4, -3, -2, -1]

nums9 = [-1, 5, -3, 2, 0, 4]
print(sortArray(nums9)) # Output: [-3, -1, 0, 2, 4, 5]

nums10 = [1, 2, 3, 4, 5]
print(sortArray(nums10)) # Output: [1, 2, 3, 4, 5]

nums11 = [7, 2, 9, 2, 5, 1, 8]
print(sortArray(nums11)) # Output: [1, 2, 2, 5, 7, 8, 9]