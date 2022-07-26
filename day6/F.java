import java.util.Scanner;
import java.util.*;
import java.util.Arrays;
import java.util.Vector;

public class F {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();// tamaño del array
        int b = 0;
        String s;
        int v[] = new int[n * 2];
        
        for (int i = 0; i < n * 2; i++) {
            s = sc.next();
            v[i] = sc.nextInt();
            int tmp = v[i];
            i++;
            v[i] = sc.nextInt();
            if (tmp >= 2400 && (v[i] > 2400 && v[i] > tmp) && b == 0) {
                b++;
            }
        }

        if (b == 0) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }
}
