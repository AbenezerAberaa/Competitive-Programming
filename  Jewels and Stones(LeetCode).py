class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = Counter(stones)
        count = 0
        for each in set(jewels):
            count += dic[each]
        return count

