# DESTINATION CITY

'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
'''

def destinationCity(paths):
    visited = set()
    
    for path in paths:
        visited.add(path[0])
    
    for path in paths:
        if path[1] not in visited:
            return path[1]
        
'''
Time Complexity: O(N)
- N is the number of paths.
- The first loop iterates through all N paths to populate the set of starting cities. Adding to a set is O(1) on average. So, this loop is O(N).
- The second loop also iterates through all N paths. Checking for an element in a set is O(1) on average. So, this loop is also O(N).
- The total time complexity is O(N) + O(N) = O(N).

Space Complexity: O(N)
- We use a set to store all the starting cities.
- In the worst case, all N starting cities are unique, so the set will store N elements.
- Therefore, the space complexity is O(N).
'''

# Test Cases
paths1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destinationCity(paths1)) # Output: "Sao Paulo"

paths2 = [["A", "B"]]
print(destinationCity(paths2)) # Output: "B"

paths3 = [["B","C"],["D","B"],["C","A"]]
print(destinationCity(paths3)) # Output: "A"

paths4 = [["JFK","SFO"]]
print(destinationCity(paths4)) # Output: "SFO"

paths5 = [["p","q"],["q","r"],["r","s"]]
print(destinationCity(paths5)) # Output: "s"

paths6 = [["Z", "Y"], ["Y", "X"], ["X", "W"]]
print(destinationCity(paths6)) # Output: "W"

paths7 = [["b", "a"], ["c", "b"], ["d", "c"]]
print(destinationCity(paths7)) # Output: "a"

paths8 = [["Paris", "Skopje"]]
print(destinationCity(paths8)) # Output: "Skopje"

paths9 = [["Ushuaia", "Buenos Aires"], ["Buenos Aires", "Santiago"], ["Santiago", "Lima"]]
print(destinationCity(paths9)) # Output: "Lima"

paths10 = [["q", "z"], ["z", "w"], ["w", "e"], ["e", "p"]]
print(destinationCity(paths10)) # Output: "p"