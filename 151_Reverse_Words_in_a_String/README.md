# LeetCode Problem: Reverse Words in a String

## Problem Statement

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space. Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Example 1:**
```
Input: "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**
```
Input: "  hello world  "
Output: "world hello"
Explanation: There are multiple spaces both at the beginning and the end of the input string. Only one space should separate the words in the output.
```

## Solution Explanation

The provided solution is implemented as a Python class named `Solution` with a method `reverseWords`. Here's a step-by-step explanation of the solution:

1. `original_list`: The input string `s` is first split into a list of words using the `split(" ")` method. This splits the string wherever there's a space character, creating a list of words.

2. `filtered_list`: The `original_list` may contain empty strings if there are multiple spaces between words or leading/trailing spaces in the input string. To address this, a list comprehension is used to create `filtered_list`, which contains only non-empty words.

3. Two pointers `i` and `j` are initialized. `i` starts at the beginning of `filtered_list`, and `j` starts at the end.

4. The while loop runs as long as `i` is less than `j`. Inside the loop, the words at positions `i` and `j` are swapped. This effectively reverses the order of words in `filtered_list`.

5. Finally, the `filtered_list` is joined into a single string using the `join` method with a space as the separator, and the result is returned.

### Example

Let's illustrate the solution with an example:

Input: `"the sky is blue"`

1. `original_list`: `["the", "sky", "is", "blue"]`
2. `filtered_list`: `["the", "sky", "is", "blue"]` (no empty strings)
3. `i` starts at 0, and `j` starts at 3.
4. The while loop swaps the words at `i` and `j`, so the list becomes `["blue", "sky", "is", "the"]`.
5. The list is joined into a single string with spaces as separators: `"blue is sky the"`

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        original_list = s.split(" ")
        filtered_list = [item for item in original_list if item != '']
        i, j = 0, len(filtered_list) - 1
        while i < j:
            filtered_list[i], filtered_list[j] = filtered_list[j], filtered_list[i]
            i += 1
            j -= 1
        return " ".join(filtered_list)
```

This solution effectively reverses the order of words while handling leading/trailing spaces and multiple spaces between words as specified in the problem statement.