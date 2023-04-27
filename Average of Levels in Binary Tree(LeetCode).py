from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]: 
        queue = deque()
        queue.append(root)
        print(queue)
        average = []

        while queue:
            curr_lev_count = len(queue)
            total = []

            for each in range(curr_lev_count):
                curr = queue.popleft()
                print(curr)
                total.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            average.append(total)
        return average
