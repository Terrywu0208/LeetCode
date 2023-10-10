class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, max_count, zero_count = 0, 0, 0
        for r in range(len(nums)):
            if nums[r]==0:
                zero_count +=1
            while zero_count > k:
                if nums[l]==0:
                    zero_count -=1
                l+=1
            max_count = max(max_count, r-l+1)
        return max_count