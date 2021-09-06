## BOJ1406 에디터

### 아이디어
* 2개의 stack을 사용했다.
* 커서의 위치를 기준으로 왼쪽, 오른쪽에 위치한 문자를 나눴다.

### 핵심 부분 구현
```java
	Main_1406(){
        Stack<Character> left = new Stack<>();
        Stack<Character> right = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            left.push(str.charAt(i));
        }
        ...
        switch(line.charAt(0)) {
                case 'L':
                    if(!left.isEmpty()) {
                        right.push(left.pop());
                    }
                    break;
                case 'D':
                    if(!right.isEmpty()) {
                        left.push(right.pop());
                    }
                    break;
                case 'B':
                    if(!left.isEmpty()) {
                        left.pop();
                    }
                    break;
                case 'P':
                    left.push(line.charAt(2));
        }
	}
```

### 정리
* 흔히 사용하는 String 함수를 사용하면 시간초과 .. (2초)
* stack으로 푸는 방법도 있고, linkedList로 푸는 방법도 있으니까 나중에 도전해보자!