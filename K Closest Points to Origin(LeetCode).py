class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sort = sorted(points,key=lambda a:(a[0])**2+(a[1]**2))
        ans=[]
        for i in range(k):
            ans.append(sort[i])

        return ans
