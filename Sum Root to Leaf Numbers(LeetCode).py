# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, num, lst):
        if root == None:
            return lst
        if root.left == None  and root.right == None:
            return lst.append(num + '' + str(root.val))
        else:
            self.helper(root.right, num + str(root.val), lst)
            self.helper(root.left, num + str(root.val), lst)
            return lst
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numList = []
        self.helper(root, '', numList)
        
        ans = 0
        for num in numList:
            ans += int(num)
        
        return ans
