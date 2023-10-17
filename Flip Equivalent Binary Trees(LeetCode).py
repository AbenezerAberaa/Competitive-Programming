    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None or root1.val != root2.val:
            return False

        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
