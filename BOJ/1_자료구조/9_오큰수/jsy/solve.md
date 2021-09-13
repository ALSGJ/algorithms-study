## BOJ17298 오큰수
### 아이디어
* stack을 사용하여, 오큰수를 구하지 못한 수와 그 위치 인덱스를 stack에 저장한다.

### 핵심 부분 구현
```java
Main_17298(){
    int[] arr = new int[N];
    Arrays.fill(arr, -1);

    for (int i = 0; i < N; i++) { // 수열을 순차적으로 탐색
        int nowVal = Integer.parseInt(st.nextToken());
        // 현재 input 값이 스택의 값보다 크면
        // 오큰수 '현재 원소 위치보다 큰 수 중에서 가장 왼쪽에 있는 원소' 라고 할 수 있다.
        while (!stack.isEmpty() && stack.peek().val < nowVal) {
            // 정답 배열 중 스택의 가장 위쪽 숫자와 같은 인덱스에 현재 값을 넣는다.
            arr[stack.pop().idx] = nowVal;
        }
        // 다음번에 비교할 (현재 인덱스, 현재 값) 를 push
        stack.push(new Pos(i, nowVal));
    }
}
```

### 정리
* 이중 for문을 쓰면 아주 쉬운 문제지만, 시간제한에 걸려 쓰지 못한다.
* 그러므로 항상 풀이법이 생각나면 시간 복잡도를 먼저 생각하고 구현해나가는 습관을 들이자!