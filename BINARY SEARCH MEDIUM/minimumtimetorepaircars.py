# MINIMUM TIME TO REPAIR CARS

'''
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. 
A mechanic with a rank r can repair n cars in r * n2 minutes.
You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.
Return the minimum time taken to repair all the cars.
Note: All the mechanics can repair the cars simultaneously.
'''

'''
Algorithm and Intuition (Binary Search on the Answer):
Intuition:
The problem asks for the minimum time required. The possible time can range from 1 to a very large number.
Let's consider a function `isCountRepaired(time)` which tells us if it's possible to repair the required number of `cars` within a given `time`.
If we can repair all cars in `t` minutes, we can also repair them in any time greater than `t`. 
This monotonic property (if `isCountRepaired(t)` is true, then `isCountRepaired(t+1)` is also true) allows us to use binary search to find the *minimum* `time` for which `isCountRepaired(time)` is true.
The core of the problem is to figure out how many cars a mechanic of rank `r` can repair in a given `time`.
The formula is `time = r * n^2`, where `n` is the number of cars.
Solving for `n`, we get `n = sqrt(time / r)`. Since a mechanic can only repair a whole number of cars, they can repair `floor(sqrt(time / r))` cars.

Algorithm Steps:
1.  **Define the Search Space:**
    -   `left = 1`: The minimum possible time is 1.
    -   `right = min(ranks) * cars * cars`: This is a safe upper bound. It represents the time taken if the single fastest mechanic (with the minimum rank) repaired all the cars alone.

2.  **Binary Search for the Minimum Time:**
    -   Loop while `left <= right`.
    -   Calculate `mid` as the potential minimum time.
    -   Use a helper function `isCountRepaired(mid)` to check if this `mid` time is sufficient to repair at least `cars` cars.
        -   Inside `isCountRepaired(time)`, iterate through each mechanic's rank `r`. Calculate the number of cars they can fix: `int(sqrt(time / r))`.
        -   Sum up the cars repaired by all mechanics. If the total is `>= cars`, return `True`. Otherwise, `False`.
    -   If `isCountRepaired(mid)` is `True`, it means `mid` is a possible answer. We try for an even smaller time, so we set `right = mid - 1`.
    -   If `isCountRepaired(mid)` is `False`, `mid` is too short. We need more time, so we set `left = mid + 1`.

3.  **Return the Result:**
    -   The loop terminates when `left` and `right` cross. The value of `left` will be the smallest time for which `isCountRepaired` returned `True`.
'''

from math import sqrt

def repairCars(ranks, cars):
    def isCountRepaired(time):
        count = 0
        for r in ranks:
            count += int(sqrt(time / r))
            if count >= cars:
                return True
        return False
    
    left = 1
    right = min(ranks) * cars * cars
    
    while left <= right:
        mid = (left + right) // 2
        if isCountRepaired(mid):
            right = mid - 1
        else:
            left = mid + 1
            
    return left

'''
Time Complexity: O(R * log(min_rank * cars^2))
- The binary search operates on the range [1, min(ranks) * cars^2].
  The upper bound is derived from the worst-case scenario where one mechanic with the smallest rank repairs all cars.
  The number of iterations for the binary search is O(log(min_rank * cars^2)).
- Inside the `while` loop, the `isCountRepaired` function is called.
- The `isCountRepaired` function iterates through the `ranks` array once.
  Let R be the number of mechanics (len(ranks)). This takes O(R) time.
- The `sqrt` operation is typically O(1) for standard floating-point numbers.
- Therefore, the total time complexity is O(R * log(min_rank * cars^2)).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for variables: `left`, `right`, `mid`, `count`, `r`, `time`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
ranks1 = [4,2,3,1], cars1 = 10
print(repairCars(ranks1, cars1)) # Output: 16

ranks2 = [1], cars2 = 1
print(repairCars(ranks2, cars2)) # Output: 1

ranks3 = [10], cars3 = 10
print(repairCars(ranks3, cars3)) # Output: 1000

ranks4 = [1, 1, 1], cars4 = 10
print(repairCars(ranks4, cars4)) # Output: 9

ranks5 = [2, 3], cars5 = 5
print(repairCars(ranks5, cars5)) # Output: 18

ranks6 = [5, 1], cars6 = 7
print(repairCars(ranks6, cars6)) # Output: 25

ranks7 = [100], cars7 = 1
print(repairCars(ranks7, cars7)) # Output: 100

ranks8 = [1, 2, 3, 4, 5], cars8 = 15
print(repairCars(ranks8, cars8)) # Output: 36

ranks9 = [1, 1, 1, 1, 1], cars9 = 100
print(repairCars(ranks9, cars9)) # Output: 400

ranks10 = [7, 8, 9], cars10 = 20
print(repairCars(ranks10, cars10)) # Output: 112