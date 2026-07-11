# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0

            q = deque([root])
            height = 0
            while q:

                height +=1
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            return height

        if not root:
            return True

        q = deque([root])

        while q:
            for _ in range(len(q)):

                node = q.popleft()
                left = height(node.left)
                right = height(node.right)

                if abs(left-right) > 1:
                    return False

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return True

        
        # def height(root):

        #     if not root:
        #         return 0

        #     left = height(root.left)
        #     if left == -1:
        #         return -1

        #     right = height(root.right)
        #     if right == -1:
        #         return -1

            
        #     if abs(left-right)>1:
        #         return -1

        #     return 1 +max(left,right)

        # height(root)

        # if height(root) == -1:
        #     return False
        # return True
