class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        temp = [(-1)*item for item in piles]
        heapq.heapify(temp)
        for i in range(k):
            maxu = heapq.heappop(temp)
            maxu = maxu - math.ceil(maxu / 2)
            heapq.heappush(temp, maxu)
        return sum(temp) * (-1)
