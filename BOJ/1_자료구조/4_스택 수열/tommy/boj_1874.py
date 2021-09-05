import sys

n = int(sys.stdin.readline().rstrip())

nums = [i for i in range(1, n + 1)]

stack1 = []
stack2 = []
result = []
for _ in range(n):
    temp = int(sys.stdin.readline().rstrip())
    while nums.count(temp):
        # push
        stack1.append(nums.pop(0))
        result.append("+")

    # pop
    if stack1[-1] == temp:
        stack2.append(stack1.pop())
        result.append("-")


if stack1:
    print("NO")
else:
    for item in result:
        print(item)
