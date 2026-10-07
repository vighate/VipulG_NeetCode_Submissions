# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(root, p):

            if not root:
                return TreeNode(p)

            if p < root.val:
                root.left = dfs(root.left, p)

            if p > root.val:
                root.right = dfs(root.right, p)

            return root
            
        return dfs(root, val)