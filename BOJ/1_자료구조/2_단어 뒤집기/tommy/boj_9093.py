n = int(input())

for _ in range(n):
    case = input()
    stack = []
    result = ''
    for i in range(len(case)):
        if case[i] != ' ': stack.append(case[i])
        if i == len(case) - 1 or case[i] == ' ':
            while len(stack):
                result += stack.pop()
            if case[i] == ' ': result += ' '

    print(result)