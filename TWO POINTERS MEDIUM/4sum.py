# 4 SUM

'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

# Solution 1: Using 4 Nested For Loops
def fourSum1(nums, target):
    n = len(nums)
    hashSet = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        total = tuple(sorted((nums[i], nums[j], nums[k], nums[l])))
                        hashSet.add(total)
                        
    return list(hashSet)

'''
Time Complexity: O(N^4)
- The code uses four nested loops to iterate through all possible combinations of four distinct elements in the array.
- The outer loop runs N times, the second loop runs up to N-1 times, the third up to N-2, and the fourth up to N-3 times.
- This results in a total number of iterations proportional to N * N * N * N, which simplifies to O(N^4).
- Inside the innermost loop, operations like summing, sorting a 4-element tuple, and adding to a hash set are considered constant time on average.

Space Complexity: O(k)
- A hash set `hashSet` is used to store the unique quadruplets that sum up to the target.
- The space required is proportional to the number of unique quadruplets found, denoted by `k`.
- The final list returned also takes O(k) space.
'''

# Solution 2: Using Three For Loops and HashSets
def fourSum2(nums, target):
    n = len(nums)
    hashSet = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            seen = set()
            for k in range(j + 1, n):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in seen:
                    total = tuple(sorted((nums[i], nums[j], nums[k], fourth)))
                    hashSet.add(total)
                seen.add(nums[k])
                    
    return list(hashSet)

'''
Time Complexity: O(N^3)
- The code uses three nested loops to find the quadruplets.
- The outer loop runs N times, the second loop runs up to N-1 times, and the third loop runs up to N-2 times.
- This results in a time complexity of O(N * N * N) = O(N^3).
- Inside the innermost loop, operations like calculating the `fourth` element, checking for its existence in the `seen` set, and adding to sets are O(1) on average.

Space Complexity: O(N + k)
- `hashSet` is used to store the unique quadruplets, where `k` is the number of unique quadruplets. This takes O(k) space.
- `seen` is a hash set created in each iteration of the second loop. In the worst case, it can store up to N elements to keep track of numbers seen for a given pair `(nums[i], nums[j])`. This takes O(N) space.
- Therefore, the total space complexity is the sum of the space for `seen` and `hashSet`, which is O(N + k).
'''

# Solution 3: Using Two Diffirent Two Pointers
def fourSum3(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left = j + 1
            right = n - 1
            
            while left < right:
                currentSum = nums[i] + nums[j] + nums[left] + nums[right]
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
    return result

'''
Time Complexity: O(N^3)
- Sorting the input array `nums` takes O(N log N) time.
- The code uses a nested loop structure. The first loop iterates through `i` from 0 to N-1.
- The second loop iterates through `j` from `i+1` to N-1.
- Inside the second loop, a two-pointer approach (`left` and `right`) is used to find the remaining two numbers. This inner `while` loop takes O(N) time in the worst case for each pair of `(i, j)`.
- The combination of these three nested levels of iteration results in a time complexity of O(N * N * N) = O(N^3).
- Since O(N^3) is greater than O(N log N), the overall time complexity is dominated by the nested loops, making it O(N^3).

Space Complexity: O(log N) or O(N)
- The space complexity is primarily determined by the sorting algorithm used.
- In Python, the `sort()` method (Timsort) can use up to O(N) auxiliary space in the worst case.
- If a sorting algorithm like Heapsort were used, the space complexity would be O(log N).
- The space required for the output list `result` is not included in the auxiliary space complexity analysis.
- Apart from sorting, the algorithm uses a constant amount of extra space for variables like `i`, `j`, `left`, `right`, which is O(1).
- Therefore, the dominant factor for space is the sorting algorithm, resulting in a space complexity of O(log N) to O(N).
'''

# Test Cases
nums1 = [1,0,-1,0,-2,2], target1 = 0
print(fourSum3(nums1, target1)) # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums2 = [2,2,2,2,2], target2 = 8
print(fourSum3(nums2, target2)) # Output: [[2,2,2,2]]

nums3 = [0,0,0,0], target3 = 0
print(fourSum3(nums3, target3)) # Output: [[0,0,0,0]]

nums4 = [], target4 = 0
print(fourSum3(nums4, target4)) # Output: []

nums5 = [-2,-1,-1,1,1,2,2], target5 = 0
print(fourSum3(nums5, target5)) # Output: [[-2,-1,1,2],[-1,-1,1,1]]

nums6 = [-3,-1,0,2,4,5], target6 = 2
print(fourSum3(nums6, target6)) # Output: [[-3,-1,2,4]]

nums7 = [1,2,3,4,5], target7 = 20
print(fourSum3(nums7, target7)) # Output: []

nums8 = [1,-2,-5,-4,-3,3,3,5], target8 = -11
print(fourSum3(nums8, target8)) # Output: [[-5,-4,-3,1]]

nums9 = [1000000000,1000000000,1000000000,1000000000], target9 = -294967296
print(fourSum3(nums9, target9)) # Output: []

nums10 = [-1,0,1,2,-1,-4], target10 = -1
print(fourSum3(nums10, target10)) # Output: [[-4,0,1,2],[-1,-1,0,1]]