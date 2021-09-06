## BOJ1874 스택 수열

### 아이디어
* stack에 input으로 받은 값만큼 push해주면서 +를 추가한다.
* push하다가 찾는 숫자를 만났다면(arr[idx])  -를 추가한다.

### 핵심 부분 구현
```java
    int idx = 0;
    for (int i = 1; i <= n; i++) {
        stack.push(i);
        sb.append("+").append("\n");
        while (!stack.empty() && stack.peek() == arr[idx]) {
            stack.pop();
            sb.append("-").append("\n");
            idx++;
        }
    }
```

### 정리
* 어려웠고 오래걸렸다. . ㅠ ㅠ
* stack 자료구조로 다양한 로직을 구현할 수 있다는 것을 배웠다.