// time out

import java.math.BigInteger;
import java.util.Scanner;

public class p14928 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        BigInteger input = scan.nextBigInteger();

        System.out.println(input.mod(BigInteger.valueOf(20000303)));

        scan.close();
    }
}