class Solution:
    def find_gcd(self, first:int, Second:int)->int:
        if not Second:
            return first
        return self.find_gcd(Second, first % Second)

    def gcd(self, arr: List[int]) -> int:
        greatest = arr[0]
        for n in arr[1:]:
            greatest = self.find_gcd(greatest, n)
            if greatest == 1:
                return 1
        return greatest

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = collections.Counter(deck)
        count = [dic[n] for n in dic]

        return self.gcd(count) >= 2
