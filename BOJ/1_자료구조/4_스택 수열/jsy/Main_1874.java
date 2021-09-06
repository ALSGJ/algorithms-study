package study;

import java.util.Scanner;
import java.util.Stack;

public class Main_1874 {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int idx = 0;
        for (int i = 1; i <= n; i++) {
            stack.push(i);
            sb.append("+").append("\n");
            while (!stack.empty() && stack.peek() == arr[idx]) {
                stack.pop();
                sb.append("-").append("\n");
                idx++;
            }
        }

        if (!stack.isEmpty()) {
            System.out.print("NO");
        } else {
            System.out.print(sb);
        }
    }
}