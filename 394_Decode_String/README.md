# LeetCode Problem: Decode String

## Problem Explanation

Given an encoded string, you need to decode it following a specific pattern. The encoding rule is as follows: `k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly `k` times. You can assume that `k` is guaranteed to be a positive integer. There are no extra white spaces, square brackets are well-formed, and digits are only used for repeat numbers, `k`. For example, you will not encounter input like `3a` or `2[4]`. The length of the output will never exceed 105.

Here are some examples to help you understand the problem:

### Example 1:
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

### Example 2:
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

### Example 3:
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Solution

To solve this problem, we can use a stack data structure to keep track of characters in the encoded string. Here's a step-by-step explanation of the provided solution:

1. Initialize an empty stack to store characters.

2. Iterate through the input string `s` character by character.

3. If the current character is not ']', push it onto the stack. This is because we want to collect characters until we encounter a ']'.

4. If the current character is ']', it means we need to process the characters within the square brackets. So, we pop characters from the stack until we encounter a '[' and concatenate them to create the `encoded_string`.

5. After popping the '[', we need to extract the number `k` that represents how many times the `encoded_string` should be repeated. We continue popping characters from the stack until we find a non-digit character. Concatenate the digits in reverse order to get the correct value of `k`.

6. Multiply the `encoded_string` by `k` and push the result back onto the stack. This represents the decoded portion of the input string.

7. Continue this process for the entire input string.

8. Finally, join all the characters left in the stack to obtain the decoded string.

Here's the Python code for the solution:

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    tmp = stack.pop()
                    substr = tmp + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    tmp = stack.pop()
                    k = tmp + k
                stack.append(int(k) * substr)
        return "".join(stack)
```

