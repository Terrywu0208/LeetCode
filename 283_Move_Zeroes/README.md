# LeetCode Readme: Move Zeroes

## Problem Description
Given an integer array `nums`, you are tasked with moving all the zeroes to the end of the array while preserving the relative order of the non-zero elements. It's important to perform this operation in-place, meaning you should modify the original `nums` array without creating a new copy.

## Example
**Input:**
```python
nums = [0, 1, 0, 3, 12]
```

**Output:**
```python
[1, 3, 12, 0, 0]
```

**Explanation:** In this example, all non-zero elements are moved to the beginning, and all zeroes are moved to the end while preserving their relative order.

## Solution Explanation

To solve this problem efficiently, we can use a two-pointer approach. Here's a step-by-step explanation of the solution:

1. Initialize two pointers, `i` and `j`, both initially set to 0.
   - `i` will represent the position where the next non-zero element should be placed.
   - `j` will be used to traverse the array.

2. Iterate through the array using the `j` pointer.
   - If `nums[j]` is not equal to 0 (i.e., a non-zero element is encountered):
     - Swap `nums[i]` and `nums[j]`. This moves the non-zero element to the correct position at `i`.
     - Increment `i` to prepare for the next non-zero element.

3. Continue this process until you have traversed the entire array.

4. After the loop, all non-zero elements will have been moved to the beginning of the array, and all zeroes will be at the end, preserving their relative order.

Here's the Python code that implements this approach:

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
```

