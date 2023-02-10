class Solution:
    def captureForts(self, forts: List[int]) -> int:
        prev = 0
        maxu = 0
        for right, value in enumerate(forts):
            if value == 1 or value == -1:
                if value == (-1)*forts[prev]:
                    curr_max = right - prev - 1
                    maxu = max(maxu, curr_max)
                    prev = right
                else:
                    prev = right
        return maxu or 0

