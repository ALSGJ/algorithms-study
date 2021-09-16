package study;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main_1158 {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }
        int cnt = 1;
        while (queue.size() > 1) { // 큐에 1개가 남을 때까지 반복
            if (cnt == K) { // K만큼 카운팅이 되면
                sb.append(queue.poll()).append(", "); // 원에서 해당하는 사람을 제거
                cnt = 0; // 카운팅 변수 초기화
            } else {
                queue.offer(queue.poll()); // 앞에 있는 사람을 맨 뒤로 보냄
            }
            ++cnt; // 한 턴이 끝남
        }
        sb.append(queue.poll()); // 마지막은 ,을 넣지 않기 위함
        System.out.println("<" + sb + ">");
    }
}
