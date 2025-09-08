# NEXT GREATER ELEMENT 1

'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''

# Solution 1: Brute Force using HashMap
def nextGreaterElement1(nums1, nums2):
    hashMap = {}
    i = 0
    
    while i < len(nums2):
        hashMap[nums2[i]] = i
        i += 1
        
    answer = []
    
    for num in nums1:
        startIndex = hashMap[num]
        nextGreater = -1
        
        j = startIndex + 1
        
        while j < len(nums2):
            if nums2[j] > num:
                nextGreater = nums2[j]
                break
            j += 1
            
        answer.append(nextGreater)
        
    return answer

'''
Time Complexity: O(m * n)
Let m be the length of nums1 and n be the length of nums2.
The first while loop iterates through nums2 to create a hash map of its elements to their indices. This takes O(n) time.
The second for loop iterates through each element in nums1 (m elements).
For each element in nums1, we perform a lookup in the hash map which is O(1) on average.
Then, we iterate through the rest of nums2 from the found index. In the worst case, this inner while loop can run up to n times for each element in nums1.
Therefore, the total time complexity is O(n + m * n), which simplifies to O(m * n).

Space Complexity: O(n)
We use a hash map to store the elements of nums2 and their indices. In the worst case, this map will store all n elements of nums2.
The result array `answer` will store m elements.
Since nums1 is a subset of nums2, m <= n.
Thus, the space complexity is O(n) for the hash map.
'''

# Solution 2: Using Monotonic Stack and HashMap
def nextGreaterElement2(nums1, nums2):
    hashMap = {}
    stack = []
    
    for num in nums2:
        while stack and num > stack[-1]:
            popped = stack.pop()
            hashMap[popped] = num

        stack.append(num)
        
    while stack:
        popped = stack.pop()
        hashMap[popped] = -1
        
    answer = []
    
    for num in nums1:
        answer.append(hashMap[num])
        
    return answer

'''
Time Complexity: O(m + n)
Let m be the length of nums1 and n be the length of nums2.
We iterate through nums2 once to populate the hash map. Each element of nums2 is pushed and popped from the stack at most once. This takes O(n) time.
The while loop after that processes any remaining elements in the stack, which also takes at most O(n) time.
Then, we iterate through nums1 to build the result array. This takes O(m) time.
The total time complexity is O(n + m).

Space Complexity: O(n)
We use a hash map to store the next greater element for each number in nums2. In the worst case, this map will store all n elements of nums2.
The stack can also store up to n elements in the worst case (e.g., if nums2 is sorted in descending order).
The result array `answer` will store m elements.
Since nums1 is a subset of nums2, m <= n.
Thus, the space complexity is dominated by the hash map and the stack, making it O(n).
'''

# Test Cases
nums1 = [4,1,2], nums2 = [1,3,4,2]
print(nextGreaterElement2(nums1, nums2)) # Output: [-1, 3, -1]

nums1 = [2,4], nums2 = [1,2,3,4]
print(nextGreaterElement2(nums1, nums2)) # Output: [3, -1]

nums1 = [1,3,5,2,4], nums2 = [6,5,4,3,2,1,7]
print(nextGreaterElement2(nums1, nums2)) # Output: [7, 7, 7, 7, 7]

nums1 = [3,2,1], nums2 = [3,2,1]
print(nextGreaterElement2(nums1, nums2)) # Output: [-1, -1, -1]

nums1 = [1,2,3], nums2 = [1,2,3]
print(nextGreaterElement2(nums1, nums2)) # Output: [2, 3, -1]

nums1 = [7,8], nums2 = [1,2,3,4,5,6,7,8]
print(nextGreaterElement2(nums1, nums2)) # Output: [8, -1]

nums1 = [1], nums2 = [1]
print(nextGreaterElement2(nums1, nums2)) # Output: [-1]

nums1 = [], nums2 = [1,2,3]
print(nextGreaterElement2(nums1, nums2)) # Output: []

nums1 = [6, 7], nums2 = [7, 6]
print(nextGreaterElement2(nums1, nums2)) # Output: [-1, -1]

nums1 = [137, 59, 92], nums2 = [137, 59, 92]
print(nextGreaterElement2(nums1, nums2)) # Output: [-1, 92, -1]