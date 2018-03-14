import java.util.*;

public class FibonacciSumLastDigit {

    private static long getFibonacciSumFast(long n) {
        if (n <= 1)
            return n;

        n +=2;
        return getFibonacciHuge(n,10);
    }

    private static long getFibonacciHuge(long n, long m) {

        long pisanoPeriodLength = 60L;
    
        long index = (n % pisanoPeriodLength);

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

    private static long getFibonacciLastDigitNaive(long n, long m) {
        if (n <= 1)
            return 0 ;

        long previous = 0L;
        long current  = 1L;

        for (long i = 0; i < n - 1; ++i) {
            long tmp_previous = previous;
            previous = current;
            if(i != n-2){
                current = (tmp_previous + current) % m;
            }
            else{
                current = (tmp_previous + current -1) % m;
            }
        }

        return current;
    }
    
    
    public static void main(String[] args) {
        // 0 1 1 2 3 5  8  13  21  34 
        // 0 1 2 4 7 12 20 33  54  88
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        // long s = getFibonacciSumNaive(n);
        long s2 = getFibonacciSumFast(n);
        // System.out.println(s);
        System.out.println(s2);
    }
}

