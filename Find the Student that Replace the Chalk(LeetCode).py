class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for index in range(len(chalk)):
            if chalk[index]>k:
                return index
            k -= chalk[index]   