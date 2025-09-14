# PATH CROSSING

'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. 
Return false otherwise.
'''

def ispathCrossing(path):
    direction = {
        "N" : [0, 1],
        "S" : [0, -1],
        "E" : [1, 0],
        "W" : [0, -1]
    }
    
    cross = set()
    x, y = 0, 0
    
    for i in path:
        cross.add((x, y))
        dx, dy = direction[i]
        x, y = x + dx, y + dy
        if (x, y) in cross:
            return True
        
    return False

'''
Time Complexity: O(N)
- Let N be the length of the input string `path`.
- The algorithm iterates through each character of the `path` string exactly once.
- Inside the loop, all operations—adding a tuple to a set (`cross.add`), dictionary lookup (`direction[i]`), and checking for an element in a set (`in cross`)—take constant time on average, O(1).
- Therefore, the overall time complexity is proportional to the length of the path, resulting in O(N).

Space Complexity: O(N)
- The algorithm uses a set `cross` to store the coordinates of all visited points.
- In the worst-case scenario, the path does not cross itself, and every position visited is unique.
- The number of unique points visited can be up to N + 1 (including the starting origin).
- Thus, the space required for the set grows linearly with the length of the input path.
- Therefore, the space complexity is O(N).
'''

# Test Cases
path1 = "NES"
print(ispathCrossing(path1)) # Output: False

path2 = "NESWW"
print(ispathCrossing(path2)) # Output: True

path3 = "NNS"
print(ispathCrossing(path3)) # Output: True

path4 = "E"
print(ispathCrossing(path4)) # Output: False

path5 = "NEWS"
print(ispathCrossing(path5)) # Output: True

path6 = "S"
print(ispathCrossing(path6)) # Output: False

path7 = "W"
print(ispathCrossing(path7)) # Output: False

path8 = "NESW"
print(ispathCrossing(path8)) # Output: True

path9 = "ENW"
print(ispathCrossing(path9)) # Output: False

path10 = "NWSENSS"
print(ispathCrossing(path10)) # Output: True