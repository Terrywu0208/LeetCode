# LeetCode Readme: Greatest Common Divisor of Strings

## Problem Description
Given two strings `str1` and `str2`, you are tasked with finding the largest string `x` such that `x` divides both `str1` and `str2`. In other words, you need to determine if there exists a string `x` that can be concatenated multiple times to form both `str1` and `str2`. If such a string exists, return it; otherwise, return an empty string.

## Example
**Input:**
```python
str1 = "ABCABC"
str2 = "ABC"
```

**Output:**
```python
"ABC"
```

**Explanation:** In this example, the largest string that divides both `str1` and `str2` is "ABC".

**Input:**
```python
str1 = "LEET"
str2 = "CODE"
```

**Output:**
```python
""
```

**Explanation:** In this case, there is no common string that divides both `str1` and `str2`, so we return an empty string.

## Solution Explanation

To solve this problem, we can use a simple algorithm:

1. Calculate the lengths of both input strings, `len1` and `len2`.
2. Iterate from `min(len1, len2)` down to 1. This ensures that we start with the largest possible common divisor and work our way down to smaller divisors.
3. For each divisor `i`, check if both `len1` and `len2` are divisible by `i` (i.e., `len1 % i == 0` and `len2 % i == 0`).
4. If both conditions are met, check if `str1[:i] * (len1 // i)` is equal to `str1` and `str1[:i] * (len2 // i)` is equal to `str2`. This ensures that the common string `x` can be formed by concatenating `str1[:i]` the appropriate number of times.
5. If the conditions in step 4 are satisfied, return `str1[:i]` as the greatest common divisor. Otherwise, continue the loop.
6. If the loop completes without finding a common divisor, return an empty string.

## Example

Let's illustrate the solution with the first example from above:

**Input:**
```python
str1 = "ABCABC"
str2 = "ABC"
```

1. Calculate the lengths: `len1 = 6`, `len2 = 3`.
2. Start the loop from `min(6, 3) = 3` down to 1.
3. For `i = 3`, both `len1` and `len2` are divisible by 3 (`len1 % 3 == 0` and `len2 % 3 == 0`).
4. Check if `str1[:3] * (len1 // 3)` equals `str1` and `str1[:3] * (len2 // 3)` equals `str2`:
   - `str1[:3] * (6 // 3)` becomes "ABCABC," which equals `str1`.
   - `str1[:3] * (3 // 3)` becomes "ABC," which equals `str2`.
5. The conditions are satisfied, so we return `"ABC"` as the greatest common divisor.

The solution works similarly for other test cases and is a straightforward approach to find the greatest common divisor of strings.

## Code Explanation

The provided Python code implements the solution:

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                if str1[:i] * (len1 // i) == str1 and str1[:i] * (len2 // i) == str2:
                    return str1[:i]
        return ""
```

It calculates the lengths of the input strings, then iterates through possible divisors, checking if they meet the conditions described earlier. If a common divisor is found, it returns that string; otherwise, it returns an empty string.