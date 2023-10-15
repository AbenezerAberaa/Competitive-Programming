class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        not_swap, swap = 0, 1
        for i in range(1, n):
            new_nums1 = nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]
            new_nums2 = nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]
            if new_nums1 and new_nums2:
                t = min(not_swap, swap)
                not_swap, swap = t, t + 1
            elif new_nums1:
                swap += 1
            elif new_nums2:
                not_swap, swap = swap, not_swap + 1
        return min(not_swap, swap)
