class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        count = 0
        for i in nums:
            if d.get(k-i, 0):
                count+=1
                d[k-i] -=1
            else:
                d[i] = d.get(i, 0) + 1
        return count
    