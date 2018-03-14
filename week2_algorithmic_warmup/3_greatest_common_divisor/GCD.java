import java.util.*;

public class GCD {

  private static int gcd_euclidian(int a, int b) {
    int c = 1;
    while (b != 0){
        c = a % b;
        a = b;
        b = c;
      }
      return a;
    }


  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(gcd_euclidian(a, b));
  }
}
