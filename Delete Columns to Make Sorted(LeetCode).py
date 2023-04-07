class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

         
        arr = []
        
        for col in range(len(strs)-1):
            for row in range(len(strs[0])):
                if strs[col][row] > strs[col+1][row]:
                    arr.append(row)
                    
        return len(set(arr))
