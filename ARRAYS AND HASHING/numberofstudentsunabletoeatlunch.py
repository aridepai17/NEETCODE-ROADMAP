# NUMBER OF STUDENTS UNABLE TO EAT LUNCH

'''
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. 
All students stand in a queue. Each student either prefers square or circular sandwiches.
The number of sandwiches in the cafeteria is equal to the number of students. 
The sandwiches are placed in a stack. At each step:
If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). 
Return the number of students that are unable to eat.
'''

def constStudents(students, sandwiches):
    hashMap = {}
    result = len(students)
    
    for s in students:
        hashMap[s] = hashMap.get(s, 0) + 1
        
    for s in sandwiches:
        if hashMap.get(s, 0) > 0:
            hashMap[s] -= 1
            result -= 1
        else:
            break
        
    return result

'''
Time Complexity: O(N)
Let N be the number of students (which is also the number of sandwiches).
- The first loop iterates through all N students to count their preferences. This takes O(N) time.
- The second loop iterates through the sandwiches. In the worst case, it will iterate through all N sandwiches. This also takes O(N) time.
- The overall time complexity is O(N) + O(N) = O(N), as the operations inside the loops are constant time on average (for the hash map).

Space Complexity: O(1)
- We use a hash map to store the counts of student preferences.
- Since there are only two types of sandwiches (0 and 1), the hash map will have at most two keys.
- Therefore, the space required for the hash map is constant, regardless of the number of students.
- The space complexity is O(1).
'''

# Test Cases
students1 = [1,1,0,0], sandwiches1 = [0,1,0,1]
print(constStudents(students1, sandwiches1)) # Output: 0

students2 = [1,1,1,0,0,1], sandwiches2 = [1,0,0,0,1,1]
print(constStudents(students2, sandwiches2)) # Output: 3

students3 = [0,0,0], sandwiches3 = [1,1,1]
print(constStudents(students3, sandwiches3)) # Output: 3

students4 = [1,1,1], sandwiches4 = [1,1,1]
print(constStudents(students4, sandwiches4)) # Output: 0

students5 = [0], sandwiches5 = [0]
print(constStudents(students5, sandwiches5)) # Output: 0

students6 = [0], sandwiches6 = [1]
print(constStudents(students6, sandwiches6)) # Output: 1

students7 = [1,0,1,0], sandwiches7 = [1,1,1,1]
print(constStudents(students7, sandwiches7)) # Output: 2

students8 = [0,0,0,0], sandwiches8 = [0,1,0,0]
print(constStudents(students8, sandwiches8)) # Output: 3

students9 = [1,0,0,1,1], sandwiches9 = [0,1,0,1,1]
print(constStudents(students9, sandwiches9)) # Output: 0

students10 = [1,0,1,1], sandwiches10 = [1,1,0,0]
print(constStudents(students10, sandwiches10)) # Output: 1