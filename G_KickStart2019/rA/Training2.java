/*

This solution is the correct one. Instead of having to calculate the difference of
each individual item in the set from the maximum, the difference can be defined as 
(the max value * the number in the set) - (the sum of the set) and the sum of the set
can be calculated from the lowest possible set, and then incrementally changed by adding the new top
value and subtracting the dropped lowest value as you increment through each possible set.
This means you only have to have one loop instead of a nested loop that runs through each
member of the set, like in my original Training problem. 
*/

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