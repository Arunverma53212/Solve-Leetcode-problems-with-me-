# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        def preorder(root):
            if root is None:
                return 0

            lheight = preorder(root.left)
            rheight = preorder(root.right)

            return 1 + max(lheight, rheight)

        # return preorder(root)
        def inorder(root):
            if root is None:
                return 0

            lheight = inorder(root.left)

            rheight = inorder(root.right)

            return 1 + max(lheight, rheight)
        return inorder(root)


        def postorder(root):
            if root is None:
                return 0

            lheight = postorder(root.left)

            rheight = postorder(root.right)

            height = 1 + max(lheight, rheight)

            return height

        # return postorder(root)
    