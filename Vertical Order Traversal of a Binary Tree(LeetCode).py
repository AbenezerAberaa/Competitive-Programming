# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        col_ind= defaultdict(list)
        def helper(root,row,col,col_ind):
            if not root:
                return [row,col]
            r,c = helper(root.left,row+1 if root.left else row , col - 1 if root.left else col, col_ind)
            col_ind[c].append([r,root.val])
            r,c = helper(root.right,row+1 if root.right else row , col+1 if root.right else col, col_ind)
            return [row-1,col+1]
            
        helper(root,0,0,col_ind)
        ans=[]
        for item in sorted(col_ind.keys()):
            col_ind[item].sort()
            temp=[]
            for item in col_ind[item]:
                temp.append(item[-1])
            ans.append(temp)
        return ans
