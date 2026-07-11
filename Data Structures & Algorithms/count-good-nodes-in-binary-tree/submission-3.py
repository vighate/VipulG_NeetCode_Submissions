# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        def dfs(node, max_so_far):

            if not node:
                return 0

            count = 0
            if node.val >= max_so_far:
                count +=1
            max_so_far = max(max_so_far, node.val)

            return (count + dfs(node.left, max_so_far) +
                    dfs(node.right, max_so_far))

        return dfs(root, float('-inf'))
        







        
        # def dfs(root, max_val):

        #     if not root:
        #         return 0
            
        #     if root.val >= max_val:
        #         good = 1
        #         max_val = root.val
        #     else:
        #         good = 0
            
        #     good += dfs(root.left, max_val)
        #     good += dfs(root.right, max_val)

        #     return good

        # return dfs(root, -9999999)