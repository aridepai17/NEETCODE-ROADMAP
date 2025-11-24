# FIND MOUNTAIN ARRAY

'''
This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. 
If such an index does not exist, return -1.
You cannot access the mountain array directly. You may only access the array using a MountainArray interface:
MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. 
Also, any solutions that attempt to circumvent the judge will result in disqualification.
'''

'''
Algorithm and Intuition (Binary Search):
Intuition:
A mountain array has a unique peak element. The array is strictly increasing up to the peak and strictly decreasing afterwards.
This structure allows us to use binary search in three phases:
1. Find the peak element: The peak element is the largest element in the array. We can find it using binary search.
   - If `arr[mid-1] < arr[mid] < arr[mid+1]`, we are on the increasing slope, so the peak is to the right.
   - If `arr[mid-1] > arr[mid] > arr[mid+1]`, we are on the decreasing slope, so the peak is to the left.
   - If `arr[mid-1] < arr[mid]` and `arr[mid] > arr[mid+1]`, then `mid` is the peak.
   - Note: The problem statement implies `arr[0] < arr[1]` and `arr[length-2] > arr[length-1]`, so the peak cannot be at index 0 or length-1.
2. Search in the left (increasing) portion: Once the peak is found, the left part of the array (from index 0 to peak-1) is strictly increasing. We can perform a standard binary search here.
3. Search in the right (decreasing) portion: The right part of the array (from peak+1 to length-1) is strictly decreasing. We can perform a modified binary search here (where `value < target` means search left, and `value > target` means search right).

The constraint of at most 100 calls to `MountainArray.get()` is crucial. Binary search is efficient in terms of calls.

Algorithm Steps:
1. Find the length of the array using `mountainArr.length()`.
2. **Find the Peak Element:**
   - Use binary search on the range `[1, length - 2]` to find the peak index.
   - In each step, get `arr[mid-1]`, `arr[mid]`, `arr[mid+1]`. Adjust `left` or `right` based on the slope.
3. **Search Left Portion (0 to peak):**
   - Perform a standard binary search on the range `[0, peak]`. If `target` is found, return its index.
4. **Search Right Portion (peak+1 to length-1):**
   - Perform a binary search on the range `[peak + 1, length - 1]`. This is a decreasing array, so adjust the binary search logic:
     - If `value < target`, the target must be to the left (larger values), so `right = mid - 1`.
     - If `value > target`, the target must be to the right (smaller values), so `left = mid + 1`.
   - If `target` is found, return its index.
5. If `target` is not found in either portion, return -1.
'''

def findInMountainArray(target, mountainArr) -> int:
        length = mountainArr.length()
        left = 1
        right = length - 2

        # Find Peak Element
        while left <= right:
            mid = (left + right) // 2
            l = mountainArr.get(mid - 1)
            m = mountainArr.get(mid)
            r = mountainArr.get(mid + 1)

            if l < m < r:
                left = mid + 1
            elif l > m > r:
                right = mid - 1
            else:
                break
        peak = mid

        # Search Left Portion
        l = 0
        r = peak

        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)

            if value < target:
                l = m + 1
            elif value > target:
                r = m - 1
            else:
                return m

        # Search Right Portion
        l = peak + 1
        r = length - 1

        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)
            
            if value < target:
                r = m - 1
            elif value > target:
                l = m + 1
            else:
                return m

        return -1

'''
Time Complexity Analysis: O(log(length))
The problem statement specifies a constraint on the number of calls to `MountainArray.get()`, which is 100.
This implies that the solution must be efficient in terms of array accesses.

1. Finding the Peak Element:
   - This is a binary search on the range `[1, length - 2]`.
   - In each step, we make 3 calls to `mountainArr.get()` (`mid-1`, `mid`, `mid+1`).
   - The number of iterations is `log(length)`.
   - So, finding the peak takes `O(3 * log(length))` calls to `get()`.

2. Searching the Left Portion:
   - This is a binary search on the range `[0, peak]`.
   - In each step, we make 1 call to `mountainArr.get()` (`m`).
   - The number of iterations is `log(peak + 1)`.
   - So, searching the left portion takes `O(log(peak))` calls to `get()`.

3. Searching the Right Portion:
   - This is a binary search on the range `[peak + 1, length - 1]`.
   - In each step, we make 1 call to `mountainArr.get()` (`m`).
   - The number of iterations is `log(length - 1 - peak)`.
   - So, searching the right portion takes `O(log(length - peak))` calls to `get()`.

Total calls to `get()`: `O(3 * log(length) + log(peak) + log(length - peak))`.
Since `peak` is at most `length`, this simplifies to `O(log(length))`.
Given `length` can be up to 10000, `log2(10000)` is approximately 13-14.
So, `3 * 14 + 14 + 14 = 42 + 28 = 70` calls, which is well within the 100 call limit.

Space Complexity Analysis: O(1)
The algorithm uses a constant amount of extra space for variables like `length`, `left`, `right`, `mid`, `l`, `m`, `r`, `peak`, `value`.
It does not use any data structures that scale with the input size.
Therefore, the space complexity is O(1).
'''

# Test Cases
mountainArr1 = [1,2,3,4,5,3,1], target1 = 3
print(findInMountainArray(mountainArr1, target1)) # Output: 2

mountainArr2 = [0,1,2,4,2,1], target2 = 3
print(findInMountainArray(mountainArr2, target2)) # Output: -1

mountainArr3 = [0,5,3,1], target3 = 1
print(findInMountainArray(mountainArr3, target3)) # Output: 3

mountainArr4 = [0,1,2,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0], target4 = 7
print(findInMountainArray(mountainArr4, target4)) # Output: 6

mountainArr5 = [1,5,2], target5 = 2
print(findInMountainArray(mountainArr5, target5)) # Output: 2

mountainArr6 = [0,1,0], target6 = 1
print(findInMountainArray(mountainArr6, target6)) # Output: 1

mountainArr7 = [0,5,10,5,0], target7 = 10
print(findInMountainArray(mountainArr7, target7)) # Output: 2

mountainArr8 = [0,2,4,8,16,8,4,2,0], target8 = 4
print(findInMountainArray(mountainArr8, target8)) # Output: 2

mountainArr9 = [1,3,5,4,2], target9 = 6
print(findInMountainArray(mountainArr9, target9)) # Output: -1

mountainArr10 = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0], target10 = 0
print(findInMountainArray(mountainArr10, target10)) # Output: 0