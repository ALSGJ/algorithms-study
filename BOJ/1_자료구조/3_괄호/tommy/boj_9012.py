n = int(input())

for _ in range(n):
    vps = input()
    stack = []
    result = True
    for vp in vps:
        if (not len(stack)) and (vp == ')'):
            result = False
            break
        if vp == '(':
            stack.append(vp)
        else:
            stack.pop()
    if len(stack): result = False
    if result:
        print('YES')
    else:
        print('NO')