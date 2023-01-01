class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_operation = float('inf')
        curr = 0 
        for index in range(len(blocks)):
            if blocks[index] == "W":
                curr += 1 
            if index - k >= 0 and blocks[index - k] == "W":
                curr -= 1
            if index - k + 1 >= 0:
                min_operation = min(curr, min_operation)
                
        return min_operation
