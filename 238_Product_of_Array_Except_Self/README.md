# LeetCode Problem: Product of Array Except Self

## Problem Description

You are given an integer array `nums`, and your task is to return an array `answer` where each `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must solve this problem in O(n) time complexity and without using the division operation.

**Input:**
- An integer array `nums` (2 <= nums.length <= 10^5) containing integers.

**Output:**
- An array of the same length as `nums`, where each element at index `i` is the product of all elements in `nums` except `nums[i]`.

## Approach

To solve this problem efficiently in O(n) time complexity without using division, we can use two passes through the input array `nums`. The idea is to maintain two auxiliary arrays to keep track of the product of elements to the left and right of each element in `nums`.

1. **Initialization**: First, initialize a result array `result` of the same length as `nums` and set all its elements to 1. Initialize two variables, `pre` and `pos`, to 1. This `result` array will store the final product values for each element.

2. **Left Pass**: These variables will keep track of the product of elements to the left and right of the current element, respectively.

    - In the first pass (from left to right), iterate through `nums`. At each index `i`, update `result[i]` with the product of all elements to the left of `nums[i]` (which is stored in `pre`). Then, update `pre` by multiplying it with `nums[i]`. This pass will ensure that `result[i]` contains the product of all elements to the left of `nums[i]`.

3. **Right Pass**: In the second pass (from right to left), iterate through `nums` in reverse order. At each index `i`, multiply `result[i]` with the product of all elements to the right of `nums[i]` (which is stored in `pos`). Update `pos` by multiplying it with `nums[i]`. This pass will ensure that `result[i]` now contains the product of all elements to the left and right of `nums[i]`.

4. **Final Result**: Finally, return the `result` array, which contains the desired product values.

## Example

Let's illustrate the approach with an example:

**Input:** `nums = [1, 2, 3, 4]`

1. **Initialization**:
   - Initialize `result = [1, 1, 1, 1]`, `pre = 1`, `pos = 1`

2. **Left Pass (from left to right)**:
   - At index 0: `result[0] = pre = 1`, `pre *= nums[0] = 1`
   - At index 1: `result[1] = pre = 1`, `pre *= nums[1] = 2`
   - At index 2: `result[2] = pre = 2`, `pre *= nums[2] = 6`
   - At index 3: `result[3] = pre = 6`, `pre *= nums[3] = 24`

   Now, `result = [1, 1, 2, 6]`, and `pre = 24`

3. **Right Pass (from right to left)**:
   - At index 3: `result[3] *= pos = 1`, `pos *= nums[3] = 4`
   - At index 2: `result[2] *= pos = 4`, `pos *= nums[2] = 12`
   - At index 1: `result[1] *= pos = 48`, `pos *= nums[1] = 24`
   - At index 0: `result[0] *= pos = 144`, `pos *= nums[0] = 24`

   The final `result` array is `[24, 12, 8, 6]`.

4. **Return Result**: Return `[24, 12, 8, 6]` as the answer.

## Solution:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre = 1
        pos = 1
        
        # Left Pass: Compute products of elements to the left of each element
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        
        # Right Pass: Compute products of elements to the right of each element
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= pos
            pos *= nums[i]
        
        return result
```

This Python code implements the algorithm described above and solves the "Product of Array Except Self" problem in O(n) time complexity without using division.