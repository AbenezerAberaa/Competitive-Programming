class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if n <= time * 2:
            return []

        left, right = [0] * n, [0] * n
        for index in range(1,n):
            if security[index] <= security[index - 1]:
                left[index] = left[index - 1] + 1

        for index in range(n - 2, -1, -1):
            if security[index] <= security[index + 1]:
                right[index] = right[index + 1] + 1
        arr = []
        for index in range(n):
            if time <= min(left[index], right[index]):
                arr.append(index)
        return arr
        
