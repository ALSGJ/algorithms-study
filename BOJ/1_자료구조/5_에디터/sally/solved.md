## BOJ1406 에디터

### 아이디어
* 편집기에 입력된 배열을 가지고 있는 스택과, 커서의 움직임을 관리할 스택을 만든다


### 핵심 부분 구현
```python
for _ in range(t):
    ow = sys.stdin.readline().rstrip().split()
    if ow[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif ow[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif ow[0] == 'B':
        if stack1:
            stack1.pop()
    elif ow[0] == 'P':
        stack1.append(ow[1])
```

### 정리
* 처음에는 커서의 인덱스 위치를 저장해서 문자열을 인덱스로 슬라이싱하며 추가/삭제 하는 방법으로 코드를 짰더니 시간초가가 발생했다.
* 커서의 움직임을 스택으로 관리하여서 시간을 줄이는 것이 이 문제의 핵심이였다.
