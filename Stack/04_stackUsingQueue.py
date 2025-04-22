from collections import deque


class MyStack:

    def __init__(self):
        self.st = deque()

    def push(self, x: int) -> None:
        self.st.append(x)
        for _ in range(len(self.st)-1):
            self.st.append(self.st.popleft())

    def pop(self) -> int:
        return self.st.popleft()

    def top(self) -> int:
        return self.st[0]

    def empty(self) -> bool:
        return len(self.st) == 0


obj = MyStack()
obj.push(10)
print("Top after push:", obj.top())
param_2 = obj.pop()
print("Popped value:", param_2)


if not obj.empty():
    param_3 = obj.top()
    print("Top after pop:", param_3)
else:
    print("Stack is empty, can't call top.")

param_4 = obj.empty()
print("Is stack empty?:", param_4)
