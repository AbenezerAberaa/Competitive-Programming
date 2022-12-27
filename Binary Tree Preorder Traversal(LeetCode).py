# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        result = []
        stack = []
        curr = root
        
        stack.append(curr)
        

        while stack:
            container = stack.pop()
            if container:
                result.append(container.val)
                stack.append(container.right)
                stack.append(container.left)

        return result

