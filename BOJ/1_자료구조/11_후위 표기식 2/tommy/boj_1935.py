n = int(input())
after = ' '.join(list(input()))
stack = []

# 알파벳을 숫자로 변환하는 작업을 하기 위해서 loop하여 입력값을 변환시킨다.
for i in range(n):
    after = after.replace(chr(65 + i), input())


after = after.split()
for a in after:
    # 만약 숫자일 경우, stack에 push한다.
    if a.isalnum():
        stack.append(int(a))
    else:
        # 숫자가 아닐 경우, 계산을 시작하는데, 규칙상 무조건 최소 2개 이상의 숫자가 스택에 들어가 있으므로, 숫자 2개를 pop한다.
        # 나눗셈, 빼기 연산의 경우 두번째 pop된 숫자가 앞에 오게 해야한다.
        tmp1 = stack.pop()
        tmp2 = stack.pop()
        if a == '+':
            stack.append(tmp1 + tmp2)
        elif a == '-':
            stack.append(tmp2 - tmp1)
        elif a == '*':
            stack.append(tmp1 * tmp2)
        elif a == '/':
            stack.append(tmp2 / tmp1)

print('%.2f' % stack[0])