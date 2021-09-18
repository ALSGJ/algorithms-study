package study;

import java.util.Scanner;
import java.util.Stack;

public class Main_1935 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        String line = sc.next();
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) { // A, B, C, D ...
            arr[i] = Integer.parseInt(sc.next());
        }

        Stack<Double> stack = new Stack<>();
        for (int i = 0; i < line.length(); i++) { // 후위 표기식을 탐색
            char ch = line.charAt(i);
            if (ch >= 'A' && ch <= 'Z') { // 피연산자일 때,
                stack.push(arr[ch - 'A']); // 스택에 넣는다.
            } else {
                // 각각의 연산에 맞게 stack에서 피연산자를 pop하여 연산한다.
                // 그 후, 연산 결과를 다시 stack에 넣는다.
                double a = stack.pop();
                double b = stack.pop();
                switch (ch) {
                    case '*':
                        stack.push(a * b);
                        break;
                    case '/':
                        stack.push(b / a);
                        break;
                    case '+':
                        stack.push(a + b);
                        break;
                    case '-':
                        stack.push(b - a);
                }
            }
        }

        System.out.printf("%.2f", stack.pop()); // 소수 2번째 자리까지 출력
    }
}
