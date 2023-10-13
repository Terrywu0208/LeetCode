# LeetCode Readme: Is Subsequence

## Problem Description
Given two strings `s` and `t`, return true if `s` is a subsequence of `t`, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

## Example
**Input:**
```python
s = "abc"
t = "ahbgdc"
```

**Output:**
```python
True
```

**Explanation:** In this example, you can obtain `s` by deleting characters from `t`. Removing 'h', 'b', 'g', and 'd' from `t` leaves you with 'abc', which is `s`.

**Input:**
```python
s = "axc"
t = "ahbgdc"
```

**Output:**
```python
False
```

**Explanation:** In this case, you cannot obtain `s` by deleting characters from `t` without changing the relative order of the remaining characters. Hence, the result is `False`.

## Solution Explanation

To solve this problem, we can use a simple algorithm:

1. Initialize two pointers, `s_i` and `t_i`, both initially set to 0.
   - `s_i` will be used to traverse string `s`.
   - `t_i` will be used to traverse string `t`.

2. Initialize an empty list, `tmp`, to store the characters of `s` that are found in `t`.

3. Use a while loop to iterate through both strings, comparing characters at the current positions of `s_i` and `t_i`.

4. If `s[s_i]` is equal to `t[t_i]`, it means we've found a matching character. Append `s[s_i]` to the `tmp` list, and increment both `s_i` and `t_i`.

5. If `s[s_i]` is not equal to `t[t_i]`, increment only `t_i` to continue searching for the next character in `t`.

6. After the loop, check if the joined characters in `tmp` form the string `s`. If they do, return `True`. Otherwise, return `False`.

Here's the Python code that implements this approach:

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        t_i = 0
        tmp = []
        while t_i < len(t) and s_i < len(s):
            if s[s_i] == t[t_i]:
                tmp.append(s[s_i])
                s_i += 1
            t_i += 1
        return "".join(tmp) == s
```

