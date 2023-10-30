# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        nodelist = []
        deleteset = set(to_delete)
        def findnode(root,parent):
            nonlocal nodelist
            if not root:
                return
            leftnd,rightnd=root.left,root.right
            if root.val in deleteset :
                if parent:
                    if parent.left and parent.left.val == root.val:
                        parent.left = None
                    else:
                        parent.right = None
                
                findnode(leftnd,None)
                findnode(rightnd,None)
            else:
                findnode(leftnd,root)
                findnode(rightnd,root)
                
            if not parent and root.val not in deleteset:
                nodelist.append(root)
            return
        findnode(root,None)
        return nodelist
        