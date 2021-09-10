package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main_17298 {

    static class Pos {
        int idx, val;

        Pos(int idx, int val) {
            this.idx = idx;
            this.val = val;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        Arrays.fill(arr, -1);

        StringTokenizer st = new StringTokenizer(br.readLine());
        Stack<Pos> stack = new Stack<>();
        for (int i = 0; i < N; i++) { // 수열을 순차적으로 탐색
            int nowVal = Integer.parseInt(st.nextToken());
            // 현재 input 값이 스택의 값보다 크면
            // 오큰수 '현재 원소 위치보다 큰 수 중에서 가장 왼쪽에 있는 원소' 라고 할 수 있다.
            while (!stack.isEmpty() && stack.peek().val < nowVal) {
                // 정답 배열 중 스택의 가장 위쪽 숫자와 같은 인덱스에 현재 값을 넣는다.
                arr[stack.pop().idx] = nowVal;
            }
            // 다음번에 비교할 (현재 인덱스, 현재 값) 를 push
            stack.push(new Pos(i, nowVal));
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(arr[i]).append(" ");
        }
        System.out.print(sb);
    }
}
