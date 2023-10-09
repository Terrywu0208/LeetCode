# LeetCode Problem: Maximum Average Subarray I

This is a solution and explanation for the "Maximum Average Subarray I" problem on LeetCode. The problem statement is as follows:

## Problem Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`. Your task is to find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

## Example

**Input:**
```python
nums = [1, 12, -5, -6, 50, 3]
k = 4
```

**Output:**
```python
12.75
```

**Explanation:**
- The subarray `[12, -5, -6, 50]` has the maximum average value.
- Average = `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`.

## Solution Explanation

To solve this problem efficiently, you can use a sliding window approach. Here's an explanation of the provided solution:

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        current_sum = max_sum
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum / k
```

1. **Initialize Sums**: We start by initializing `max_sum` to 0. This variable will keep track of the maximum sum of a contiguous subarray of length `k`. We also iterate through the first `k` elements of `nums` to calculate the initial `max_sum`. This is done by summing the first `k` elements.

2. **Sliding Window**: We use a sliding window approach to efficiently find the maximum sum of a contiguous subarray of length `k`. We start from index `k` and iterate through the remaining elements of `nums`.

3. **Update Current Sum**: In each iteration, we update the `current_sum` by subtracting the first element that is no longer part of the current subarray (i.e., `nums[i - k]`) and adding the current element (i.e., `nums[i]`). This simulates moving the sliding window one element to the right.

4. **Update Maximum Sum**: We continuously update the `max_sum` by taking the maximum of the current `max_sum` and the `current_sum`. This ensures that we keep track of the maximum sum seen so far.

5. **Return Maximum Average**: Finally, we return `max_sum / k`, which is the maximum average value of a contiguous subarray of length `k`.

### Example

Let's take the example input `nums = [1, 12, -5, -6, 50, 3]` and `k = 4`:

1. Initialize `max_sum` to 0 and calculate the initial `max_sum` by summing the first `k` elements: `max_sum = 1 + 12 + (-5) + (-6) = 2`.

2. Start the sliding window from index `k = 4` (element `50`). We calculate the `current_sum` by subtracting the first element `1` (which is no longer in the window) and adding the current element `50`: `current_sum = 2 - 1 + 50 = 51`.

3. Update `max_sum` to 51 since it's greater than the previous `max_sum` of 2.

4. Continue this process for the remaining elements of `nums`.

5. After processing all elements, `max_sum` is 51, and we return `max_sum / k = 51 / 4 = 12.75`.

This solution efficiently finds the maximum average value of a contiguous subarray of length `k` by sliding a window of size `k` through the array and updating the maximum sum as needed.