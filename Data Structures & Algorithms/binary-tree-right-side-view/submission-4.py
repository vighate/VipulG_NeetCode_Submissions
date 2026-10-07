# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(root, depth):

            if not root:
                return None
            
            if len(res) == depth:
                res.append(root.val)
            
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)

            return res

        dfs(root, 0)
        return res
            
        
        if not root:
            return []
        
        q = deque([root])

        res = []
        while q:
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()

                if i == len_q-1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
