# CAR FLEET

'''
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
A car fleet is a single car or a group of cars driving next to each other. 
The speed of the car fleet is the minimum speed of any car in the fleet.
If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
Return the number of car fleets that will arrive at the destination.
'''

def fleetCars(target, position, speed):
    carData = []
    
    for i in range(len(position)):
        carData.append([position[i], speed[i]])
        
    stack = []
    carData.sort(reverse = True)
    
    for p, s in carData:
        timetoTarget = (target - p) / s
        stack.append(timetoTarget)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
            
    return len(stack)

'''
Time Complexity: O(n log n)
- The algorithm first combines the `position` and `speed` arrays into a single `carData` list of pairs. This takes O(n) time, where `n` is the number of cars.
- The most time-consuming step is sorting the `carData` list based on the car positions. The standard sorting algorithm used in Python (Timsort) has a time complexity of O(n log n).
- After sorting, the algorithm iterates through the `n` cars once. Inside the loop, all operations (calculating time, appending to the stack, checking the condition, and popping) are O(1). This loop takes O(n) time.
- The overall time complexity is dominated by the sorting step, making it O(n log n).

Space Complexity: O(n)
- The `carData` list is created to store the position and speed for each of the `n` cars, which requires O(n) space.
- The `stack` is used to store the arrival times of the car fleets. In the worst-case scenario (where no cars form a fleet), the stack could grow to a size of `n`.
- Therefore, the auxiliary space required is proportional to the number of cars, resulting in a space complexity of O(n).
'''

# Test Cases
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(fleetCars(position, speed)) # Output: 3

target = 10
position = [3]
speed = [3]
print(fleetCars(position, speed)) # Output: 1

target = 100
position = [0,2,4]
speed = [4,2,1]
print(fleetCars(position, speed)) # Output: 1

target = 10
position = [6,8]
speed = [3,2]
print(fleetCars(position, speed)) # Output: 2

target = 10
position = [0,4,2]
speed = [2,1,3]
print(fleetCars(position, speed)) # Output: 1

target = 100
position = [0, 50, 90]
speed = [10, 5, 1]
print(fleetCars(position, speed)) # Output: 1

target = 20
position = [0, 5, 10, 15]
speed = [1, 1, 1, 1]
print(fleetCars(position, speed)) # Output: 4

target = 10
position = []
speed = []
print(fleetCars(position, speed)) # Output: 0

target = 100
position = [0, 10, 20, 30, 40]
speed = [10, 1, 10, 1, 10]
print(fleetCars(position, speed)) # Output: 3

target = 100
position = [98, 99]
speed = [2, 1]
print(fleetCars(position, speed)) # Output: 1