# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        def dfs(root, level):

            if not root:
                return []

            if len(res) == level:
                res.append([])

            res[level].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)
            
            return res
            
        dfs(root, 0)
        return res


        if not root:
            return []
        
        res = []
        
        q = deque([root])

        while q:

            level = []

            for _ in range(len(q)):

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res