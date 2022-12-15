class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashes = {}
        for each in nums:
            if each not in hashes:
                hashes[each] = 1
            else:
                return each in hashes
