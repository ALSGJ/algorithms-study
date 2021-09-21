package study;

import java.util.Arrays;
import java.util.Scanner;

public class Main_10809 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.next();
        int[] idx = new int[26]; // a:0, b:1, c:2, ...
        Arrays.fill(idx, -1); // 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력

        for (int i = 0; i < line.length(); i++) {
            if (idx[line.charAt(i) - 'a'] == -1) { // 아직 등장하지 않은 알파벳이라면
                idx[line.charAt(i) - 'a'] = i; // 처음으로 등장하는 위치를 저장한다.
            }
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(idx[i] + " ");
        }
    }
}
