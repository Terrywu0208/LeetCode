# LeetCode Problem: Increasing Triplet Subsequence

## Problem Description

Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

### Example

Input: `nums = [1,2,3,4,5]`

Output: `true`

Explanation: There are many valid triplets that satisfy the condition, for example, `(1, 2, 3)`.

Input: `nums = [5,4,3,2,1]`

Output: `false`

Explanation: No triplet exists that satisfies the condition.

## Solution Explanation

We can solve this problem using a simple algorithm that keeps track of the two smallest numbers encountered so far (`first` and `second`). If we find a number greater than or equal to `second`, it means we've found a triplet that satisfies the condition, so we return `True`. Otherwise, we continue updating `first` and `second` as we iterate through the array.

Here's how the solution works step by step:

1. Initialize `first` and `second` to positive infinity (`float("inf")`) as placeholders for the two smallest numbers.

2. Iterate through the elements of the `nums` array.

3. For each element `n`, check if it is less than or equal to `first`. If it is, update `first` to `n`. This step ensures that `first` always contains the smallest number encountered so far.

4. If `n` is greater than `first` but less than or equal to `second`, update `second` to `n`. This step ensures that `second` always contains the second smallest number encountered so far.

5. If `n` is greater than both `first` and `second`, it means we've found a triplet `(first, second, n)` where `first < second < n`. In this case, return `True` as we've found a valid triplet.

6. If we complete the loop without finding a valid triplet, return `False`.

### Example

Let's walk through an example using the input `nums = [1, 3, 2, 4, 5]`:

1. Initialize `first` and `second` to `inf`: `first = inf`, `second = inf`.

2. Loop through the elements:
   - For `n = 1`, `n` is less than `first`, so update `first` to `1`.
   - For `n = 3`, `n` is greater than `first` but less than `second`, so update `second` to `3`.
   - For `n = 2`, `n` is greater than `first` but less than `second`, so update `second` to `2`.
   - For `n = 4`, `n` is greater than both `first` and `second`, so return `True`.

The algorithm returns `True` for this example because it finds the triplet `(1, 2, 4)` where `1 < 2 < 4`.

## Code

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
```

The provided code implements the solution we described. It initializes `first` and `second` to `inf`, iterates through the `nums` array, and updates `first` and `second` accordingly. If it finds a valid triplet, it returns `True`. If no valid triplet is found after the loop, it returns `False`.

This solution has a time complexity of O(n) where n is the length of the `nums` array, making it efficient for large inputs.