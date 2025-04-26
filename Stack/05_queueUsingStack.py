class MyQueue:

    def __init__(self):
        self.inSt = []
        self.outSt = []

    def push(self, x: int) -> None:
        self.inSt.append(x)

    def pop(self) -> int:
        self._move()
        return self.outSt.pop()

    def peek(self) -> int:
        self._move()
        return self.outSt[-1]

    def empty(self) -> bool:
        return not self.inSt and not self.outSt

    def _move(self):
        if not self.outSt:
            while self.inSt:
                self.outSt.append(self.inSt.pop())


q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(q.empty())
