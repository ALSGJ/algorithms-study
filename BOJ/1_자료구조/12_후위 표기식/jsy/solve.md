## BOJ1918 후위 표기식
### 아이디어
* 피연산자는 순서대로 출력되는 성질을 파악하여, 결과에 순서대로 담는다. (추가 연산 필요 없음)
* 연산자는 stack에 담아, 괄호와 우선순위에 따라 순서를 결정한다.

### 핵심 부분 구현
```java
Main_1918(){

    for (int i = 0; i < line.length(); i++) {
            char ch = line.charAt(i);
            if (ch >= 'A' && ch <= 'Z') { // 피연산자
                sb.append(ch); // 결과로 바로 출력하기 위해 담아둠
            } else { // 연산자
                if (ch == '(') {
                    stack.push(ch); // 스택에 넣는다.
                } else if (ch == ')') {
                    while (!stack.isEmpty() && stack.peek() != '(') { // ( 괄호 이후에 스택에 쌓인 연산자를 다 결과로 담는다.
                        sb.append(stack.pop());
                    }
                    if (!stack.isEmpty()) { // ( 괄호를 스택에서 삭제
                        stack.pop();
                    }
                } else { // *, /, +, -
                    while (!stack.isEmpty() && op_rank(stack.peek()) >= op_rank(ch)) { // 현재 연산자보다 스택의 연산자가 우선순위가 더 크면
                        sb.append(stack.pop()); // 스택에서 빼서 결과로 담는다.
                    }
                    stack.push(ch);
                }
            }
        }

}
```

### 정리
* 처음에는 당연하게 피연산자, 연산자 모두를 스택에 넣어야한다고 생각했는데 그러니까 규칙이 안보여서 푸는데 오래 걸렸다..
* **피연산자는 순서대로 출력**된다는 점을 빨리 파악하는게 문제의 핵심같다 !
* ***피연산자와 연산자를 따로 구분해서 각각 성질에 맞는 자료구조로 담을 수 있다는 점을 기억하자 !!!!***