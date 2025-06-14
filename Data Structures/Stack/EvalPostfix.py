from Class_ArrayStack import Stack

expr1 = ['8','2','/','3','-','3','2','*','+']
expr2 = ['1','2','/','4','*','1','4','/','*']

def evalPostfix(expr):
    s = Stack(100)
    for token in expr:
        if token in "+-/*":
           val2 = s.pop()
           val1 = s.pop()
        if token == '+':    s.push(val1 + val2)
        elif token == '-':    s.push(val1 - val2)
        elif token == '*':    s.push(val1 * val2)
        elif token == '/':    s.push(val1 / val2)
        else:   s.push(int(token))
    return s.peek()

print(expr1,"---->",evalPostfix(expr1))
print(expr2,"---->",evalPostfix(expr2))
