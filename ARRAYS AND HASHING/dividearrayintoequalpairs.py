# DIVIDE ARRAY INTO EQUAL PAIRS

'''
You are given an integer array nums consisting of 2 * n integers.
You need to divide nums into n pairs such that:
- Each element belongs to exactly one pair.
- The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
'''

# Solution 1: Using a HashMap
def divideArray1(nums):
    freq = {}
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for val in freq.values():
        if val % 2 == 1:
            return False
        
    return True

'''
Time Complexity: O(N)
Let N be the number of elements in the `nums` array.
- We iterate through the `nums` array once to build the frequency map. This involves N insertions or updates into the hash map, where each operation takes, on average, O(1) time. This step takes O(N) time.
- We then iterate through the values of the frequency map. The number of unique elements in `nums` is at most N. Let's say there are `k` unique elements. This loop runs `k` times. Since `k <= N`, this step is O(N) in the worst case.
- The overall time complexity is dominated by these linear scans, resulting in O(N).

Space Complexity: O(N)
- The algorithm uses a hash map (`freq`) to store the counts of each number in the input array.
- In the worst-case scenario, if there are many unique numbers, the size of the hash map will grow proportionally to the number of unique elements.
- For example, if all pairs are distinct (e.g., [1,1, 2,2, ..., N/2, N/2]), the hash map will store N/2 key-value pairs.
- Therefore, the space complexity is O(N), as the space required depends on the number of unique elements, which can be at most N/2.
'''

# Solution 2: Using a HashSet
def divideArray2(nums):
    oddSet = set()
    
    for num in nums:
        if not num in oddSet:
            oddSet.add(num)
        else:
            oddSet.remove(num)
            
    return len(oddSet) == 0

'''
Time Complexity: O(N)
Let N be the number of elements in the `nums` array.
- The algorithm iterates through the `nums` array once with a single `for` loop.
- Inside the loop, all operations on the hash set (`add`, `remove`, and checking for existence) take, on average, constant time, O(1).
- Since the loop runs N times and each iteration takes O(1) time, the total time complexity is O(N).

Space Complexity: O(N)
- The algorithm uses a hash set (`oddSet`) to keep track of numbers that have appeared an odd number of times.
- In the worst-case scenario, if the first N/2 elements are all unique, the hash set will store N/2 elements.
- For example, in an array like `[1, 2, 3, ..., N/2, 1, 2, 3, ..., N/2]`, the set's size will grow to N/2.
- Therefore, the space required by the set is proportional to the number of unique elements, which can be up to O(N).
'''

# Test Cases
nums1 = [3,2,3,2,2,2]
print(divideArray1(nums1)) # Output: True

nums2 = [1,2,3,4]
print(divideArray1(nums2)) # Output: False

nums3 = [1,1]
print(divideArray1(nums3)) # Output: True

nums4 = [1,1,2,3]
print(divideArray1(nums4)) # Output: False

nums5 = [10,10,10,10,20,20]
print(divideArray1(nums5)) # Output: True

nums6 = [1,1,1,1,1,1]
print(divideArray1(nums6)) # Output: True

nums7 = [1,1,1,2,2,2]
print(divideArray1(nums7)) # Output: False

nums8 = []
print(divideArray1(nums8)) # Output: True

nums9 = [8,8]
print(divideArray1(nums9)) # Output: True

nums10 = [8,9]
print(divideArray1(nums10)) # Output: False