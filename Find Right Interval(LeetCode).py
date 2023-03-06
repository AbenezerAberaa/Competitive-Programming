class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        start_idx = {}
        for index, (start, end) in enumerate(intervals):
            start_idx[start] = index
        
        sorted_starts = sorted(list(start_idx.keys()))
        print(sorted_starts)
        
        output = []
        for start, end in intervals:
           
            if end in start_idx:
                output.append(start_idx[end])

            else:
                idx = bisect.bisect_right(sorted_starts, end)
                if idx == len(sorted_starts):
                    output.append(-1)
                else:
                    min_right = sorted_starts[idx]
                    output.append(start_idx[min_right])
        return output
