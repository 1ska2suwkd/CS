#dequeue()를 할 경우 무조건 모든 인덱스가 이동하기 때문에 시간 복잡도가 O(N)으로 비효율적
class Queue:
    def __init__(self,capacity=10):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity-1

    def enqueue(self,e):
        if not self.isFull():
            self.array[self.size] = e
            self.size+=1
    
    def dequeue(self):
        if not self.isEmpty():
            e = self.array[0]
            for i in range(self.size-1):
                self.array[i] = self.array[i+1]
            self.size-=1
            return e
    
    def peek(self):
        if not self.isEmpty():
            return self.array[0]

    def __str__(self):
        return str(self.array[:self.size])

Q = Queue()

Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
print(Q.dequeue())
Q.enqueue(6)
print(Q.dequeue())
print(Q.peek())

print(Q)
