class Stack:
    def __init__(self,capacity=10):
        self.top = -1 #Stack 상단에 있는 인덱스 번호
        self.capacity = capacity
        self.array = [None]*self.capacity

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self,e):
        if not self.isFull():
            self.top+=1
            self.array[self.top] = e
        else: exit()
    
    def pop(self):
        if not self.isEmpty():
            e = self.array[self.top]
            self.array[self.top] = None
            self.top-=1
            return e
        else: exit()
    
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: exit()

    def __str__(self):
        return str(self.array[:self.top+1])

S = Stack()

S.push(1)
S.push(2)
S.push(3)

print(S.peek())
print(S.pop())
print(S)
