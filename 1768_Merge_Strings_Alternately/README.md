# Merge Strings Alternately

I recently tackled the LeetCode problem "Merge Strings Alternately" and came up with a Python solution to solve it. Let me explain the problem first in simple terms and then walk you through my solution.

## Problem Explanation

In this problem, we're given two strings, `word1` and `word2`, and our task is to merge them by taking characters from each string in an alternating fashion. We start with `word1`, add a character from it, then add a character from `word2`, and so on. If one of the strings is longer than the other, we append the remaining characters from the longer string to the end of our merged string.

Let me illustrate this with a couple of examples:

### Example 1:

Input:
- `word1 = "abc"`
- `word2 = "xyz"`

Output:
- `"axbycz"`

Explanation:
- We start with `word1[0]`, which is `"a"`, then `word2[0]`, which is `"x"`.
- Next, we take `word1[1]`, which is `"b"`, followed by `word2[1]`, which is `"y"`.
- Finally, we take `word1[2]`, which is `"c"`, and `word2` is exhausted, so we don't add any more characters from it.
- The merged string is `"axbycz"`.

### Example 2:

Input:
- `word1 = "abcd"`
- `word2 = "ef"`

Output:
- `"aebfcd"`

Explanation:
- We start with `word1[0]`, which is `"a"`, then `word2[0]`, which is `"e"`.
- Next, we take `word1[1]`, which is `"b"`, and `word2[1]`, which is `"f"`.
- Now, `word1` is longer, so we continue adding characters from `word1`: `"c"` and `"d"`.
- The merged string is `"aebfcd"`.

## My Solution

To solve this problem, I used Python and implemented a solution as follows:

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        tmp = []
        while i < len(word1) and j < len(word2):
            tmp.append(word1[i])
            tmp.append(word2[j])
            i += 1
            j += 1
        tmp.append(word1[i:])
        tmp.append(word2[j:])
        return "".join(tmp)
```

Here's how my solution works:

- created a class `Solution` with a method `mergeAlternately` that takes two input strings, `word1` and `word2`, and returns the merged string.

- used two pointers, `i` and `j`, to keep track of the current positions in `word1` and `word2`, respectively.

- created an empty list `tmp` to store the characters of the merged string.

- used a `while` loop to iterate through both `word1` and `word2` until I reached the end of either string.

- Inside the loop, appended characters from `word1` and `word2` to the `tmp` list in alternating order.

- After the loop, checked if there were any remaining characters in either `word1` or `word2` and appended them to the `tmp` list.

- Finally, used `"".join(tmp)` to concatenate all the characters in the `tmp` list and returned the merged string.

