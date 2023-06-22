# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = {}
        
        stack = [root]
        while stack: 
            node = stack.pop()
            for child in (node.left, node.right): 
                if child: 
                    stack.append(child)
                    graph.setdefault(node.val, []).append(child.val)
                    graph.setdefault(child.val, []).append(node.val)
        
        queue = [target.val]
        seen = set()
        while queue: 
            if K == 0: break 
            newq = []
            for n in queue: 
                seen.add(n)
                newq.extend(nn for nn in graph.get(n, []) if nn not in seen)
            K -= 1
            queue = newq
        return queue
