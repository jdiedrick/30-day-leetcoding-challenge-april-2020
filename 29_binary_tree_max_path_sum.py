# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path_sum = -float('inf')

        def pathSum(node):
            if not node:
                return 0
            
            left = max(0, pathSum(node.left))
            right = max(0, pathSum(node.right))
            self.max_path_sum = max(self.max_path_sum, left + right + node.val)
            return max(left, right) + node.val
        
        pathSum(root)
        return self.max_path_sum
        
