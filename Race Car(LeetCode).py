class Solution:
    def racecar(self, target: int) -> int:

        default_deque = deque([(0,0,1)])
        while default_deque:
            move , position ,speed = default_deque.popleft()
            if position == target:
                return move
            default_deque.append((move+1, position+speed, speed*2))
            if (position+speed > target and speed > 0) or position + speed < target and speed < 0:
                speed =-1 if speed > 0 else 1
                default_deque.append((move+1,position,speed))
            else:
                continue
        
