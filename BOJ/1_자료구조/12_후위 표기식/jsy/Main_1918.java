package study;

import java.util.Scanner;
import java.util.Stack;

public class Main_1918 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.next();

        Stack<Character> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

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

        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        System.out.println(sb);
    }

    private static int op_rank(char op) {
        int result = 0;
        if (op == '*' || op == '/') {
            result = 2;
        } else if (op == '+' || op == '-') {
            result = 1;
        }
        return result;
    }
}
