# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
        
        # search in BST

        # def searchBST(root,val):
        #     if not root:
        #         return False
        #     if root.val == val:
        #         return True
        #     if val < root.val:
        #         return searchBST(root.left,val)
        #     else:
        #         return searchBST(root.right,val)

        # flag = searchBST(root,3)
        # print(flag)

        # Insert BST
        
        # def insertBST(root,val):
        #     if not root:
        #         return TreeNode(val)
        #     if val < root.val:
        #         root.left = insertBST(root.left,val)
        #     else:
        #         root.right = insertBST(root.right,val)

        #     return root

        # print tree structure. inorder
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     print(root.val)
        #     inorder(root.right)
        
        # tree = insertBST(root,5)
        # inorder(tree)
