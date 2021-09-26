from sys import stdin

n = int(input())
stack = []
for _ in range(n):
    # push일 경우, split하여 처리하기 위함
    commands = stdin.readline().rstrip().split()
    if commands[0] == 'push':
        stack.append(commands[1])
    elif commands[0] == 'pop':
        if stack: # stack만 해도 True, False 체크 가능하다.
            print(stack.pop())
        else:
            print(-1)
    elif commands[0] == 'size':
        print(len(stack))
    elif commands[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif commands[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
