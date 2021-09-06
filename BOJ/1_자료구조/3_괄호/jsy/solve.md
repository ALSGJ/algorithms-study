## BOJ9012 괄호

### 아이디어
* greedy하게 괄호 '('의 개수를 세면서 괄호 ')'와 개수만큼 있는지 확인한다.
* 탐색이 끝난 후, '('의 개수가 남아있으면 안된다.

### 핵심 부분 구현
```java
	Main_9012(){
        String line = sc.next();
        int check = 0, idx;
        for (idx = 0; idx < line.length(); idx++) {
            if(line.charAt(idx) == '(') {
                check++;
            } else {
                if(check == 0) {
                    break;
                } else {
                    check--;
                }
            }
        }
        if(check != 0 || idx != line.length()) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
	}
```

### 정리
* 처음엔 stack을 써야한다고 생각했지만, 단순히 괄호의 개수를 카운팅하면 되는 문제였다.