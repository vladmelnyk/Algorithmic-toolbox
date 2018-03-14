import java.util.*;

public class LCM {
   private static int gcd_euclidian(int a, int b) {
    int c = 1;
    while (b != 0){
        c = a % b;
        a = b;
        b = c;
      }
      return a;
    }

   private static long lcm_fast(int a, int b) {
    return ((long)a * b) / (gcd_euclidian(a,b));
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(lcm_fast(a, b));
  }
}
