class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        current_l = 0
        for i in range(len(nums)):
            current_r = total - nums[i] - current_l
            if current_l == current_r:
                return i
            current_l += nums[i]
        return -1 