import java.util.*;

/*
the incredibly sexy answer by uwi on leetcode
*/

class Solution1 {
    public int[] numMovesStones(int a, int b, int c) {
        int[] d = {a, b, c};
        Arrays.sort(d);
        int max = d[2]-d[0]-2;
        int min = 2;
        if(d[2] - d[0] == 2){
            min = 0;
        }else{
            if(d[1] - d[0] <= 2 || d[2] - d[1] <= 2){
                min = 1;
            }
        }
        return new int[]{min, max};
    }
}	


/*
Original solution, could compress the 3 else ifs into one.

*/


class Solution {
    public int[] numMovesStones(int a, int b, int c) {
        int[] inp = new int[3];
        inp[0]= a;
        inp[1]= b;
        inp[2]= c;
        java.util.Arrays.sort(inp);
        
        int[] ans = new int[2];   
        ans[1] = 0;
        ans[0] = 0;
        
        if (inp[2] - inp[1] == 1 && inp[1] - inp[0] == 1){
            return ans;
        }
        else if (inp[2] - inp[1] == 1){
            ans[0] = 1;
            ans[1] = inp[1] - inp[0] - 1;
        }
        else if (inp[1] - inp[0] == 1){
            ans[0] = 1;
            ans[1] = inp[2] - inp[1] - 1;
        }
        else if(inp[2] - inp[1] == 2 || inp[1] - inp[0] == 2){
            ans[0] = 1; 
            ans[1] = (inp[2] - inp[1] - 1) + (inp[1] - inp[0] - 1);
        }
        
        else {
                ans[0] = 2; 
                ans[1] = (inp[2] - inp[1] - 1) + (inp[1] - inp[0] - 1);
        }
        
        return ans;
    }
}