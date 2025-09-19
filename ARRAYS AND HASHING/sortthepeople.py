# SORT THE PEOPLE

'''
You are given an array of strings names, and an array heights that consists of distinct positive integers. 
Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.
'''

def sortPeople(names, heights):
    people = []
    
    for i in range(len(names)):
        people.append((heights[i], names[i]))
        
    people.sort(reverse = True)
    
    sortedNames = []
    
    for height, name in people:
        sortedNames.append(name)
        
    return sortedNames

'''
Time Complexity: O(N log N)
Let N be the number of people (i.e., the length of the `names` and `heights` arrays).
- The first `for` loop iterates N times to create a list of tuples `people`. Each append operation is O(1) on average. This step takes O(N) time.
- The `people.sort()` method is then called. The time complexity of Python's built-in sort (Timsort) is O(N log N).
- The second `for` loop iterates N times to extract the names from the sorted list of tuples into a new list. This step takes O(N) time.
- The total time complexity is the sum of these steps: O(N) + O(N log N) + O(N), which is dominated by the sorting step. Thus, the overall time complexity is O(N log N).

Space Complexity: O(N)
- A list `people` is created to store N tuples, where each tuple contains a height and a name. This requires O(N) space.
- The `sortedNames` list is created to store the N sorted names, which also requires O(N) space.
- The space complexity of Python's `sort()` method can be up to O(N) in the worst case for temporary storage.
- Therefore, the total auxiliary space required is proportional to N, resulting in an overall space complexity of O(N).
'''

# Test Cases
names1 = ["Mary","John","Emma"], heights1 = [180,165,170]
print(sortPeople(names1, heights1)) # Output: ["Mary", "Emma", "John"]

names2 = ["Alice","Bob","Bob"], heights2 = [155,185,150]
print(sortPeople(names2, heights2)) # Output: ["Bob", "Alice", "Bob"]

names3 = [], heights3 = []
print(sortPeople(names3, heights3)) # Output: []

names4 = ["David"], heights4 = [160]
print(sortPeople(names4, heights4)) # Output: ["David"]

names5 = ["Iker", "Jose", "Peter", "Frank"], heights5 = [175, 190, 165, 188]
print(sortPeople(names5, heights5)) # Output: ["Jose", "Frank", "Iker", "Peter"]

names6 = ["Eve", "Frank", "Grace"], heights6 = [160, 170, 180]
print(sortPeople(names6, heights6)) # Output: ["Grace", "Frank", "Eve"]

names7 = ["Bob", "Charlie", "David"], heights7 = [190, 185, 180]
print(sortPeople(names7, heights7)) # Output: ["Bob", "Charlie", "David"]

names8 = ["Liam", "Noah", "Oliver"], heights8 = [178, 179, 177]
print(sortPeople(names8, heights8)) # Output: ["Noah", "Liam", "Oliver"]

names9 = ["Ava", "Mia", "Isabella"], heights9 = [162, 172, 158]
print(sortPeople(names9, heights9)) # Output: ["Mia", "Ava", "Isabella"]

names10 = ["James", "William", "Henry", "George", "Charles"], heights10 = [181, 176, 182, 192, 175]
print(sortPeople(names10, heights10)) # Output: ["George", "Henry", "James", "William", "Charles"]