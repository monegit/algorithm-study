import java.math.BigInteger;
import java.util.Scanner;

public class p2338 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        BigInteger x = scan.nextBigInteger();
        BigInteger y = scan.nextBigInteger();

        System.out.println(x.add(y));
        System.out.println(x.subtract(y));
        System.out.println(x.multiply(y));

        scan.close();
    }
}