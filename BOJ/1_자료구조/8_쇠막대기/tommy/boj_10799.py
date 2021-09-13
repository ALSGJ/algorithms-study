t = list(input())
sticks = []
result = 0
# 입력 받은 괄호만큼 loop 실행
for i in range(len(t)):
    # 여는 괄호일 경우
    if t[i] == '(':
        # 현재보다 앞에 있는 문자가 여는 괄호일 경우, 현재 여는 괄호를 sticks에 넣어준다.
        if t[i + 1] == '(':
            sticks.append(t[i])
        # 현재보다 앞에 있는 문자가 닫는 괄호일 경우, 짝이 맞아 쇠막대기를 자르는 형태가 되므로,
        # 기존에 sticks의 크기가 자른 쇠막대기의 갯수가 된다.
        # 해당 인덱스에서 변경사항이 일어났다면 조건들을 타지 않게 하기 위해서 0으로 변환해준다.
        elif t[i + 1] == ')':
            t[i] = '0'
            t[i + 1] = '0'
            result += len(sticks)
    # 현재 문자가 닫는 괄호일 경우, 리스트에서 pop하고 결과값을 +1 해준다.
    elif t[i] == ')':
        sticks.pop()
        result += 1

print(result)