from ArrayStack import Stack

#좀 더 효율적인 알고리즘 알아보기
def checkBrackets(s):
    stack = Stack(100)
    for ch in s:
        if ch in "({[":
            stack.push(ch)
        if ch in ")}]":
            if stack.peek() == "(" and ch == ")":
                stack.pop()
            elif stack.peek() == "{" and ch == "}":
                stack.pop()
            elif stack.peek() == "[" and ch == "]":
                stack.pop()
            else: return False
    if not stack.isEmpty():
        return False
    elif not s in "({[)}]":
        return False
    return True


s1 = "{ A (i+1) ] = 0; } "
s2 = "if( (i==0) && (j==0)"
s3 = "  "
s4 = "()()(  "

print(s1, " ---> ", checkBrackets(s1))
print(s2, " ---> ", checkBrackets(s2))
print(s3, " ---> ", checkBrackets(s3))
print(s4, " ---> ", checkBrackets(s4))
