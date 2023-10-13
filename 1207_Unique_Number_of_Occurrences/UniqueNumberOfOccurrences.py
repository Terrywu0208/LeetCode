class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for i in arr:
            counts[i] = counts.get(i, 0)+1
        return len(counts) == len(set(counts.values()))
