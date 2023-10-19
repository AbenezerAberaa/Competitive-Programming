class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.inorder = []
        
        def inorder(root):
            if not root: return
            inorder(root.left)
            self.inorder.append(root.val)
            inorder(root.right)
            
        inorder(root)
        
        return self.inorder[k-1]
