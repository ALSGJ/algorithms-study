package study;

import java.util.Scanner;

public class Main_10820 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()) { // EOF 처리
            String line = sc.nextLine();
            int[] arr = new int[4];
            for (int i = 0; i < line.length(); i++) {
                char now = line.charAt(i);
                if(now >= 'a' && now <= 'z') { // 소문자
                    arr[0]++;
                }
                else if(now >= 'A' && now <= 'Z') { // 대문자
                    arr[1]++;
                }
                else if(now >= '0' && now <= '9') { // 숫자
                    arr[2]++;
                }
                else if(now == ' ') { // 공백
                    arr[3]++;
                }
            }
            for (int i = 0; i < 4; i++) {
                System.out.print(arr[i] + " ");
            }
        }
    }
}
