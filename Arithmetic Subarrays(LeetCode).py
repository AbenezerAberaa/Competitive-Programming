class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            l_index = l[i]
            r_index = r[i]
            tmp = nums[l_index:r_index+1]
            tmp.sort()
            if(len(tmp)==2):
                res.append(True)
                continue
            distance = tmp[1]-tmp[0]
            for j in range(2, len(tmp)):
                if distance != tmp[j]-tmp[j-1]:
                    res.append(False)
                    break
                elif j==len(tmp)-1:
                    res.append(True)
        return res 
