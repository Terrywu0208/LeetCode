 # LeetCode Problem: Reverse Vowels of a String

## Problem Statement
Given a string `s`, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

## Problem Explanation
You are given a string `s` containing letters. Your task is to reverse only the vowels in the string while keeping the consonants and other characters in their original positions. The vowels to consider are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lowercase and uppercase.

## Example

**Input:**
```python
s = "hello"
```

**Output:**
```python
"holle"
```

**Explanation:** The vowels are 'e' and 'o'. We reverse them to get "holle".

**Input:**
```python
s = "LeetCode"
```

**Output:**
```python
"Loetceed"
```

**Explanation:** The vowels are 'e', 'e', and 'o'. We reverse them to get "Loetceed".

## Solution

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        i, j = 0, len(s_list) - 1
        while i < j:
            while i < j and s_list[i] not in vowels:
                i += 1
            while i < j and s_list[j] not in vowels:
                j -= 1
            if i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
        return ''.join(s_list)
```

## Solution Explanation

1. To solve this problem, we create a set `vowels` that contains all the lowercase and uppercase vowels: {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}. This set will help us quickly check if a character is a vowel.

2. We convert the input string `s` into a list of characters `s_list` to make it mutable. This allows us to modify the string in place, as strings are immutable in Python.

3. We initialize two pointers, `i` and `j`, to 0 and the length of `s_list` minus 1, respectively. These pointers will help us traverse the string from both ends.

4. We use a while loop to iterate as long as `i` is less than `j`. This loop will continue until we have checked all possible pairs of characters to reverse.

5. Inside the loop, we have two nested while loops:
   - The first while loop increments `i` until we find a character that is a vowel (i.e., in `vowels`). We also check that `i` is less than `j` to avoid going beyond the `j` pointer.
   - The second while loop decrements `j` until we find a character that is a vowel (i.e., in `vowels`). We also check that `i` is less than `j` to avoid going beyond the `i` pointer.

6. If `i` is still less than `j` after both while loops, it means we have found vowels at positions `i` and `j` that need to be reversed. We swap these characters using tuple unpacking: `s_list[i], s_list[j] = s_list[j], s_list[i]`. This effectively reverses the vowels.

7. After swapping the vowels, we increment `i` and decrement `j` to continue checking the next pair of characters.

8. Once the while loop finishes, all the vowels in the string will be reversed.

9. Finally, we convert the modified `s_list` back to a string using `''.join(s_list)` and return the result.

This solution works by efficiently reversing the vowels in the string while keeping the consonants and other characters in their original positions, as required by the problem statement.