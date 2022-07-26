import java.util.Scanner;
import java.util.Arrays;

public class J {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();// tamaño del array
        int v[] = new int[n];
        int tmp = 0;
        int rta = 0;
        int k = 0;
        int vector[] = new int[n];
        for (int i = 0; i < n; i++) {
            v[i] = sc.nextInt();
            if (tmp < v[i]) {
                rta++;
            } else {
                vector[k] = rta;
                k++;
                rta = 1;
            }
            tmp = v[i];
        }
        vector[k] = rta;
        Arrays.sort(vector);
        System.out.println(vector[vector.length - 1]);
    }
}
