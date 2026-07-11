# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            k-=1
            if k==0:
                return root.val

            root = root.right


        # def inorder(node, res):
        #     if not node:
        #         return []
            
        #     inorder(node.left, res)
        #     res.append(node.val)
        #     inorder(node.right, res)

        # res = []
        # inorder(root, res)
        # return res[k-1]


        
        # q = deque([root])
        # res = []

        # while q:

        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         res.append(node.val)

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)


        # res = sorted(res)

        # return res[k-1]