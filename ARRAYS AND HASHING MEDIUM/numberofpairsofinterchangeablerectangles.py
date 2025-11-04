# NUMBER OF PAIRS OF INTERCHANGEABLE RECTANGLES

'''
You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.
Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio.
More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).
Return the number of pairs of interchangeable rectangles in rectangles.
'''

def interchangeableRectangles(rectangles):
    hashMap = {}
    
    for width, height in rectangles:
        hashMap[width / height] = hashMap.get(width / height, 0) + 1
        
    result = 0
    for value in hashMap.values():
        if value > 1:
            result += value * (value - 1) // 2
            
    return result

'''
Time Complexity: O(n)
- Let n be the number of rectangles in the input array `rectangles`.
- The algorithm iterates through the rectangles once to build the `hashMap`, which takes O(n) time.
- Iterating through the values of the `hashMap` and calculating the result also takes O(n) in the worst case when all rectangles have unique ratios.
- Therefore, the overall time complexity is O(n).

Space Complexity: O(n)
- The `hashMap` uses space proportional to the number of unique width-to-height ratios in the input.
- In the worst case, each rectangle could have a unique ratio, leading to a space complexity of O(n).
- The other variables use constant space O(1).
- Therefore, the overall space complexity is O(n).
'''

# Test Cases
rectangles1 = [[4, 8], [3, 6], [10, 20], [15, 30]]
print(interchangeableRectangles(rectangles1)) # Output: 4

rectangles2 = [[1, 1], [2, 2], [3, 3]]
print(interchangeableRectangles(rectangles2)) # Output: 3

rectangles3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(interchangeableRectangles(rectangles3)) # Output: 0

rectangles4 = [[1, 1], [1, 1], [1, 1]]
print(interchangeableRectangles(rectangles4)) # Output: 3

rectangles5 = [[1, 2], [2, 4], [4, 8], [8, 16]]
print(interchangeableRectangles(rectangles5)) # Output: 6

rectangles6 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
print(interchangeableRectangles(rectangles6)) # Output: 10

rectangles7 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
print(interchangeableRectangles(rectangles7)) # Output: 0

rectangles8 = [[1, 1], [1, 2], [2, 1], [2, 2]]
print(interchangeableRectangles(rectangles8)) # Output: 2

rectangles9 = [[1, 1], [1, 1], [1, 1], [1, 1]]
print(interchangeableRectangles(rectangles9)) # Output: 6

rectangles10 = [[1, 2], [2, 4], [4, 8], [8, 16], [16, 32]]
print(interchangeableRectangles(rectangles10)) # Output: 10