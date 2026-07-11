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

                node1, node2 = q.popleft()

                if not node1 and not node2:
                    continue
                
                if not node1 or not node2:
                    return False

                if node1.val != node2.val:
                    return False

                q.append((node1.left,node2.left))
                q.append((node1.right,node2.right))
            
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

