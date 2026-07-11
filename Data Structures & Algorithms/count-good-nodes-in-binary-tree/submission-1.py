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
            return True

        q = deque([(root, root.val)])

        count = 0

        while q:

            node, max_so_far = q.popleft()

            if node.val >= max_so_far:
                count +=1

            newMax = max(node.val, max_so_far)

            if node.left:
                q.append((node.left, newMax))
            
            if node.right:
                q.append((node.right, newMax))
                
        return count
