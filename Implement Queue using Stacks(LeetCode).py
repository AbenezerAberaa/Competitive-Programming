class MyQueue:
    def __init__(self):
        self.firstStack = []
        self.secondStack = []
        self.front = None
        

    def push(self, x: int) -> None:
        if not self.firstStack:
            self.front = x
        self.firstStack.append(x)
        
        

    def pop(self) -> int:
        if not self.secondStack:
            while self.firstStack:
                self.secondStack.append(self.firstStack.pop())
            
        container = self.secondStack.pop()
            
        return container

    def peek(self) -> int:
        if self.secondStack:
            return self.secondStack[-1]
            
        return self.front
        

    def empty(self) -> bool:
        if (not self.firstStack and not self.secondStack):
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()