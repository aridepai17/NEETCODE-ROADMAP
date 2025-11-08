# ROBOT COLLISIONS

'''
There are n 1-indexed robots, each having a position on a line, health, and movement direction.
You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right).
All integers in positions are unique.
All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.
If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. 
If both robots have the same health, they are both removed from the line.
Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on.
If there are no survivors, return an empty array.
Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.
Note: The positions may be unsorted.
'''

def robotCollisions(positions, healths, directions):
    hashMap = {}
    
    for i in range(len(positions)):
        p = positions[i]
        hashMap[p] = i
        
    stack = []
    for p in sorted(positions):
        i = hashMap[p]
        if directions[i] == "R":
            stack.append(i)
        else:
            while stack and healths[i]:
                j = stack.pop()
                if healths[i] > healths[j]:
                    healths[j] = 0
                    healths[i] -= 1
                elif healths[i] < healths[j]:
                    healths[i] = 0
                    healths[j] -= 1
                    stack.append(j)
                else:
                    healths[i] = 0
                    healths[j] = 0
                    
    result = []
    for h in healths:
        if h:
            result.append(h)
            
    return result

'''
Time Complexity: O(N log N)
Let N be the number of robots (length of positions, healths, and directions arrays).
- Building the hashMap takes O(N) time, as we iterate through all positions once.
- Sorting the positions array takes O(N log N) time.
- The main loop iterates through the sorted positions, which is O(N) iterations.
- Inside the loop, for each robot moving left ('L'), we may pop elements from the stack. Each robot can be pushed and popped from the stack at most once across all iterations, so the total time for all stack operations is O(N).
- Building the result array takes O(N) time.
- Overall, the time complexity is dominated by the sorting step, resulting in O(N log N).

Space Complexity: O(N)
- The hashMap stores N position-to-index mappings, requiring O(N) space.
- The stack can store up to N robot indices in the worst case (e.g., when all robots are moving right), requiring O(N) space.
- The result array can store up to N health values, requiring O(N) space.
- The sorted positions array takes O(N) space.
- Therefore, the overall space complexity is O(N).
'''

# Test Cases
positions1 = [5,4,3,2,1], healths1 = [2,17,9,15,10], directions1 = "RRRRR"
print(robotCollisions(positions1, healths1, directions1)) # Output: [2,17,9,15,10]

positions2 = [3,5,2,6], healths2 = [10,10,15,12], directions2 = "RLRL"
print(robotCollisions(positions2, healths2, directions2)) # Output: [14]

positions3 = [1,2,5,6], healths3 = [10,10,11,11], directions3 = "RLRL"
print(robotCollisions(positions3, healths3, directions3)) # Output: []

positions4 = [1,40], healths4 = [10,11], directions4 = "RL"
print(robotCollisions(positions4, healths4, directions4)) # Output: [10,11]

positions5 = [3,47], healths5 = [46,26], directions5 = "LR"
print(robotCollisions(positions5, healths5, directions5)) # Output: [46,26]

positions6 = [1,2,3,4,5], healths6 = [1,2,3,4,5], directions6 = "LLLLR"
print(robotCollisions(positions6, healths6, directions6)) # Output: [1,2,3]

positions7 = [10,20,30], healths7 = [5,5,5], directions7 = "RRL"
print(robotCollisions(positions7, healths7, directions7)) # Output: [5]

positions8 = [1,2,3,4,5,6], healths8 = [10,5,20,15,30,25], directions8 = "RRRLLL"
print(robotCollisions(positions8, healths8, directions8)) # Output: [10,29]

positions9 = [15,10,5,20], healths9 = [8,12,16,4], directions9 = "LRRR"
print(robotCollisions(positions9, healths9, directions9)) # Output: [8,11,15,4]

positions10 = [7,3,9,1], healths10 = [20,15,25,10], directions10 = "RRLL"
print(robotCollisions(positions10, healths10, directions10)) # Output: [19,24]