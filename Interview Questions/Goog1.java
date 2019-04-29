/*abstract
For any positive integer, write a method that returns what the number would be if every number containing one or more '7' digits was skipped while counting.

So our new counting system is: 1 2 3 4 5 6 8 9 10 11 12 13 14 15 16 18 19...

7 would map to 8, 8 would map to 9, 16 would map to 18, etc.

*/

import java.io.*;
import java.util.*;

public class convertNum {

    // private static int convert(int N) {
    	
    //     String n = Integer.toString(N, 9);
    //     String newN = "";
        
    //     for (int i = 0; i < n.length(); i++){
    //         switch (n.charAt(i)){
    //             case('7'): newN = newN + "8";
    //                 break;
    //             case('8'): newN = newN + "9";
    //                 break;
    //             default: newN = newN + n.charAt(i);
    //         }
    //     }

    //     return Integer.valueOf(newN);

    // }

    public int convert(int n) {
        StringBuilder sb = new StringBuilder();
        while (n != 0) {
            int digit = n % 9;
            if (digit >= 7) digit++;
            sb.append(digit);
            n /= 9;
        }
        return Integer.parseInt(sb.reverse().toString());
    }

    public static void main(String[] args){
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        
        while (in.hasNextInt()) {
        	System.out.print(convert(in.nextInt()) + " ");
        }

        in.close();
    }
}
