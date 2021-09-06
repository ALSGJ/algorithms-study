## BOJ10828 스택

### 아이디어
* switch문으로 스택 명령어를 구분한다.
* 0.5초라는 시간 내에 완료되도록 하기 위해, Scanner가 아닌 BufferedReader를 사용한다.


### 핵심 부분 구현
```java
	Main_10828(){
              switch(line[0]) { // command
                case "push": // push command에 대한 처리
                    
                    break;
                case "pop": // pop command에 대한 처리
                    if(stack.isEmpty()) { // 스택이 비어있을 때 처리
                    
                    } else { // 스택에 값이 있을 때 처리
                    
                    }
                    break;
                    ...
	}
```

### 정리
* 쉬운 문제였지만, 단순히 Scanner로 input 값을 받았다가 시간 초과가 되었다.
* 백준에서 알고리즘 문제를 풀 때는 입력값을 받을 때도 최적화해야겠다고 생각했ㅁ다.
