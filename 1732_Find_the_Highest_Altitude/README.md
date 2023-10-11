# LeetCode Problem: Find the Highest Altitude

## Problem Explanation

Imagine a biker embarking on a road trip. This road trip comprises n+1 points at varying altitudes. The journey begins at point 0, where the altitude is 0. You are given an integer array `gain` of length n, where `gain[i]` represents the net gain in altitude between points i and i+1 for all 0 <= i < n. Your task is to determine the highest altitude reached during the journey.

**Example 1:**

Input: `gain = [-5,1,5,0,-7]`

Output: 1

Explanation: The altitudes experienced during the journey are as follows: [0, -5, -4, 1, 1, -6]. The highest altitude reached is 1.

**Example 2:**

Input: `gain = [-4,-3,-2,-1,4,3,2]`

Output: 0

Explanation: The altitudes experienced are: [0, -4, -7, -9, -10, -6, -3, -1]. The highest altitude reached is 0.

## Solution

The provided solution offers an effective way to calculate the highest altitude reached during the biker's journey:

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current = 0
        for r in range(len(gain)):
            current += gain[r]
            max_altitude = max(max_altitude, current)
        return max_altitude
```

Here's how the solution works:

1. Initialize two variables, `max_altitude` and `current`, to 0. `max_altitude` stores the highest altitude encountered, and `current` keeps track of the current altitude during the journey.

2. Iterate through the `gain` array using a pointer `r` that moves from left to right.

3. Update the `current` altitude by adding the value at `gain[r]`.

4. Continuously update the `max_altitude` to store the maximum altitude encountered during the journey. It's done using the `max()` function to compare the current altitude with the `max_altitude` variable.

5. Repeat steps 3-4 for the entire `gain` array, ensuring that `max_altitude` holds the highest altitude at the end of the journey.

6. Return the `max_altitude` as the answer.

This solution maintains a running sum of altitudes in the `current` variable, and it updates the `max_altitude` whenever a new highest altitude is encountered. At the end of the journey, `max_altitude` contains the highest altitude reached.

The time complexity of this solution is O(n), where n is the length of the input `gain`, as it iterates through the array once.