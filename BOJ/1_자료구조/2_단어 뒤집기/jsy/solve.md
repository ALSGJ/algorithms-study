## BOJ9093 단어 뒤집기

### 아이디어
* StringBuilder의 reverse 함수를 사용하여 뒤집힌 단어로 나오도록 한다.
* I/O에서 BufferedReader, StringTokenizer, StringBuilder를 사용하여 실행시간을 줄인다.


### 핵심 부분 구현
```java
	Main_9093(){
            StringTokenizer st = new StringTokenizer(br.readLine());
            StringBuilder sb = new StringBuilder();
            while(st.hasMoreTokens()) {
                StringBuilder temp = new StringBuilder(st.nextToken());
                sb.append(temp.reverse()).append(" ");
            }
            System.out.println(sb);
	}
```

### 정리
* 쉬운 문제였지만, 또 I/O를 고려 안했다가 시간 초과가 되었다.
* 10번은 틀린거같다ㅠㅠ..