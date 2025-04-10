from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if not self.IsEmpyt() else None

    def IsEmpyt(self):
        return len(self.stack) == 0
    

s = Stack()
s.push(10)
s.push(15)
print(s.pop())


    