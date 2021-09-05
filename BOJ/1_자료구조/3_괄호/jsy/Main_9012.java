package study;

import java.util.Scanner;

public class Main_9012 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        for (int i = 0; i < n; i++) {
            String line = sc.next();
            int check = 0, idx;
            for (idx = 0; idx < line.length(); idx++) {
                if (line.charAt(idx) == '(') {
                    check++;
                } else {
                    if (check == 0) {
                        break;
                    } else {
                        check--;
                    }
                }
            }
            if (check != 0 || idx != line.length()) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }
    }
}
