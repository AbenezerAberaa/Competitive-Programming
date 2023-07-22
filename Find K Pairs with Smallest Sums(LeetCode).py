class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        l1, l2 = len(nums1), len(nums2)
        i = 0

        while i<l1 and i<k:
            heappush(h, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))
            i+=1
        res = []

        while k and h:
            e = heappop(h)
            res.append([e[1], e[2]])
            if e[3]<l2-1:
                heappush(h, (e[1]+nums2[e[3]+1], e[1], nums2[e[3]+1], e[3]+1))
            k-=1
        return res
