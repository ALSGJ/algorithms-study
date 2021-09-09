package study;

import java.util.Scanner;
import java.util.Stack;

public class Main_17413 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Character> stack = new Stack<>();

        String line = sc.nextLine();
        boolean isBracket = false;

        for (int i = 0; i < line.length(); i++) {
            char now = line.charAt(i);

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

        while (!stack.isEmpty()) { // 마지막으로 남은 문자 출력
            System.out.print(stack.pop());
        }
    }
}
