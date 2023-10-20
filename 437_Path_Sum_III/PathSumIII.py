# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, target, prefix_sum, prefix_sums):
            if node is None:
                return 0

            prefix_sum += node.val
            count = prefix_sums.get(prefix_sum - target, 0)

            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

            count += dfs(node.left, target, prefix_sum, prefix_sums) + dfs(node.right, target, prefix_sum, prefix_sums)

            prefix_sums[prefix_sum] -= 1

            return count

        prefix_sums = {0: 1}  # Initialize with a prefix sum of 0
        return dfs(root, targetSum, 0, prefix_sums)
