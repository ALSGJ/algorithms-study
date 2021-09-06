## BOJ1874 스택 수열

### 아이디어
* 스택 수열 배열, 임시 스택 배열, 정답 배열을 만들어서 처리한다.
* count를 세서 입력받은 수보다 count가 같거나 클때까지 임시 스택 배열에 숫자를 넣는다.
* 임시 스택 배열의 마지막 숫자가 입력받은 숫자와 같다면 스택 수열 배열에 넣는다.


### 핵심 부분 구현
```python
    num = int(input())
    while num >= cnt:
        tmp.append(cnt)
        ans.append('+')
        cnt += 1
    if tmp[-1] == num:
        s.append(tmp.pop())
        ans.append('-')
```

### 정리
* 문제를 이해하는데 오래 걸렸던 문제였다.
* 알고리즘 능력 뿐 아니라 독해 능력도 키워야 할 것 같다 😂
