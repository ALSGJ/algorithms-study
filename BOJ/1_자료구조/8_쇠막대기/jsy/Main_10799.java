package study;

import java.util.Scanner;

public class Main_10799 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] line = sc.nextLine().toCharArray();
        int cnt = 0, ans = 0;

        for (int i = 0; i < line.length - 1; i++) {
            if (line[i] == '(' && line[i + 1] == '(') { // 쇠막대기 추가
                ++cnt;
            } else if (line[i] == ')' && line[i + 1] == ')') { // 쇠막대기 끝 & 잘라진 마지막 부분 더하기
                --cnt;
                ++ans;
            } else if (line[i] == '(' && line[i + 1] == ')') { // 쇠막대기 수만큼 잘려짐
                ans += cnt;
            }
        }

        System.out.println(ans);
    }
}
