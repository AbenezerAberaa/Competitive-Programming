class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.sums = 0
        def tiltval(root):
            
            if not root:
                return 0 
            l = tiltval(root.left)
            r = tiltval(root.right)
            self.sums += abs(r-l)

            return l + r + root.val

        tiltval(root)
            
        return self.sums
        
