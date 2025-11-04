# VALID SUDOKU

'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
'''

# Solution 1: Using Normal {}
def isValidSudoku(board):
    rows = {}
    cols = {}
    boxes = {}
    
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == ".":
                continue
            
            boxKey = (r // 3, c // 3)
            if r not in rows:
                rows[r] = set()
            if c not in cols:
                cols[c] = set()
            if boxKey not in boxes:
                boxes[boxKey] = set()
                
            if (value in rows[r] or value in cols[c] or value in boxes[boxKey]):
                return False
            
            rows[r].add(value)
            cols[c].add(value)
            boxes[boxKey].add(value)
            
    return True

'''
Time Complexity: O(1)
- The board is always 9x9, so we iterate through a constant 81 cells.
- For each cell, we perform constant-time operations: checking membership in sets (O(1) average) and adding to sets (O(1) average).
- Since the input size is fixed (9x9), the time complexity is O(1).

Space Complexity: O(1)
- We use three dictionaries (rows, cols, boxes) to store sets of seen values.
- In the worst case:
  - `rows` can have at most 9 keys (one per row), each with a set of at most 9 elements.
  - `cols` can have at most 9 keys (one per column), each with a set of at most 9 elements.
  - `boxes` can have at most 9 keys (one per 3x3 box), each with a set of at most 9 elements.
- The total space is bounded by 9 * 9 * 3 = 243 elements, which is constant.
- Therefore, the space complexity is O(1).
'''

# Solution 2: Using defaultdict(set)
def isValidSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)
    
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == ".":
                continue
            boxKey = (r // 3, c // 3)
            if (value in rows[r] or value in cols[c] or value in boxes[boxKey]):
                return False
            
            rows[r].add(value)
            cols[c].add(value)
            boxes[boxKey].add(value)
            
    return True

'''
Time Complexity: O(1)
- The board is always 9x9, so we iterate through a constant 81 cells.
- For each cell, we perform constant-time operations: checking membership in sets (O(1) average) and adding to sets (O(1) average).
- Since the input size is fixed (9x9), the time complexity is O(1).

Space Complexity: O(1)
- We use three defaultdict(set) objects (rows, cols, boxes) to store sets of seen values.
- In the worst case:
  - `rows` can have at most 9 keys (one per row), each with a set of at most 9 elements.
  - `cols` can have at most 9 keys (one per column), each with a set of at most 9 elements.
  - `boxes` can have at most 9 keys (one per 3x3 box), each with a set of at most 9 elements.
- The total space is bounded by 9 * 9 * 3 = 243 elements, which is constant.
- Therefore, the space complexity is O(1).
'''

# Test Cases
board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board1)) # Output: True

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board2)) # Output: False

board3 = [[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","."]
,[".",".",".",".",".","3",".",".","1"]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board3)) # Output: False

board4 = [[".",".",".",".",".",".",".",".","2"]
,[".",".",".",".",".",".","6",".","."]
,[".",".","1","4",".",".","8",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".","3",".",".",".","."]
,["5",".","8","6",".",".",".",".","9"]
,[".",".",".",".",".",".","4",".","."]
,[".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board4)) # Output: True

board5 = [[".",".","4",".",".",".","6","3","."]
,[".",".",".",".",".",".",".",".","."]
,["5",".",".",".",".",".",".","9","."]
,[".",".",".",".",".",".","4",".","7"]
,[".",".",".",".",".",".",".",".","5"]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".","2",".",".",".",".","1"]
,[".",".",".",".",".",".",".",".","8"]
,[".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board5)) # Output: False

board6 = [["1","2","3","4","5","6","7","8","9"]
,["4","5","6","7","8","9","1","2","3"]
,["7","8","9","1","2","3","4","5","6"]
,["2","3","4","5","6","7","8","9","1"]
,["5","6","7","8","9","1","2","3","4"]
,["8","9","1","2","3","4","5","6","7"]
,["3","4","5","6","7","8","9","1","2"]
,["6","7","8","9","1","2","3","4","5"]
,["9","1","2","3","4","5","6","7","8"]]
print(isValidSudoku(board6)) # Output: True

board7 = [["1","2","3","4","5","6","7","8","9"]
,["2","3","4","5","6","7","8","9","1"]
,["3","4","5","6","7","8","9","1","2"]
,["4","5","6","7","8","9","1","2","3"]
,["5","6","7","8","9","1","2","3","4"]
,["6","7","8","9","1","2","3","4","5"]
,["7","8","9","1","2","3","4","5","6"]
,["8","9","1","2","3","4","5","6","7"]
,["9","1","2","3","4","5","6","7","8"]]
print(isValidSudoku(board7)) # Output: False

board8 = [[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board8)) # Output: True

board9 = [["7",".",".",".","4",".",".",".","."]
,[".",".",".","8","6","5",".",".","."]
,[".","1",".","2",".",".",".",".","."]
,[".",".",".",".",".","9",".",".","."]
,[".",".",".",".","5",".","5",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".","2",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board9)) # Output: False

board10 = [[".",".",".",".",".",".","5",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,["9","3",".",".","2",".","4",".","."]
,[".",".","7",".",".",".","3",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","8"]
,[".",".",".",".",".",".",".","7","."]
,[".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board10)) # Output: True