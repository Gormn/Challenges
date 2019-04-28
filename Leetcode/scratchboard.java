import java.util.*;

class Solution {
    public int removeDuplicates(int[] nums) {
        int tot = nums.length;
        
        for (int i = 1; i < nums.length; i++){
            if (nums[i] == 2147483647){
                tot += 1;
            }
            
            if (nums[i] == nums[i-1]){
                nums[i -1 ] = 2147483647;
                tot -=1;
            }
        }
        java.util.Arrays.sort(nums);
        
        return tot;
    }
}