# LeetCode Problem: Unique Number of Occurrences

## Problem Explanation

You are given an array of integers, `arr`. Your task is to determine if the number of occurrences of each value in the array is unique. In other words, you need to check if no two different values in the array have the same count of occurrences. If this condition is met, return `true`; otherwise, return `false`.


**Example 1:**

```Input: arr = [1,2,2,1,1,3]
Output: true```

Explanation: In this example, the value 1 appears 3 times, 2 appears 2 times, and 3 appears 1 time. No two values have the same number of occurrences, so the function returns `true`.

**Example 2:**

```Input: arr = [1,2]
Output: false```

Explanation: Here, the value 1 appears 1 time, and the value 2 appears 1 time as well. Since both values have the same number of occurrences (1), the function returns `false`.

**Example 3:**

```Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true```

Explanation: In this case, the value -3 appears 3 times, 0 appears 2 times, 1 appears 4 times, and 10 appears 1 time. No two values have the same number of occurrences, so the function returns `true`.

## Solution

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for i in arr:
            counts[i] = counts.get(i, 0) + 1
        return len(counts) == len(set(counts.values()))
```

This solution defines a class `Solution` with a method `uniqueOccurrences`. Here's how it works:

1. Initialize an empty dictionary `counts` to store the counts of each unique element in the input array `arr`.

2. Iterate through the elements of `arr` using a for loop.

3. For each element `i`, use `counts.get(i, 0)` to get the current count of that element. If the element is not in the dictionary, it defaults to 0. Then, increment the count by 1.

4. After counting all the elements in the array, you have a dictionary `counts` where the keys are unique elements from `arr`, and the values are their respective counts.

5. To check if the number of occurrences is unique, compare the length of the `counts` dictionary with the length of a set of its values. If they are equal, it means that no two different values have the same count of occurrences, and the function returns `True`. Otherwise, it returns `False`.
