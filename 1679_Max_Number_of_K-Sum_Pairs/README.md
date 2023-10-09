# LeetCode Problem: Max Number of K-Sum Pairs

This is a solution and explanation for the "Max Number of K-Sum Pairs" problem on LeetCode. The problem statement is as follows:

## Problem Description

You are given an integer array `nums` and an integer `k`. In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array. Your task is to return the maximum number of operations you can perform on the array.

## Example

**Input:**
```python
nums = [1, 2, 3, 4]
k = 5
```

**Output:**
```python
2
```

**Explanation:**
- In the first operation, you can pick `1` and `4` (1 + 4 = 5) and remove them from the array, resulting in `[2, 3]`.
- In the second operation, you can pick `2` and `3` (2 + 3 = 5) and remove them from the array, resulting in an empty array.
- You have performed a total of 2 operations.

## Solution Explanation

To solve this problem efficiently, you can use a Python solution that uses a dictionary to keep track of the numbers in the array. Here's an explanation of the provided solution:

```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        count = 0
        for i in nums:
            if d.get(k-i, 0):
                count+=1
                d[k-i] -=1
            else:
                d[i] = d.get(i, 0) + 1
        return count
    
```

1. **Initialize Dictionary and Count**: We start by initializing an empty dictionary `d` to store counts of numbers and a variable `count` to count the number of operations.

2. **Iterate Through Array**: We iterate through the `nums` array using a `for` loop. For each number `i` in `nums`, we check whether there is a complementary number in the dictionary that can form a pair with `i` to equal `k`.

3. **Check for Complementary Pair**: If `d.get(k - i, 0)` returns a value greater than 0 (meaning there is a complementary number in the dictionary), it implies that we can perform an operation. In this case:
   - Increment the `count` variable to keep track of the number of operations.
   - Decrease the count of the complementary number in the dictionary by 1 (`d[k - i] -= 1`), indicating that one occurrence of that number has been used.

4. **No Complementary Pair Found**: If no complementary number is found, we add the current number `i` to the dictionary or increment its count if it already exists (`d[i] = d.get(i, 0) + 1`).

5. **Return Count**: Finally, we return the total count of operations, which represents the maximum number of pairs that can be removed to achieve the sum of `k`.

### Example

Let's take the example input `nums = [1, 2, 3, 4]` and `k = 5`:

1. Initialize an empty dictionary `d` and `count` to 0.

2. Start iterating through the `nums` array:
   - For `i = 1`, check if there is a complementary number `k - i = 4` in the dictionary. None is found, so add `1` to the dictionary: `d = {1: 1}`.
   - For `i = 2`, check if there is a complementary number `k - i = 3` in the dictionary. None is found, so add `2` to the dictionary: `d = {1: 1, 2: 1}`.
   - For `i = 3`, check if there is a complementary number `k - i = 2` in the dictionary. None is found, so add `3` to the dictionary: `d = {1: 1, 2: 1, 3: 1}`.
   - For `i = 4`, check if there is a complementary number `k - i = 1` in the dictionary. A complementary number is found (`1`), so increment the `count` to 1 and decrease the count of `1` in the dictionary: `d = {1: 0, 2: 1, 3: 1}`.

3. Continue iterating, but no more complementary pairs are found.

4. Return the `count`, which is 1. This means you can perform a maximum of 1 operation to remove a pair of numbers whose sum equals `k`.
