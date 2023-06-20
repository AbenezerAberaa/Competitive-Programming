class Solution:
    total = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if(root == None):
            return

        if(root.val%2 == 0):
            self.GrandChildren(root.left)
            self.GrandChildren(root.right)

        self.sumEvenGrandparent(root.left)
        self.sumEvenGrandparent(root.right)

        return self.total


    def GrandChildren(self,root):
        if(root != None and root.left != None):
            self.total+= root.left.val
            
        
        if (root != None and root.right != None):
            self.total += root.right.val
