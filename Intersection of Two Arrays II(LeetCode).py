class Solution:
   class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash_map = {}
        for each in nums1:
            if each not in hash_map:
                hash_map[each] = 1
            else:
                hash_map[each] += 1
        val = []
        for each in nums2:
            if each in nums1:
                if each not in val:
                    minu = min(hash_map[each],nums2.count(each))
                    val += minu*[each]
        return val
