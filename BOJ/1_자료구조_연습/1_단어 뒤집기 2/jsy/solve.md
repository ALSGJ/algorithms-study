## BOJ17413 단어 뒤집기 2

### 아이디어
* stack을 사용하여 뒤집은 단어를 출력하도록 한다.
* 괄호 안에 있는 단어는, StringBuilder의 reverse함수를 통해 원래 순서대로 되돌린다.

### 핵심 부분 구현
```java
Main_17413(){
    if (!isBracket && (now == ' ' || now == '<')) {
        while (!stack.isEmpty()) { // ' ', '<' 전에 스택에 담겨있던 문자 출력
            System.out.print(stack.pop());
        }
        if(now == ' ')
            System.out.print(" ");
        else // '<' 앞에는 공백 출력 필요 없음, 괄호가 열리므로 변수 값 변경
            isBracket = true;
    }
    else if (now == '>') { // 괄호가 닫힘
        System.out.print("<"); // 괄호 안을 출력
        StringBuilder temp = new StringBuilder();
        while (!stack.isEmpty()) { // 스택에서 꺼내면 반대로 나옴
            temp.append(stack.pop());
        }
        System.out.print(temp.reverse()); // reverse를 통해 원래로 되돌림
        System.out.print(">");
        isBracket = false; // 괄호가 끝났으므로 변수 값 변경
    }
    else {
        stack.push(now); // 위의 경우가 아니라면 스택에 문자 넣기
    }
}
```
