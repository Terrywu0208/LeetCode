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