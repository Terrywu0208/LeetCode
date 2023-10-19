class Solution:
    def DFS(self, node, result):
        if node is None:
            return

        if node.left is None and node.right is None:
            result.append(node.val)
        else:
            self.DFS(node.left, result)  
            self.DFS(node.right, result)  

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_values1, leaf_values2 = [], []
        self.DFS(root1, leaf_values1)
        self.DFS(root2, leaf_values2)

        return leaf_values1 == leaf_values2
