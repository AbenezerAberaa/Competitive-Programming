class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        initially = [False] * n
        
        for into, out in edges:
            initially[out] = True
       
        res = []
        for into in range(n):
            
            if not initially[into]:
                res.append(into)
        return res
