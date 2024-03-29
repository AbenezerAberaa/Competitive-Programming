# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        answer=[]
        def backtrace(root,path=[]):
            if not root:
                return
            if not root.left and not root.right:
                path.append(str(root.val))
                answer.append("".join(path.copy()))
                path.pop()
                return 
            add = str(root.val)+"->"
            path.append(add)
            backtrace(root.left,path)
            backtrace(root.right,path)
            path.pop()      
    
        backtrace(root)
        return answer
