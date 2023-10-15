# LeetCode Problem: Asteroid Collision

## Problem Explanation

You are given an array `asteroids` of integers, each representing an asteroid in a row. These asteroids are characterized by their size (represented as the absolute value of the integer) and their direction (positive for right, negative for left). All asteroids move at the same speed.

Your task is to determine the state of the asteroids after they collide. When two asteroids collide, the smaller one will explode. If two asteroids are of the same size, they will both explode. However, two asteroids moving in the same direction will never collide.

### Example 1:
```
Input: asteroids = [5, 10, -5]
Output: [5, 10]
```
Explanation: The asteroid with size 10 and the one with size -5 collide, resulting in a single asteroid with a size of 10. The asteroid with size 5 and the one with size 10 never collide.

### Example 2:
```
Input: asteroids = [8, -8]
Output: []
```
Explanation: The asteroid with size 8 and the one with size -8 collide, and both explode, leaving no remaining asteroids.

### Example 3:
```
Input: asteroids = [10, 2, -5]
Output: [10]
```
Explanation: The asteroid with size 2 and the one with size -5 collide, resulting in an asteroid with a size of -5. Then, the asteroid with size 10 and the one with size -5 collide, resulting in an asteroid with a size of 10.

## Solution

To solve this problem, we can use a stack to keep track of the asteroids as they move from left to right. We iterate through the `asteroids` array, and for each asteroid, we compare it with the asteroid at the top of the stack to determine if they will collide.

Here's the Python solution to this problem:

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid) 

        return stack 
```
