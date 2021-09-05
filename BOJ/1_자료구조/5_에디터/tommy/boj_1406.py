import sys

stack_left = list(sys.stdin.readline().rstrip())
stack_right = []
n = int(sys.stdin.readline().rstrip())
commands = ['L', 'D', 'B', 'P']

for _ in range(n):
    inp = sys.stdin.readline().rstrip().split()
    if inp[0] == commands[0]:
        if stack_left:
            stack_right.append(stack_left.pop())
    elif inp[0] == commands[1]:
        if stack_right:
            stack_left.append(stack_right.pop())
    elif inp[0] == commands[2]:
        if stack_left:
            stack_left.pop()
    elif inp[0] == commands[3]:
        stack_left.append(inp[1])


print(''.join(stack_left + list(reversed(stack_right))))
