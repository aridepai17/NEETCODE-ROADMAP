# MOST BEAUTIFUL ITEM FOR EACH QUERY

'''
You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.
You are also given a 0-indexed integer array queries. 
For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. 
If no such item exists, then the answer to this query is 0.
Return an array answer of the same length as queries where answer[j] is the answer to the jth query.
'''

'''
Algorithm and Intuition (Optimized Binary Search Solution):
Intuition:
The problem asks to find the maximum beauty for items whose price is less than or equal to a given query price.
A naive approach (brute force) would iterate through all items for each query, leading to O(Q*N) complexity, which is too slow.
The key insight for optimization is that if we sort both the `items` by price and the `queries` by value,
we can process them efficiently using a two-pointer approach.
When queries are sorted, as the query price increases, the set of eligible items (price <= query) can only grow or stay the same.
This allows us to maintain a `maxBeauty` seen so far among eligible items without re-scanning.

Algorithm Steps:
1. Sort the `items` array based on their prices in ascending order. This takes O(N log N).
2. Create a new list `sortedQueries` that stores tuples of `(query_value, original_index)`. This is necessary to reconstruct the result in the original query order.
3. Sort `sortedQueries` based on `query_value` in ascending order. This takes O(Q log Q).
4. Initialize `result` as an array of zeros with the same length as the original `queries` array.
5. Initialize `maxBeauty = 0` to keep track of the maximum beauty encountered for items whose price is less than or equal to the current query.
6. Initialize `itemPointer = 0` to iterate through the sorted `items` array.
7. Iterate through each `(value, original_index)` in `sortedQueries`:
   a. While `itemPointer` is within the bounds of `items` and the price of `items[itemPointer]` is less than or equal to the current `value` (query price):
      - Update `maxBeauty = max(maxBeauty, items[itemPointer][1])` (the beauty of the current item).
      - Increment `itemPointer` to consider the next item.
   b. Assign the current `maxBeauty` to `result[original_index]`. This ensures the result is stored at the correct position corresponding to the original query.
8. Return the `result` array.
'''

# Brute Force Solution ( Time Limit Exceeded )
def maximumBeauty(items, queries):
    result = []
    
    for q in queries:
        maxBeauty = 0
        for price, beauty in items:
            if price <= q:
                maxBeauty = max(maxBeauty, beauty)
        result.append(maxBeauty)
        
    return result
'''
Time Complexity: O(Q * N)
- The outer loop iterates through each query, which is Q times.
- The inner loop iterates through all items for each query, which is N times.
- Inside the inner loop, operations like comparison and `max` take O(1) time.
- Therefore, the total time complexity is O(Q * N).

Space Complexity: O(Q)
- The `result` list stores an answer for each query.
- The size of the `result` list is equal to the number of queries, Q.
- No other significant data structures are used that scale with input size.
- Therefore, the space complexity is O(Q) for the output.
'''

# Optimized Binary Search Solution
def maximumBeauty(items, queries):
    items.sort()
    sortedQueries = []
    for index in range(len(queries)):
        sortedQueries.append((queries[index], index))
    sortedQueries.sort()

    result = [0] * len(queries)
    maxBeauty = 0
    itemPointer = 0

    for value, index in sortedQueries:
        while itemPointer < len(items) and items[itemPointer][0] <= value:
            price, beauty = items[itemPointer]
            maxBeauty = max(maxBeauty, beauty)
            itemPointer += 1

        result[index] = maxBeauty

    return result

'''
Time Complexity: O(N log N + Q log Q + N + Q) which simplifies to O(N log N + Q log Q)
- Sorting `items`: O(N log N), where N is the number of items.
- Creating `sortedQueries` and sorting it: O(Q log Q), where Q is the number of queries.
  - Creating the list of tuples takes O(Q).
  - Sorting this list takes O(Q log Q).
- Iterating through `sortedQueries`: O(Q) iterations.
  - Inside the loop, the `while` loop (itemPointer advancement): The `itemPointer` starts at 0 and goes up to `N`. It never resets. So, the total number of times `itemPointer` is incremented across all `Q` iterations of the outer loop is at most `N`.
  - The `max` operation and assignment are O(1).
  - Assigning to `result[index]` is O(1).
- Therefore, the total time complexity is dominated by the sorting steps: O(N log N + Q log Q).

Space Complexity: O(N + Q)
- `items.sort()`: If in-place, O(log N) or O(N) depending on implementation.
- `sortedQueries`: Stores Q tuples, each containing an integer and an index. This takes O(Q) space.
- `result`: Stores Q integers. This takes O(Q) space.
- `maxBeauty`, `itemPointer`, `value`, `index`, `price`, `beauty` are all O(1) space.
- Total auxiliary space complexity is O(Q) for `sortedQueries` and `result`.
- If we consider the input `items` as part of the space, then O(N) for `items`.
- Overall, the space complexity is O(N + Q).
'''

# Test Cases
items1 = [[1,2],[3,2],[2,4],[5,3]], queries1 = [3,1,2,6]
print(maximumBeauty(items1, queries1))
# Expected: [4,2,4,3]

items2 = [[1,1],[4,2],[2,3],[5,4]], queries2 = [2,3,5]
print(maximumBeauty(items2, queries2))
# Expected: [3,3,4]

items3 = [[10,1000]], queries3 = [5]
print(maximumBeauty(items3, queries3))
# Expected: [0]

items4 = [[1,10],[2,20],[3,30]], queries4 = [1,2,3,4]
print(maximumBeauty(items4, queries4))
# Expected: [10,20,30,30]

items5 = [[1,1],[1,2],[1,3]], queries5 = [1]
print(maximumBeauty(items5, queries5))
# Expected: [3]

items6 = [[1,5],[2,3],[3,7],[4,2]], queries6 = [2,4,1,5]
print(maximumBeauty(items6, queries6))
# Expected: [5,7,5,7]

items7 = [[10,10],[20,20],[30,30]], queries7 = [5,15,25,35]
print(maximumBeauty(items7, queries7))
# Expected: [0,10,20,30]

items8 = [[1,100],[100,1]], queries8 = [50]
print(maximumBeauty(items8, queries8))
# Expected: [100]

items9 = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries9 = [0,1,2,3,4,5,6]
print(maximumBeauty(items9, queries9))
# Expected: [0,1,2,3,4,5,5]

# Test Case 10: Empty items list
items10 = [], queries10 = [1, 5, 10]
print(maximumBeauty(items10, queries10))
# Expected: [0, 0, 0]