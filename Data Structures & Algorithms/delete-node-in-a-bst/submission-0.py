# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(root, p):

            if not root:
                return None

            if p < root.val:
                root.left = dfs(root.left, p)

            elif p > root.val:
                root.right = dfs(root.right, p)

            else:

                if not root.left:
                    return root.right
                
                elif not root.right:
                    return root.left

                else:

                    curr = root.right

                    while curr.left:
                        curr = curr.left

                    root.val = curr.val
                    root.right = dfs(root.right, root.val)

            return root

        return dfs(root, key) 