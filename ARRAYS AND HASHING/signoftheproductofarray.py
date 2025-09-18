# SIGN OF PRODUCT OF ARRAY

'''
Implement a function signFunc(x) that returns:
1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).
'''

def arraySign(nums):
    product = 1
    
    if 0 in nums:
        return 0
    
    for num in nums:
        product *= num
        
    if product > 0:
        return 1
    else:
        return -1

'''
Time Complexity: O(N)
Let N be the number of elements in the input array `nums`.
- The check `if 0 in nums:` requires iterating through the array in the worst case, which takes O(N) time.
- If 0 is not in the array, the code then enters a `for` loop that iterates through all N elements of `nums` to compute their product. This loop also takes O(N) time.
- The operations inside the loop (multiplication) and the final check of the product's sign are constant time operations, O(1).
- Since these two O(N) operations are sequential, the total time complexity is O(N) + O(N), which simplifies to O(N).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space, regardless of the input size.
- A single variable `product` is used to store the running product.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [-1,-2,-3,-4,3,2,1]
print(arraySign(nums1)) # Output: 1

nums2 = [1, 5, 0, 2, -3]
print(arraySign(nums2)) # Output: 0

nums3 = [-1, 1, -1, 1, -1]
print(arraySign(nums3)) # Output: -1

nums4 = [1, 2, 3, 4, 5]
print(arraySign(nums4)) # Output: 1

nums5 = [4, 3, -2, -1]
print(arraySign(nums5)) # Output: 1

nums6 = [-5]
print(arraySign(nums6)) # Output: -1

nums7 = [100]
print(arraySign(nums7)) # Output: 1

nums8 = [0]
print(arraySign(nums8)) # Output: 0

nums9 = [9, 72, 34, 29, -49, -22, -77, -17, -66, -75, -44, -30, -24, -9, -72, 0]
print(arraySign(nums9)) # Output: 0

nums10 = [-1, -1, -1, 5, 8, 10]
print(arraySign(nums10)) # Output: -1