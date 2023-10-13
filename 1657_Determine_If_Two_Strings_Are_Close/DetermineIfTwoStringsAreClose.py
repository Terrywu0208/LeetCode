class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(list(Counter(word1).values())) == sorted(list(Counter(word2).values())) and set(word1) == set(word2)