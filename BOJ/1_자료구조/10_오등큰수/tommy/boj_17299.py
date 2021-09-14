from collections import Counter

# 오큰수를 이전에 풀어봤으므로 기존 로직은 같다고 보고 풀이에 들어갔다.
# 다른 점이라면, 현재 숫자보다 더 많이 등장한 숫자 중 가장 왼쪽에 있는 수를 구해야 하므로, 기존 로직 + 배열 내 원소별 등장 횟수를 구하기 위한 로직을 추가했다.
n = int(input())
nums = list(map(int, input().split()))
# 한가지 다른 점은 nums에 들어있는 원소들 중 중복된 원소들의 갯수를 구해주기 위해, Counter함수를 써서 dict 형태로 반환했다.
nums_count = dict(Counter(nums))
stack = [0]
result = [-1 for _ in range(n)]

for i in range(1, n):
    while stack:
        # 기존 조건문과 동일한 구조이지만, nums_count 딕셔너리를 기준으로 지금 현재 숫자의 등장횟수와 stack에서 꺼낸 인덱스에 해당하는 숫자의 등장 횟수를
        # 비교하는 로직을 사용했다.
        if nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
            result[stack.pop()] = nums[i]
        else:
            break
    stack.append(i)

print(' '.join(map(str, result)))