class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        places = []
        for n, start, end in trips:
            # print(n,start,end)
            places.append((start,n))
            places.append((end,-n))

        sums = 0
        for each_place, number in sorted(places):
            # print(each_place, number)
            sums += number
            if sums > capacity:
                return False
        return True
