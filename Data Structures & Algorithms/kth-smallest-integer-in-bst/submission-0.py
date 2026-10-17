# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)    # 1. 左の部分木を全部たどる
            vals.append(node.val)
            inorder(node.right)   # 3. 右の部分木を全部たどる
        inorder(root)
        return vals[k - 1]