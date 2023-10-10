class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        max_count = 0
        for i in range(len(s)):
            if s[i] in vowel:
                count += 1
            if i >= k - 1:
                max_count = max(max_count, count)
                if s[i - (k - 1)] in vowel:
                    count -= 1
        return max_count