package rAjava;

import java.util.*;
import java.io.*;

//char[] n = scan.next().toCharArray();

public class Training2 {
	
    private static int solve(int N, int P, Scanner in) {
    	
        int[] stud = new int[N];
        for(int i = 0; i < N; i++){
            stud[i] = in.nextInt();
        }
        
        
        Arrays.sort(stud);
        
        int sum = 0;
        
        for (int i = 0; i < P; i++) {
        	sum+= stud[i];
        }
        
        int tot = (stud[P-1] * P)- sum;
        
        for (int s = P; s < N; s++) {
            int train = stud[s] * P;
            
            sum -= stud[s-P];
            sum += stud[s];
            
            train-= sum;
            
            if (train < tot){
                tot = train;
            }
        }
        return tot;
			

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int T = in.nextInt(); // Scanner has functions to read ints, longs, strings, chars, etc.
        for (int i = 1; i <= T; ++i) {
            int N = in.nextInt();
            int P = in.nextInt();
            int tot = solve(N, P, in);

          System.out.println("Case #" + i + ": " + tot);
        }
      
    }
    
}