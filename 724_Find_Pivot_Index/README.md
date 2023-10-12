# LeetCode Problem: Find Pivot Index

## Problem Explanation

Given an array of integers `nums`, calculate the "pivot index" of this array. The pivot index is a position where the sum of all elements to the left of that index is equal to the sum of all elements to the right of that index. If the index is on the left edge of the array, the sum on the left is considered to be 0 since there are no elements to the left. The same rule applies to the right edge of the array. If no pivot index is found, return -1.

### Example 1

#### Input

```
nums = [1,7,3,6,5,6]
```

#### Output

```
3
```

#### Explanation

In this example, the pivot index is 3.

Left sum = `nums[0] + nums[1] + nums[2]` = `1 + 7 + 3` = 11

Right sum = `nums[4] + nums[5]` = `5 + 6` = 11

### Example 2

#### Input

```
nums = [1,2,3]
```

#### Output

```
-1
```

#### Explanation

In this example, no index satisfies the problem's conditions, so -1 is returned.

## Solution

Here's a Python solution for finding the pivot index:

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        current_l = 0
        for i in range(len(nums)):
            current_r = total - nums[i] - current_l
            if current_l == current_r:
                return i
            current_l += nums[i]
        return -1
```