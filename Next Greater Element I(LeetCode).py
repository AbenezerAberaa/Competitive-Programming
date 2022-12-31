class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        stack = []
        dic = {}
        for num in nums2:
            while stack != [] and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)
        
        result = []
        for num in nums1:
            if num in dic:
                result.append(dic[num])
            else:
                result.append(-1)

        return result


