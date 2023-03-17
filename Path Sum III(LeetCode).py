# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        hash_dic = {0:1}
        self.count = 0
        def pathfind(root, targetSum, hash_dic, prefixSum):

            if not root:
                return
            prefixSum += root.val

            if prefixSum - targetSum in hash_dic:
                self.count += hash_dic[prefixSum - targetSum]
            
            hash_dic[prefixSum] += 1

            pathfind(root.left, targetSum, hash_dic, prefixSum)
            pathfind(root.right, targetSum, hash_dic, prefixSum)

            hash_dic[prefixSum] -= 1
            prefixSum -= root.val

        pathfind(root, targetSum,defaultdict(int, hash_dic), 0)
        return self.count
