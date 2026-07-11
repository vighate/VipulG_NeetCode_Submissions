# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False

        def isSameTree(p,q):
            q = deque([(p,q)])
            while q:
                n1, n2 = q.popleft()

                if not n1 and not n2:
                    continue
                if not n1 or not n2:
                    return False
                if n1.val != n2.val:
                    return False
                
                q.append((n1.left, n2.left))
                q.append((n1.right, n2.right))
            return True

        q = deque([root])

        while q:

            node = q.popleft()

            if isSameTree(node, subRoot):
                return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False