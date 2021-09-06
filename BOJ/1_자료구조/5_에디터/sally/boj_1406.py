import sys

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []
t = int(input())

for _ in range(t):
    ow = sys.stdin.readline().rstrip().split()
    if ow[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif ow[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif ow[0] == 'B':
        if stack1:
            stack1.pop()
    elif ow[0] == 'P':
        stack1.append(ow[1])

print(''.join(stack1 + list(reversed(stack2))))


