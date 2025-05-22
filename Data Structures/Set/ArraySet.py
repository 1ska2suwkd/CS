class ArraySet:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def contains(self,e):
        for i in range(self.size):
            if e == self.array[i]:
                return True
        return False
    
    def insert(self,e):
        if not self.contains(e):
            self.array[self.size] = e
            self.size+=1
    
    def delete(self,e):
        if self.contains(e):
            for i in range(self.size):
                if e == self.array[i]:
                    self.array[i] = self.array[self.size-1]
            self.array[self.size-1] = None
            self.size-=1

    def union(self,setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC

    def intersection(self,setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    def difference(self,setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
    def __str__(self):
        return str(self.array[:self.size])

S1 = ArraySet()
S1.insert(5)
S1.insert(2)
S1.insert(3)
S2 = ArraySet()
S2.insert(5)
S2.insert(1)
S3 = S1.difference(S2)

print(S3) 
