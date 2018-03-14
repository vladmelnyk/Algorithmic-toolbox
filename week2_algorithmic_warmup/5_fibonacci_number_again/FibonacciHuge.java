import java.util.*;

public class FibonacciHuge {
    private static long getFibonacciLastDigitNaive(long n, long m) {
        if (n <= 1)
            return n;

        long previous = 0L;
        long current  = 1L;

        for (long i = 0; i < n - 1; ++i) {
            long tmp_previous = previous;
            previous = current;
            current = (tmp_previous + current) % m;
        }

        return current;
    }

    private static long getFibonacciHuge(long n, long m) {

        // long b = System.currentTimeMillis();
        int pisanoPeriodLength = getPisanoPeriodLength(m);
        // System.out.println("pisano " +pisanoPeriodLength);
        // long c = System.currentTimeMillis();

        // System.out.println("time : "+ (c-b));

        int index = (int) ((long)n % (long) pisanoPeriodLength);

        return getFibonacciLastDigitNaive(index, m);
    }

    private static int getPisanoPeriodLength(long m) {

        long a = 0L;
        long b = 1L;
        long c = a + b;
        for (int i = 0; i < m * m; i++) {
            c = (a + b) % m;
            a = b;
            b = c;
            if (a == 0L && b == 1L) {
                return i + 1;    
            }
        }
        return 0;
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long m = scanner.nextLong();
        System.out.println(getFibonacciHuge(n,m));
    }
}

