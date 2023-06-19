class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        que = deque()
        visited = [0]
        
        for i in range(len(rooms[0])):
            que.append(rooms[0][i])
        
        while que:
            key = que.popleft()
            if key not in visited:
                for i in range(len(rooms[key])):
                    que.append(rooms[key][i])
                
                visited.append(key)
                if len(visited) == len(rooms):
                    return True
        
        return False
