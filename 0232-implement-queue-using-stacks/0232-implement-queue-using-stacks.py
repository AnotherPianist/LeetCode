class MyQueue:

    def __init__(self):
        self.stack = []
        self.reserve = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.reserve.append(self.stack.pop())
        val = self.reserve.pop()
        while self.reserve:
            self.stack.append(self.reserve.pop())
        return val

    def peek(self) -> int:
        return self.stack[0]        

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()