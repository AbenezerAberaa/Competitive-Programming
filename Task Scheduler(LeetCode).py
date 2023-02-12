class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        curr_time = 0
        heaps = []
        for key,value in Counter(tasks).items():
            heappush(heaps, (-1*value, key))
        while heaps:
            count, temp = 0, []
            while count <= n:
                curr_time += 1
                if heaps:
                    x,y = heappop(heaps)
                    if x != -1:
                        temp.append((x+1,y))
                if not temp:
                    break
                else:
                    count += 1
            for item in temp:
                heappush(heaps, item)
        return curr_time
        
