//import java.math.BigInteger;
import java.util.*;
import java.io.*;

//char[] n = scan.next().toCharArray();

public class Training {
    private static int solve(int N, int P, Scanner in) {
        int[] stud = new int[N];
        for(int i = 0; i < N; i++){
            stud[i] = in.nextInt();
        }
        int minTop = N-1-(N-P);
        Arrays.sort(stud);
        int tot = Integer.MAX_VALUE;
        for (int s = minTop; s < N; s++) {
            int train = 0;
            int index = s-P+1;
            for (int t = index; t < s; t++){
                int dif = stud[s] - stud[t];
                train += dif;
            }
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