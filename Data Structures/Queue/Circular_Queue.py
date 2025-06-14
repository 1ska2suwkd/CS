class Queue:
    def __init__(self,capacity=10):
        self.rear = 0
        self.front = 0
        self.capacity = capacity
        self.array = [None]*capacity
    
    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return self.front == (self.rear+1)%self.capacity

    def enqueue(self,e):
        if not self.isFull():
            self.rear = (self.rear+1)%self.capacity
            self.array[self.rear] = e
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%self.capacity
            return self.array[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]

    def size(self):
        if not self.isEmpty():
            return (self.front-self.rear+self.capacity)%self.capacity

    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front+1:self.rear+1])
        else:
            return str(self.array[self.front+1:self.capacity]+self.array[:self.rear+1])

q = Queue(6)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("1,2,3,4,5 추가 ->",q)

print("삭제 ->",q.dequeue()) 
print("삭제 ->",q.dequeue())
print("삭제 ->",q.dequeue())
print("삭제 ->",q.dequeue())
print("결과 ->",q)

q.enqueue(1)
q.enqueue(2)
print("1,2 추가 ->",q)

print("q의 요소의 수 ->",q.size())
