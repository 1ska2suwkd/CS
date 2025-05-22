class List:
    def __init__(self,capacity = 100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None
    
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for index in range(self.size, pos, -1):
                self.array[index] = self.array[index-1]
            self.array[pos] = e
            self.size+=1
        else: print("list overflow 또는 유효하지 않는 삽입 위치입니다.")

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for index in range(pos, self.size-1):
                self.array[index] = self.array[index+1]
            self.size-=1
            return e
        else: print("list underflow 또는 유효하지 않는 제거 위치입니다.")

    def __str__(self):
        return str(self.array[:self.size])

    L = list()
    L.insert(0,1)
    L.insert(0,2)
    L.insert(0,3)

    print(L)
