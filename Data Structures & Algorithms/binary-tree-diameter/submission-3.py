# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root):
            if not root:
                return 0

            q = deque([root])
            height = 0
            while q:
                height+=1

                for _ in range(len(q)):
                    node = q.popleft()

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            return height

            
        diameter = 0
        q = deque([root])

        if not root:
            return 0

        while q:

            for _ in range(len(q)):
                node = q.popleft()

                left = height(node.left)
                right = height(node.right)

                diameter = max(diameter, left+right)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return diameter

        

        
        
        # self.diameter = 0

        # def height(root):

        #     if not root:
        #         return 0

        #     lmax = height(root.left)
        #     rmax = height(root.right)

        #     self.diameter = max(self.diameter, lmax+rmax)

        #     return 1 + max(lmax,rmax)

        # height(root)

        # return self.diameter

        # # self.diameter = 0

        # def height(root):
        #     if not root:
        #         return 0


        #     lmax = height(root.left)
        #     rmax = height(root.right)

        #     self.diameter = max(self.diameter, lmax+rmax)

        #     return 1 + max(lmax,rmax)

        # height(root)
        # return self.diameter