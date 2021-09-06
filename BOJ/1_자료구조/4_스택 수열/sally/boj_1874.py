t = int(input())
s = []  # 수열
tmp = []  # 임시스택
ans = []
cnt = 1
for _ in range(t):
    num = int(input())
    while num >= cnt:
        tmp.append(cnt)
        ans.append('+')
        cnt += 1
    if tmp[-1] == num:
        s.append(tmp.pop())
        ans.append('-')

if tmp:
    print('NO')
else:
    for a in ans:
        print(a)

