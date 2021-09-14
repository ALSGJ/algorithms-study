n = int(input())
nums = list(map(int, input().split()))
# 스택에 0을 넣어 최초에 선언한다.
# 다른 조건을 걸지 않고 바로 while loop를 태우기 위해서이다.
# stack에는 nums의 인덱스 값을 넣어줘서 stack에 저장되는 인덱스는 nums의 실제 원소들에 대하여 왼쪽부터 큰 순서대로 들어가게 된다.
# 그 이유는 현재 인덱스에서 바로 오른쪽에 있는 수가 현재 수보다 작기 때문에 현재 인덱스에서의 숫자는 가장 가까운 큰 수를 다음 loop에서 찾아야하기 떄문에
# 임시로 저장해둔다.
stack = [0]
# 최초에 -1로 n만큼 result 리스트 원소를 초기화한다. (오큰수가 없을 경우 -1을 그대로 반환하기 위한 목적)
result = [-1 for _ in range(n)]

for i in range(1, n):
    # stack에 인덱스 값이 들어있는지에 대해 조건을 두는 이유는 오큰수를 못찾아 대기하는 수들이 오큰수를 만나면 바로바로 오큰수를 반환해줘야하기 때문이다.
    while stack:
        # stack의 제일 마지막 숫자를 꺼내 nums의 인덱스로 사용해서 현재 값과 비교한다.
        if nums[stack[-1]] < nums[i]:
            # 만약 현재값이 스택에 있는 수보다 클 경우, 스택의 마지막 숫자를 꺼내고, 결과값에 오큰수를 입력한다.
            tmp = stack.pop()
            result[tmp] = nums[i]
        # 현재 값과 비교했을 때, 오큰수가 아닐 경우, loop를 종료한다.
        else:
            break
    # 현재 값이 다음 오큰수 찾기를 위한 비교값이 되므로, 스택에 현재 값의 인덱스를 저장해준다.
    stack.append(i)


print(' '.join(map(str, result)))