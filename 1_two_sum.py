class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in num_dict:
                num_dict[nums[i]] = i
            else:
                return [i,num_dict[target-nums[i]]]