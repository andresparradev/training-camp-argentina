import java.util.Scanner;
import java.util.*;

public class PresentFromLena
{
public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt() + 1;
    int x = 0;
    int y = 0;
    int z = -1;
    // imprime la mitad superior
    for (int i = 1; i <= n; i++)
    {
	// espacio de impresión
	for (int j = i; j < n; j++) {
	    System.out.print(' ');
	    System.out.print(' ');
	}

	// impresión 
	for (int k = 1; k < 2*i; k++) {
	  if (k!=1) {
	    System.out.print(' ');
	  }
	    if(x == y || z == 1){
		System.out.print(x);
		x--;
		z = 1;
	    }else{
		System.out.print(x);
		x++;
	    }
	}

	// pasar a la siguiente linea
	System.out.print(System.lineSeparator());
	y++;
	x = 0;
	z = 0;
    }
    y--;
    // imprime la mitad inferior
    for (int i = n - 1; i >= 1; i--)
    {
	// espacio de impresión
	for (int j = n; j > i; j--) {
	    System.out.print(' ');
	    System.out.print(' ');
	}

	// impresión 
	for (int k = 1; k < (i * 2); k++) {
	  if (k!=1) {
	    System.out.print(' ');
	  }
	  
	    if(x == y || z == 1){
		x--;
		System.out.print(x);
		z = 1;
	    }else{
		System.out.print(x);
		if(x+1 != y){
		    x++;
		}else{
		    z=1;
		}
	    }
	}

	// pasar a la siguiente linea
	System.out.print(System.lineSeparator());
	y--;
	x = 0;
	z = 0;
    }
}
}
