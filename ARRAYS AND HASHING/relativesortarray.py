# RELATIVE SORT ARRAY

'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
'''

def relativeSortArray(arr1, arr2):
    hashMap = {}
    
    for num in arr1:
        hashMap[num] = hashMap.get(num, 0) + 1
        
    result = []
        
    for num in arr2:
        if num in hashMap:
            result.extend([num] * hashMap[num])
            del hashMap[num]
            
    remainingKeys = sorted(hashMap.keys())
    
    for num in remainingKeys:
        result.extend([num] * hashMap[num])
        
    return result

'''
Time Complexity: O(N + M + K log K)
Let N be the number of elements in `arr1`.
Let M be the number of elements in `arr2`.
Let K be the number of unique elements in `arr1` that are not in `arr2`.
- Building the frequency map (`hashMap`) for `arr1` takes O(N) time, as it requires a single pass through the array.
- The first loop iterates through `arr2` (M elements). For each element, it performs a hash map lookup (O(1) on average) and extends the `result` list. The total time for all `extend` operations across the function is proportional to the total number of elements added, which is N. So, this part contributes O(M) for the iteration and a portion of the O(N) for the extensions.
- The remaining keys from the hash map are sorted. If there are K unique keys remaining, sorting them takes O(K log K) time.
- The final loop iterates through these K sorted keys and appends the corresponding elements to the `result` list.
- The total time complexity is the sum of these steps: O(N) (for frequency map and extensions) + O(M) (for `arr2` iteration) + O(K log K) (for sorting), which simplifies to O(N + M + K log K).

Space Complexity: O(N)
- A hash map (`hashMap`) is used to store the frequency of elements in `arr1`. In the worst case, if all elements are unique, this will require O(N) space.
- The `result` list stores all N elements from `arr1`, so it also requires O(N) space.
- The `remainingKeys` list stores the unique elements not in `arr2`. In the worst case, this could also be up to O(N) space.
- Therefore, the total auxiliary space required is proportional to N, resulting in an overall space complexity of O(N).
'''

# Test Cases
arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1, arr2)) # Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
print(relativeSortArray(arr1, arr2)) # Output: [22, 28, 8, 6, 17, 44]

arr1 = [1, 2, 3, 4, 5], arr2 = [5, 4, 3, 2, 1]
print(relativeSortArray(arr1, arr2)) # Output: [5, 4, 3, 2, 1]

arr1 = [2, 2, 1, 1, 3, 3, 3], arr2 = [1, 3, 2]
print(relativeSortArray(arr1, arr2)) # Output: [1, 1, 3, 3, 3, 2, 2]

arr1 = [5, 8, -1, 3, 5, 8, 0], arr2 = [8, 5]
print(relativeSortArray(arr1, arr2)) # Output: [8, 8, 5, 5, -1, 0, 3]

arr1 = [], arr2 = [1, 2, 3]
print(relativeSortArray(arr1, arr2)) # Output: []

arr1 = [5, 2, 8, 1, 9], arr2 = []
print(relativeSortArray(arr1, arr2)) # Output: [1, 2, 5, 8, 9]

arr1 = [10, 20, 30], arr2 = [10, 20, 30]
print(relativeSortArray(arr1, arr2)) # Output: [10, 20, 30]

arr1 = [2,3,1,3,2,4,6,7,9,2,19,0,0,-5], arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1, arr2)) # Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, -5, 0, 0, 7, 19]

arr1 = [5, 1, 5, 2, 5, 3], arr2 = [5]
print(relativeSortArray(arr1, arr2)) # Output: [5, 5, 5, 1, 2, 3]