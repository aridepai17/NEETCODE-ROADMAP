# ASTEROID COLLISION

'''
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteroid in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
'''

def asteroidCollision(asteroids):
    stack = []
    
    for a in asteroids:
        while stack and a < 0  and stack[-1] > 0:
            diff = a + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                a = 0
            else:
                stack.pop()
                a = 0
        if a:
            stack.append(a)
            
    return stack

'''
Time Complexity: O(n)
- The algorithm iterates through the input list `asteroids` of length `n` exactly once.
- Although there is a nested `while` loop, its total number of executions is bounded. Each asteroid is pushed onto the stack at most once.
- For each collision, at least one asteroid is destroyed and removed from consideration (either by popping from the stack or by not being pushed onto the stack).
- Since each asteroid can be involved in a collision at most once before being destroyed, the total number of operations within the `while` loop across the entire execution is proportional to `n`.
- Therefore, the amortized time complexity is O(n).

Space Complexity: O(n)
- The space complexity is determined by the `stack` used to store the asteroids that have survived collisions.
- In the worst-case scenario, no collisions occur (e.g., all asteroids are moving in the same direction, or all negative asteroids are before all positive ones).
- In this case, the stack can grow to a size of `n`, where `n` is the number of asteroids.
- Therefore, the auxiliary space required by the algorithm is O(n).
'''

# Test Cases
asteroids1 = [5,10,-5]
print(asteroidCollision(asteroids1)) # Output: [5, 10]

asteroids2 = [8,-8]
print(asteroidCollision(asteroids2)) # Output: []

asteroids3 = [10,2,-5]
print(asteroidCollision(asteroids3)) # Output: [10]

asteroids4 = [-2,-1,1,2]
print(asteroidCollision(asteroids4)) # Output: [-2, -1, 1, 2]

asteroids5 = [1,-2,-2,-2]
print(asteroidCollision(asteroids5)) # Output: [-2, -2, -2]

asteroids6 = [-2, -2, 1, -2]
print(asteroidCollision(asteroids6)) # Output: [-2, -2, -2]

asteroids7 = []
print(asteroidCollision(asteroids7)) # Output: []

asteroids8 = [10]
print(asteroidCollision(asteroids8)) # Output: [10]

asteroids9 = [-1, -2, -3]
print(asteroidCollision(asteroids9)) # Output: [-1, -2, -3]

asteroids10 = [1, 2, 3, -10]
print(asteroidCollision(asteroids10)) # Output: [-10]