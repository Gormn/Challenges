package rAjava;

import java.io.*;
import java.util.*;

public class convertNum {


    public static int convert(int n) {
        StringBuilder sb = new StringBuilder();
        while (n != 0) {
            int digit = n % 9;
            if (digit >= 7) digit++;
            System.out.println(digit);
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

