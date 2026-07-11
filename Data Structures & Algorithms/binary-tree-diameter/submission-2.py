# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def maxDepth(root):

            if not root:
                return 0

            q = deque([root])
            max_depth = 0

            while q:
                max_depth += 1

                for _ in range(len(q)):

                    node = q.popleft()

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            return max_depth

        diameter = 0

        if not root:
            return 0

        q = deque([root])

        while q:

            node = q.popleft()
            left = maxDepth(node.left)
            right = maxDepth(node.right)

            diameter = max(diameter, left+right)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return diameter

