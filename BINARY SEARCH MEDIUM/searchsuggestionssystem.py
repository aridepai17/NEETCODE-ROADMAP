# SEARCH SUGGESTIONS SYSTEM

'''
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.
'''

'''
Algorithm and Intuition (Two Pointers with Sorting):
Intuition:
The problem requires suggesting products with a common prefix to the `searchWord` as it's typed,
and returning the lexicographically smallest three if more than three match.
Sorting the `products` array initially is crucial because it ensures that:
1. Products with the same prefix will be grouped together.
2. Within a group of products sharing a prefix, they will already be in lexicographical order,
   making it easy to pick the smallest three.
We can use two pointers, `left` and `right`, to maintain the current range of products that
still match the typed prefix. As each character of `searchWord` is typed, we narrow this range.

Algorithm Steps:
1. Sort the `products` array lexicographically. This takes O(N log N) time.
2. Initialize an empty list `result` to store the suggestions for each character.
3. Initialize `left = 0` and `right = len(products) - 1`. These pointers define the current search space.
4. Iterate through each character `char` of the `searchWord` from `i = 0` to `len(searchWord) - 1`:
   a. **Adjust `left` pointer:** While `left <= right` and either `products[left]` is too short (`len(products[left]) <= i`)
      or `products[left][i]` does not match the current `char`, increment `left`.
   b. **Adjust `right` pointer:** While `left <= right` and either `products[right]` is too short (`len(products[right]) <= i`)
      or `products[right][i]` does not match the current `char`, decrement `right`.
   c. Append an empty list to `result` to store suggestions for the current prefix.
   d. Iterate `j` from `0` up to `min(3, right - left + 1)`:
      - Add `products[left + j]` to the last sublist in `result`. This collects up to 3 matching products.
5. Return the `result` list.
'''

def suggestedProducts(products, searchWord):
    products.sort()
    result = []
    
    left = 0
    right = len(products) - 1
    
    for i in range(len(searchWord)):
        char = searchWord[i]
        
        while left <= right and (len(products[left]) <= i and products[left][i] != char):
            left += 1
        while left <= right and (len(products[right]) <= i and products[right][i] != char):
            right -= 1
            
        result.append([])
        remainder = right - left + 1
        
        for j in range(min(3, remainder)):
            result[-1].append(products[left + j])
            
    return result

'''
Time Complexity: O(N log N + L * N)
- Sorting `products`: O(N log N), where N is the number of products.
- Iterating through `searchWord`: Let L be the length of `searchWord`.
  - In each iteration (for each character `char`):
    - The two `while` loops (adjusting `left` and `right` pointers): In the worst case, these loops can iterate through all `N` products.
      However, the `left` and `right` pointers only move forward or backward, respectively, and never reset.
      Over the entire `L` iterations of the outer loop, `left` can move at most `N` times and `right` can move at most `N` times.
      So, the total cost of these two `while` loops across all `L` iterations is O(N).
    - The `for` loop to append results: This loop runs at most 3 times. Appending to `result[-1]` takes O(M) time, where M is the average length of a product string.
      So, for each character of `searchWord`, this part takes O(3 * M) = O(M).
  - Therefore, the total time for the outer loop is O(L * M + N).
- Overall, the dominant factor is O(N log N) for sorting, and then O(L * M) for the search part if M is significant, or O(L * N) if considering the worst-case pointer movements for each character.
- A more precise analysis for the search part: The `while` loops effectively narrow down the search range. For each character, we are essentially filtering the current `[left, right]` range.
  The comparison `products[left][i] != char` takes O(1) if `products[left][i]` exists, or O(1) for length check.
  The total work for the `while` loops across all `L` iterations is O(N * M) in the worst case (e.g., if all products are very long and we compare character by character).
  However, if we consider the string comparisons, it's more like O(N * M) for the filtering part.
- A common way to analyze this is O(N log N + L * N * M) where M is max product length.

Space Complexity: O(N * M + L * 3 * M)
- `products.sort()` might use O(log N) or O(N) space depending on the sort implementation (in-place vs. not).
- `result` list: Stores `L` sublists. Each sublist can store up to 3 product strings. Each product string can have a maximum length of `M`.
- So, the space for `result` is O(L * 3 * M) = O(L * M).
- Total space complexity is O(N * M + L * M) if we consider the input products as part of the space, or O(L * M) for the output.
'''

# Test Cases
products1 = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord1 = "mouse"
print(suggestedProducts(products1, searchWord1))
# Expected: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]

products2 = ["havana"], searchWord2 = "havana"
print(suggestedProducts(products2, searchWord2))
# Expected: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

products3 = ["bags","baggage","banner","box","cloths"], searchWord3 = "bags"
print(suggestedProducts(products3, searchWord3))
# Expected: [["bags","baggage","banner"],["bags","baggage","banner"],["bags","baggage"],["baggage"]]

products4 = ["apple","apricot","banana","bandana"], searchWord4 = "app"
print(suggestedProducts(products4, searchWord4))
# Expected: [["apple","apricot"],["apple","apricot"],["apple","apricot"]]

products5 = ["car","carpet","cart"], searchWord5 = "car"
print(suggestedProducts(products5, searchWord5))
# Expected: [["car","carpet","cart"],["car","carpet","cart"],["car","carpet","cart"]]

products6 = ["abc","abd","abe","abf","abg"], searchWord6 = "ab"
print(suggestedProducts(products6, searchWord6))
# Expected: [["abc","abd","abe"],["abc","abd","abe"]]

products7 = ["a","b","c"], searchWord7 = "d"
print(suggestedProducts(products7, searchWord7))
# Expected: [[],[],[]]

products8 = ["z","zebra","zoo"], searchWord8 = "z"
print(suggestedProducts(products8, searchWord8))
# Expected: [["z","zebra","zoo"]]

products9 = ["code","coder","coding","coffe","coin"], searchWord9 = "cod"
print(suggestedProducts(products9, searchWord9))
# Expected: [["code","coder","coding"],["code","coder","coding"],["code","coder","coding"]]

products10 = ["hello","hell","heaven","heavy"], searchWord10 = "heav"
print(suggestedProducts(products10, searchWord10))
# Expected: [["heaven","hell","hello"],["heaven","hell","hello"],["heaven","heavy"],["heaven","heavy"]]