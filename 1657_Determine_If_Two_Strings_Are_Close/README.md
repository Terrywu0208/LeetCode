# LeetCode Problem: Determine if Two Strings Are Close

## Problem Explanation

Two strings are considered "close" if you can transform one into the other using the following operations:

1. **Operation 1:** Swap any two existing characters.
   - For example, "abcde" can be transformed into "aecdb" by swapping 'b' and 'e'.

2. **Operation 2:** Transform every occurrence of one existing character into another existing character, and do the same with the other character.
   - For example, "aacabb" can be transformed into "bbcbaa" by transforming all 'a's into 'b's and all 'b's into 'a's.

You can use these operations on either string as many times as necessary. Given two strings, `word1` and `word2`, the task is to determine if they can be considered "close." If they can be transformed into each other using these operations, the function should return `true`; otherwise, it should return `false`.


**Example 1:**

```
Input: `word1 = "abc", word2 = "bca"`
Output: `true`
```
- Explanation: You can attain `word2` from `word1` in 2 operations.
  - Apply Operation 1: "abc" -> "acb"
  - Apply Operation 1: "acb" -> "bca"

**Example 2:**

```
Input: `word1 = "a", word2 = "aa"`
Output: `false`
```
- Explanation: It is impossible to attain `word2` from `word1, or vice versa, in any number of operations.

**Example 3:**

``` 
Input: `word1 = "cabbba", word2 = "abbccc"`
Output: `true`
```
- Explanation: You can attain `word2` from `word1` in 3 operations.
  - Apply Operation 1: "cabbba" -> "caabbb"
  - Apply Operation 2: "caabbb" -> "baaccc"
  - Apply Operation 2: "baaccc" -> "abbccc"

## Solution

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(list(Counter(word1).values())) == sorted(list(Counter(word2).values())) and set(word1) == set(word2)
```

To solve this problem, you can use the following approach:

1. Count the frequency of characters in both `word1` and `word2` and create lists of these frequencies.

2. Sort both frequency lists.

3. Check if the sorted frequency lists are equal (i.e., if you can transform one set of character frequencies into the other). This checks the feasibility of Operation 2.

4. Check if the sets of characters in `word1` and `word2` are the same. If they are not, return `false` since it's impossible to perform Operation 1 (swapping characters) to transform one string into the other.

5. If both conditions are met, return `true`, indicating that the two strings are "close."
