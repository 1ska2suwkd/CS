from Class_ArrayStack import Stack

infix1 = ['3','*','4','+','5','*','6']
infix2 = ['5','/','10','*','4','+','4','*','(','3','+','2',')']

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
    
def precedence (op):
    if op in "()":  return 0
    elif op in "+-":  return 1
    elif op in "*/":  return 2
    else:   return -1

def Infix2Postfix(expr):
    S = Stack(100)
    output = []

    for term in expr:

        if term == '(':
            S.push("(")

        elif term == ')':
            while not S.isEmpty():
                op = S.pop()
                if op == "(":
                    break
                else:   output.append(op)

        elif term in "*/+-":
            while not S.isEmpty():
                if  precedence(term)<=precedence(S.peek()):
                    output.append(S.pop())
                else:   break
            S.push(term)
            
        else:
            output.append(term)
    while not S.isEmpty():
        output.append(S.pop())

    return output

postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)

print("중위표기:",infix1)
print("후위표기:",postfix1)
print("계산결과:",result1,end="\n\n")
print("중위표기:",infix2)
print("후위표기:",postfix2)
print("계산결과:",result2,end="\n\n")
