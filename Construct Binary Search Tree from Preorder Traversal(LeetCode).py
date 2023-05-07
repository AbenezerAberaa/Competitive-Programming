# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        length = len(preorder)
        def helper(maxBound):
            if(self.i == length or preorder[self.i]> maxBound):
                return None
            curr = preorder[self.i]
            root = TreeNode(curr)
            self.i += 1
            root.left = helper(curr)
            root.right = helper(maxBound)

            return root
        return helper(float("inf"))
