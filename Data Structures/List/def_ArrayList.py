capacity = 100
array = [None]*capacity
size = 0 

def isEmpty(): #리스트가 비어있는 지 확인하는 함수
    if size == 0: return True
    else: return False

def isFull():
    if size == capacity: return True
    else: return False

def getEntry(pos):
    if 0 <= pos < size: return array[pos]
    else:   return None

def insert(pos, e):
    global size
    if not isFull and 0 <= pos <= size:
        for index in range(size,pos,-1): #맨 뒤부터 앞으로 옮기는게 중요
            array[index] = array[index-1]
        array[pos] = e 
        size += 1
    else: 
        print("리스트 overflow 또는 유효하지 않는 삽입 위치")
        exit()

def delete(pos):
    global size
    if not isEmpty and 0 <= pos < size:
        e = array[pos]
        for index in range(pos,size-1):
            array[index] = array[index+1]
        size -= 1
        return e
    else:
        print("리스트 underflow 또는 유효하지 않는 삽입 위치")
        exit()
