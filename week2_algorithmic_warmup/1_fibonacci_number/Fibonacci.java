import java.util.Scanner;

public class Fibonacci {
  private static int[] intArr = new int[50];
  
  private static long calc_fib(int n) {
  	intArr[0] = 0;
  	intArr[1] = 1;
    for (int i = 2 ;i <= n; i++) {
      intArr[i] = intArr[i-1]+ intArr[i-2]; 
    }
    return intArr[n];
  }

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    System.out.println(calc_fib(n));
  }
}