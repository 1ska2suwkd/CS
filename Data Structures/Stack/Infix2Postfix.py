from Class_ArrayStack import Stack

infix1 = ['8','/','2','-','3','+','(','3','*','2',')']
infix2 = ['1','/','2','*','4','*','(','1','/','4',')']
S = Stack(100)

def precedence (op):
    if op in "()":  return 0
    elif op in "+-":  return 1
    elif op in "*/":  return 2
    else:   return -1

def Infix2Postfix(expr):
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

print("중위표기:",infix1)
print("후위표기:",Infix2Postfix(infix1),end="\n\n")
print("중위표기:",infix2)
print("후위표기:",Infix2Postfix(infix2))
