# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi = float('-inf')
        def solve(root):
            nonlocal maxi
            if root is None:
                return 0
            leftsum = solve(root.left)
            if leftsum < 0:
                leftsum = 0

            rightsum = solve(root.right)
            if rightsum < 0:
                rightsum = 0

            maxi = max(maxi,root.val+leftsum+rightsum)
            return root.val+max(leftsum,rightsum)
        solve(root)
        return maxi





