# LeetCode Problem: Find the Difference of Two Arrays

## Problem Explanation

You are given two integer arrays, `nums1` and `nums2`. Your task is to find the difference between these two arrays and return the result as a list of two lists:
1. `answer[0]` should contain all distinct integers in `nums1` that are not present in `nums2`.
2. `answer[1]` should contain all distinct integers in `nums2` that are not present in `nums1`.

The order of the integers in the lists does not matter.

**Example 1:**
```
Input: `nums1 = [1,2,3], nums2 = [2,4,6]

Output: `[[1,3],[4,6]]`

```

Explanation:
- For `nums1`, `nums1[1] = 2` is present at index 0 of `nums2`, whereas `nums1[0] = 1` and `nums1[2] = 3` are not present in `nums2`. Therefore, `answer[0] = [1,3]`.
- For `nums2`, `nums2[0] = 2` is present at index 1 of `nums1`, whereas `nums2[1] = 4` and `nums2[2] = 6` are not present in `nums1`. Therefore, `answer[1] = [4,6]`.

**Example 2:**
```
Input: `nums1 = [1,2,3,3], nums2 = [1,1,2,2]

Output: `[[3],[]]`
```

Explanation:
- For `nums1`, `nums1[2]` and `nums1[3]` are not present in `nums2`. Since `nums1[2] == nums1[3]`, their value is only included once, and `answer[0] = [3]`.
- Every integer in `nums2` is present in `nums1`. Therefore, `answer[1] = []`.

## Solution

The provided solution uses Python's set data structure to efficiently find the difference between the two arrays. Here's a detailed explanation of the code:

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)  
        s2 = set(nums2)  

        out = [[], []]  

        for i in s1:
            if i not in s2: 
                out[0].append(i)
        for i in s2:
            if i not in s1: 
                out[1].append(i)
        
        return out
```

- Create two sets, `s1` and `s2`, from `nums1` and `nums2`, respectively. Sets automatically eliminate duplicate values and store only distinct values.

- Initialize a list `out` containing two empty lists. `out[0]` will store the difference from `nums1` to `nums2`, and `out[1]` will store the difference from `nums2` to `nums1`.

- Iterate through the elements in `s1`. If an element is in `s1` but not in `s2`, it means it's a difference between `nums1` and `nums2`, so it's added to `out[0]`.

- Similarly, iterate through the elements in `s2`. If an element is in `s2` but not in `s1`, it's a difference between `nums2` and `nums1`, so it's added to `out[1]`.

- Finally, return `out` containing the differences. The order of the elements in the output lists is not guaranteed, as sets don't guarantee order.