import java.util.*;

public class FibonacciPartialSum {

    private static long getFibonacciLastDigitFastSimple(long n, long m) {

        long pisanoPeriodLength = 60L;
    
        long index = (n % pisanoPeriodLength);

        n = index;
        if (n < 1){
            return 0 ;
        }
        if (n ==1){
            return 1  ;
        }

        long previous = 0L;
        long current  = 1L;

        for (long i = 0; i < n - 1; ++i) {
            long tmp_previous = previous;
            previous = current;

            current = (tmp_previous + current) %10 ;
        }
        return current;
    }
    private static long getFibonacciSumFast(long n) {
        if( n <=0L){
            return 0L;
        }
        if (n == 1L)
            return 1L;
        
        n += 2;

        return getFibonacciHuge(n,10);
    }

    private static long getFibonacciHuge(long n, long m) {

        long pisanoPeriodLength = 60L;
    
        long index = (n % pisanoPeriodLength);

        return getFibonacciLastDigitFast(index, m);
    }

    private static long getFibonacciLastDigitFast(long n, long m) {
        if (n <= 1)
            return 0 ;

        long previous = 0L;
        long current  = 1L;

        for (long i = 0; i < n - 1; ++i) {
            long tmp_previous = previous;
            previous = current;
            if(i != n-2){
                current = (tmp_previous + current) % 10  ;
            }
            else{
                current = (tmp_previous + current -1)  % 10;
            }
        }

        return current;
    }

    

    private static long getFibonacciPartialSumFast(long from, long to){
        if(from == to){
            return  getFibonacciLastDigitFastSimple(to, 10) % 10;
        }
        if (from == 0){
            return getFibonacciSumFast(to);
        }
        long modSumFrom = getFibonacciSumFast(from-1);
        long modSumTo = getFibonacciSumFast(to);
        // System.out.println(modSumFrom);
        // System.out.println(modSumTo);
        long result = modSumTo - modSumFrom ;
        if(result < 0){
            result = 10 + result;
        }
        return result;
        
        
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long from = scanner.nextLong();
        long to = scanner.nextLong();
        System.out.println(getFibonacciPartialSumFast(from, to));
    }
}



