from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        neighbors = defaultdict(list)
        for source, dest, price in flights:
            neighbors[source].append([dest, price])
        
        cost_map = {src: 0} 
        queue = deque([(src, 0, 0)])
        while queue:
            city, cost_so_far, stops_taken = queue.popleft()
            for next_city, travel_cost in neighbors[city]:
                if next_city not in cost_map or travel_cost + cost_so_far < cost_map[next_city]:
                    cost_map[next_city] = travel_cost + cost_so_far
                    if stops_taken < K:
                        queue.append((next_city, cost_map[next_city], stops_taken + 1))

        return cost_map[dst] if dst in cost_map else -1
