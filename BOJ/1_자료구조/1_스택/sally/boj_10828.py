import sys

n = int(input())
stack = []


def push(number):
    stack.append(number)


def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)


def size():
    print(len(stack))


def empty():
    if stack:
        print(0)
    else:
        print(1)


def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)


for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "top":
        top()
