class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        heap = []
        time = 0
        i = 0
        ans = []    
        while len(ans) != len(tasks):
            if not heap and i < len(tasks) and time < tasks[i][0]:
                time = tasks[i][0] 
            
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            ans.append(heap[0][1])
            time += heap[0][0]
            heapq.heappop(heap)

        return ans
