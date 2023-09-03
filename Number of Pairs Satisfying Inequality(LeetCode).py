class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:


        result = 0
        size = len(nums1)
        nums = [nums1[i] - nums2[i] for i in range(size)]
        visited = []
        for i in range(size - 1, -1, -1):
            if not visited:
                visited.append(nums[i] + diff)
            else:
                pos = bisect.bisect_left(visited, nums[i])
                result += len(visited) - pos
                bisect.insort(visited, nums[i] + diff)
        return result
