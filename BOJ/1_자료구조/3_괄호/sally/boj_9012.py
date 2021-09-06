import sys

t = int(input())
stack = []

for _ in range(t):
    stack = []
    bracket = list(sys.stdin.readline().strip())
    for b in bracket:
        if stack:
            pre = stack[-1]
            if b == ')' and pre == '(':
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)
    if stack:
        print("NO")
    else:
        print("YES")