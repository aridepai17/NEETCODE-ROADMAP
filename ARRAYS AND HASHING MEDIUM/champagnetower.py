# CHAMPAGNE TOWER

'''
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row. 
Each glass holds one cup of champagne.
Then, some champagne is poured into the first glass at the top. 
When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  
When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  
(A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full. 
After two cups of champagne are poured, the two glasses on the second row are half full. 
After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now. 
Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)
'''

def champagneTower(poured, query_row, query_glass):
    row = [poured]
    
    for r in range(query_row):
        nextRow = [0] * (r + 2)
        for index, value in enumerate(row):
            overflow = max(0, value - 1)
            nextRow[index] += overflow / 2
            nextRow[index + 1] += overflow / 2
        row = nextRow
        
    return min(1, row[query_glass])

'''
Time Complexity: O(query_row^2)
- Let R be the value of `query_row`.
- The outer loop runs R times (from 0 to query_row - 1).
- In iteration r, the inner loop processes r + 1 elements (the length of the current row).
- The total number of operations is: 1 + 2 + 3 + ... + R = R * (R + 1) / 2, which is O(R^2).
- Therefore, the overall time complexity is O(query_row^2).

Space Complexity: O(query_row)
- The `row` list stores the champagne amounts for the current row being processed.
- In each iteration r, the `nextRow` list has a size of r + 2.
- The maximum size occurs at the last iteration, where the row has query_row + 1 elements.
- Therefore, the space complexity is O(query_row) for storing the row.
'''

# Test Cases
poured1 = 1, query_row1 = 1, query_glass1 = 1
print(champagneTower(poured1, query_row1, query_glass1)) # Output: 0.0

poured2 = 2, query_row2 = 1, query_glass2 = 1
print(champagneTower(poured2, query_row2, query_glass2)) # Output: 0.5

poured3 = 100000009, query_row3 = 33, query_glass3 = 17
print(champagneTower(poured3, query_row3, query_glass3)) # Output: 1.0

poured4 = 4, query_row4 = 2, query_glass4 = 1
print(champagneTower(poured4, query_row4, query_glass4)) # Output: 0.5

poured5 = 0, query_row5 = 0, query_glass5 = 0
print(champagneTower(poured5, query_row5, query_glass5)) # Output: 0.0

poured6 = 10, query_row6 = 3, query_glass6 = 2
print(champagneTower(poured6, query_row6, query_glass6)) # Output: 0.75

poured7 = 25, query_row7 = 4, query_glass7 = 2
print(champagneTower(poured7, query_row7, query_glass7)) # Output: 1.0

poured8 = 5, query_row8 = 2, query_glass8 = 0
print(champagneTower(poured8, query_row8, query_glass8)) # Output: 0.625

poured9 = 3, query_row9 = 1, query_glass9 = 0
print(champagneTower(poured9, query_row9, query_glass9)) # Output: 1.0

poured10 = 7, query_row10 = 2, query_glass10 = 2
print(champagneTower(poured10, query_row10, query_glass10)) # Output: 0.625