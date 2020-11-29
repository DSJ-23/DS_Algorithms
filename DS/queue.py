class Queue:
    def __init__(self):
        self.data = []
        
    def push(self, x: int) -> None:
        self.data.append(x)
        
    def pop(self):
        return self.data.pop(0)
        
    def peek(self):
        return self.data[0]
        
    def empty(self):
        return bool(self.data == [])