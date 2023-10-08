# LeetCode Problem: String Compression

## Problem Statement
Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
- If the group's length is 1, append the character to `s`.
- Otherwise, append the character followed by the group's length.

The compressed string `s` should not be returned separately but instead be stored in the input character array `chars`. Note that group lengths that are 10 or longer will be split into multiple characters in `chars`.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

## Example

Input:
```
chars = ["a","a","b","b","c","c","c"]
```

Output:
```
chars = ["a","2","b","2","c","3"]
```

Explanation:
The original array `chars` is modified in place, and the resulting compressed array has a length of 6.

## Solution Explanation

To solve this problem, we can use two pointers `i` and `j` to iterate through the array `chars`. We'll also use a temporary list `tmp` to store the compressed characters and their counts. Here's a step-by-step explanation of the solution:

1. Initialize `i` and `j` to 0. Also, create an empty list `tmp` to store the compressed characters.

2. While `j` is less than the length of `chars`, do the following:

   - Check if `chars[i]` is equal to `chars[j]`. If they are equal, increment `j` to move to the next character in the group.
   - If `chars[i]` is not equal to `chars[j]`, it means we have found the end of a group. Append `chars[i]` to `tmp`.

   - Check if the length of the group (which is `j - i`) is greater than 1. If it is, we need to append the count to `tmp`. To do this, convert the count to a string and add each digit as a separate character to `tmp`.

   - Update `i` to `j` to move to the next group of characters.

3. After the loop, we might have one more group left to process, so we append `chars[i]` and its count (if applicable) to `tmp`.

4. Finally, we update the `chars` array with the compressed content from `tmp`. We slice the `chars` array to the length of `tmp` and assign the values of `tmp` to it.

5. Return the length of `tmp`, which is also the length of the modified `chars` array.

The solution works by identifying consecutive groups of characters, compressing them, and updating the `chars` array in place.

Here's the implementation of the solution in Python:

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        tmp = []
        while j < len(chars):
            if chars[i] == chars[j]:
                j += 1
            else:
                tmp.append(chars[i])
                if j - i > 1:
                    tmp.extend(list(str(j - i)))
                i = j
        tmp.append(chars[i])
        if j - i > 1:
            tmp.extend(list(str(j - i)))
        chars[:len(tmp)] = tmp
        return len(tmp)
```

This solution efficiently compresses the input array `chars` and returns the new length of the compressed array.