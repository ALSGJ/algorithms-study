import sys

n = list(sys.stdin.readline().rstrip())

# 계산 우선순위 지정을 위해 각 연산자에 대해 우선순위를 지정한다.
opers = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

post = []
op_stack = []
for i in n:
    # 알파벳일 경우 바로 post 스택에 push한다.
    if i.isalpha():
        post.append(i)
    # 여는 괄호일 경우 바로 연산자 스택에 push한다.
    elif i == '(':
        op_stack.append(i)
    # 닫는 괄호일 경우 연산자 스택에 값이 존재하고, 연산자 스택의 마지막 원소가 ( 가 아닐 때 까지 post 스택에 연산자 스택에 원소를 pop하여 넣어준다.
    elif i == ')':
        while op_stack and op_stack[-1] != '(':
            post.append(op_stack.pop())
        # 마지막에 ( 가 남아 있기 떄문에 ( 를 제거해준다.
        op_stack.pop()
    else:
        # 일반적인 연산자가 올 경우 연산자 스택에 값이 존재하고, 연산자 스택에 마지막에 있는 연산자와 지금 연산자와 우선순위를 비교해서 post 스택에 넣어준다.
        while op_stack and opers[i] <= opers[op_stack[-1]]:
            post.append(op_stack.pop())
        op_stack.append(i)

# 조건을 타지 않은 연산자들이 남아있을 수 있으므로 남은 연산자들을 마지막에서부터 꺼내서 post에 넣어준다.
while op_stack:
    post.append(op_stack.pop())

print(''.join(post))