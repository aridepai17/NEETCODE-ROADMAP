# REPLACE ELEMENTS WITH THE GREATEST ELEMENT ON THE RIGHT SIDE

'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.
'''

def replaceElement(arr):
    maxRight = -1
    
    for i in range(len(arr) -1, -1, -1):
        current = arr[i]
        arr[i] = maxRight
        maxRight = max(maxRight, current)
        
    return arr

# Test Cases
arr1 = [17, 18, 5, 4, 6, 1]
print(replaceElement(arr1)) # Output: [18, 6, 6, 6, 1, -1]

arr2 = [400]
print(replaceElement(arr2)) # Output: [-1]

arr3 = [1, 2, 3, 4, 5]
print(replaceElement(arr3)) # Output: [5, 5, 5, 5, -1]

arr4 = [5, 4, 3, 2, 1]
print(replaceElement(arr4)) # Output: [4, 3, 2, 1, -1]

arr5 = [10, 10, 10, 10]
print(replaceElement(arr5)) # Output: [10, 10, 10, -1]

arr6 = [0, 0, 0, 0]
print(replaceElement(arr6)) # Output: [0, 0, 0, -1]

arr7 = [-1, -2, -3, -4]
print(replaceElement(arr7)) # Output: [-2, -3, -4, -1]

arr8 = [100, 50, 25, 12, 6]
print(replaceElement(arr8)) # Output: [50, 25, 12, 6, -1]

arr9 = [1, 2, 1, 2, 1, 2]
print(replaceElement(arr9)) # Output: [2, 2, 2, 2, 2, -1]

arr10 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(replaceElement(arr10)) # Output: [8, 7, 6, 5, 4, 3, 2, 1, -1]