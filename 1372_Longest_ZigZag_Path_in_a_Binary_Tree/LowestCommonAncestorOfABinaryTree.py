# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root.right, False, 0), self.helper(root.left, True, 0))
    def helper(self, root, ifLeft, depth):
        if not root:
            return depth
        if ifLeft:
            depth = max(depth, self.helper(root.right, False, depth+1), self.helper(root.left, True, 0))
        else:
            depth = max(depth, self.helper(root.left, True, depth+1), self.helper(root.right, False, 0))

        return depth
