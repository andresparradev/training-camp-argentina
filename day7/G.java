import java.util.Scanner;

public class G {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long n;
        n = sc.nextInt();
        int m = 5;
        int p = 10;
        int c = 2;
        int a = 1;

        if (n < 5) {
            if (n == 4 || n == 3) {
                System.out.println(8);
            }
            if (n == 2) {
                System.out.println(6);
            }
            if (n == 1) {
                System.out.println(4);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= c; j++) {
                if (n > m) {
                    m++;
                }
                if (c != j) {
                    if (n == m) {
                        System.out.println(p);
                        a = 2;
                        break;
                    }
                } else {
                    if (n == m) {
                        p += 2;
                        System.out.println(p);
                        a = 2;
                        break;
                    }
                }
            }

            a++;

            if (a == 3) {
                break;
            }

            if (n == m && a != 3) {
                System.out.println(p);
                break;
            }

            if (a == 2) {
                c++;
                a = 0;
            }
            p += 2;

        }
    }
}
