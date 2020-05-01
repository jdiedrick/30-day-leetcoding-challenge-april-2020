# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
https://www.youtube.com/watch?v=_Es-FEkjKmA
"""
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        length = len(arr)
        i = 0
        return Solution.check_path(root, arr, length, i)
        
    def check_path(root, arr, length, i):
        if not root:
            return length == 0
        if (i == length - 1) and (not root.left and not root.right) and root.val == arr[i]:
            return True
        if i < length and root.val == arr[i]:
            return Solution.check_path(root.left, arr, length, i + 1) or Solution.check_path(root.right, arr, length, i+1)
