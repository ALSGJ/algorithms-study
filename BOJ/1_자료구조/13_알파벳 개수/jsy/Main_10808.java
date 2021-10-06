package study;

import java.util.Scanner;

public class Main_10808 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.next();
        int[] count = new int[26]; // 알파벳 개수 저장

        for (int i = 0; i < line.length(); i++) {
            count[line.charAt(i) - 'a']++; // a = 0, b = 1, ...
        }
        for (int i = 0; i < 26; i++) {
            System.out.print(count[i] + " ");
        }
    }
}
