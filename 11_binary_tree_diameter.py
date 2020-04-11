'''
With pairing help from Justin Jaffray 
'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        diameter, depth = Solution.findDiameterAndDepth(root)
        return diameter
    
    def findDiameterAndDepth(node):
        if node is None:
            return 0, 0
        
        left_diameter, left_depth = Solution.findDiameterAndDepth(node.left)
        right_diameter, right_depth = Solution.findDiameterAndDepth(node.right)
        
        root_diameter  = left_depth + right_depth
        
        left_depth += 1
        right_depth += 1
        
        depth = max(left_depth, right_depth)
        
        diameter = max(root_diameter, left_diameter, right_diameter)
        
        return diameter, depth
