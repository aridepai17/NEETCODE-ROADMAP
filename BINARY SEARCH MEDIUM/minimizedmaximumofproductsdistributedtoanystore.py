# MINIMIZED MAXIMUM OF PRODUCTS DISTRIBUTED TO A STORE

'''
You are given an integer n indicating there are n specialty retail stores. 
There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.
You need to distribute all products to the retail stores following these rules:
- A store can only be given at most one product type but can be given any amount of it.
- After distribution, each store will have been given some number of products (possibly 0). 
- Let x represent the maximum number of products given to any store. 
- You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
Return the minimum possible x.
'''

"""
Algorithm (step by step):
1. Let the answer x be the maximum number of products any store receives. The minimum possible x is 1, and the maximum possible x is max(quantities).
2. Define a feasibility check canDistribute(x):
   - For each product amount q in quantities, compute how many stores are needed if no store gets more than x units of that product:
       stores_needed_for_q = ceil(q / x) = (q + x - 1) // x.
   - Sum across all product types: total_stores = sum(ceil(q / x)).
   - If total_stores <= n, then it is feasible to distribute with maximum per-store load x; otherwise it is not.
3. Binary search the minimal feasible x in the range [1, max(quantities)]:
   - mid = (left + right) // 2.
   - If canDistribute(mid) is True, move right to mid - 1 to try a smaller maximum; record candidate.
   - Else, move left to mid + 1 to allow a larger maximum.
4. When the loop finishes, left is the smallest x for which canDistribute(x) is True. Return left.
"""

def minimizedMaximum(n, quantities):
    def canDistribute(mid):
        stores = 0
        for q in quantities:
            stores += (q + mid - 1) // mid # Finding the Ceil
        if stores > n:
            return False
        return True
    
    left = 1
    right = max(quantities)
    
    while left <= right:
        mid = (left + right) // 2
        if canDistribute(mid):
            right = mid - 1
        else:
            left = mid + 1
            
    return left

'''
Time Complexity: O(m · log U)
- Let m = len(quantities) and U = max(quantities).
- Binary search over x in [1, U] takes O(log U) iterations.
- Each feasibility check canDistribute runs in O(m) time (single pass over quantities with O(1) work per type).
- Total time: O(m · log U).

Space Complexity: O(1)
- O(1) auxiliary space. Uses a constant number of scalar variables; no additional data structures proportional to input size.
'''

# Test Cases
n1 = 6
quantities1 = [11, 6]
print(minimizedMaximum(n1, quantities1)) # Expected: 3

n2 = 7
quantities2 = [15, 10, 10]
print(minimizedMaximum(n2, quantities2)) # Expected: 5

n3 = 3
quantities3 = [8]
print(minimizedMaximum(n3, quantities3))  # Expected: 3

n4 = 4
quantities4 = [7, 7, 7, 7]
print(minimizedMaximum(n4, quantities4))  # Expected: 7

n5 = 4
quantities5 = [1, 1, 1, 1]
print(minimizedMaximum(n5, quantities5))  # Expected: 1

n6 = 10
quantities6 = [100]
print(minimizedMaximum(n6, quantities6))  # Expected: 10

n7 = 5
quantities7 = [2, 8, 4]
print(minimizedMaximum(n7, quantities7))  # Expected: 4

n8 = 8
quantities8 = [9, 9, 9]
print(minimizedMaximum(n8, quantities8))  # Expected: 4

n9 = 2
quantities9 = [1, 100]
print(minimizedMaximum(n9, quantities9))  # Expected: 100

n10 = 9
quantities10 = [2, 2, 2, 2, 2]
print(minimizedMaximum(n10, quantities10))  # Expected: 2