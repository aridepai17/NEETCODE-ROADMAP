# 3 SUM

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

# Solution 1: Using 3 For Loops
def threeSum1(nums):
    n = len(nums)
    ans = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                    ans.add(triplet)
                    
    final = []
    for triplet in ans:
        final.append(triplet)
        
    return final

'''
Time Complexity: O(n^3)
- Three nested loops iterate through all possible combinations of triplets
- Each iteration performs constant time operations (addition, sorting 3 elements, set operations)
- Total iterations: n * (n-1) * (n-2) / 6 ≈ O(n^3)

Space Complexity: O(k) where k is the number of unique triplets
- The set 'ans' stores unique triplets that sum to zero
- The list 'final' stores the same triplets in list format
- In the worst case, there could be O(n^2) unique triplets
- Therefore, space complexity is O(k) where k ≤ n^2
'''

# Solution 2: Using Two For Loops and HashSet
def threeSum2(nums):
    hashSet = set()
    n = len(nums)
    
    for i in range(n):
        seen = set()
        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])
            
            if third in seen:
                triplet = tuple(sorted((nums[i], nums[j], third)))
                hashSet.add(triplet)
                
            seen.add(nums[j])
            
    answer = list(hashSet)
    return answer

'''
Time Complexity: O(n^2)
- The outer loop iterates 'n' times, where 'n' is the number of elements in `nums`.
- The inner loop iterates up to 'n-1' times for each iteration of the outer loop.
- Inside the inner loop, operations like calculating the 'third' element, checking for its existence in the 'seen' set, and adding elements to sets are all O(1) on average.
- The nested loop structure is the dominant factor, leading to a time complexity of O(n^2).

Space Complexity: O(n + k) where k is the number of unique triplets
- 'hashSet' is used to store the unique triplets that sum to zero. The space required is proportional to the number of unique triplets, 'k'.
- 'seen' is a hash set created in each iteration of the outer loop. It can store up to 'n' elements in the worst case to keep track of numbers seen so far for a given `nums[i]`.
- Therefore, the total space complexity is the sum of the space for the 'seen' set and the 'hashSet', which is O(n + k).
'''

# Solution 3: Two Pointers Approach
def threeSum3(nums):
    nums.sort()
    answer = []
    n = len(nums)
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if currentSum < 0:
                left += 1
            elif currentSum > 0:
                right -= 1
            else:
                result = [nums[i], nums[left], nums[right]]
                answer.append(result)               
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                    
    return answer

'''
Time Complexity: O(N^2)
- Sorting the input array `nums` takes O(N log N) time.
- The main logic involves a loop that iterates through each element of the sorted array. This outer loop runs N times.
- Inside this loop, we use a two-pointer approach (`left` and `right`) on the rest of the array. In the worst case, these two pointers traverse the subarray, which takes O(N) time.
- The combination of the outer loop and the inner two-pointer scan results in a time complexity of O(N * N) = O(N^2).
- Since O(N^2) is greater than O(N log N), the overall time complexity is dominated by the nested loop structure, making it O(N^2).

Space Complexity: O(log N) or O(N)
- The space complexity depends on the implementation of the sorting algorithm.
- In Python, the `sort()` method is implemented using Timsort, which requires O(N) auxiliary space in the worst case.
- If we use a sorting algorithm with a lower space complexity like Heapsort, it could be O(log N).
- The space required for the output list `answer` is not included in the auxiliary space complexity analysis.
- Apart from the sorting, the algorithm uses a constant amount of extra space for variables, which is O(1).
- Therefore, the dominant factor for space is the sorting algorithm, resulting in a space complexity of O(log N) to O(N).
'''

# Test Cases
nums1 = [-1,0,1,2,-1,-4]
print(threeSum3(nums1)) # Output: [[-1,-1,2],[-1,0,1]]

nums2 = [0,1,1]
print(threeSum3(nums2)) # Output: []

nums3 = [0,0,0]
print(threeSum3(nums3)) # Output: [[0,0,0]]

nums4 = [0,0,0,0]
print(threeSum3(nums4)) # Output: [[0,0,0]]

nums5 = [-2,0,1,1,2]
print(threeSum3(nums5)) # Output: [[-2,0,2],[-2,1,1]]

nums6 = [1,2,3,4,5]
print(threeSum3(nums6)) # Output: []

nums7 = [-5,-4,-3,-2,-1]
print(threeSum3(nums7)) # Output: []

nums8 = [3,0,-2,-1,1,2]
print(threeSum3(nums8)) # Output: [[-2,-1,3],[-2,0,2],[-1,0,1]]

nums9 = []
print(threeSum3(nums9)) # Output: []

nums10 = [-1, -1, -1, 2, 2, 2]
print(threeSum3(nums10)) # Output: [[-1,-1,2]]