import java.lang.reflect.Array;
class Solution {
    public void moveZeroes(int[] nums) {
        int ind = 0;
        int ct = 0;
        for(Integer i:nums){
            if(i==0){
                // ct += 1;
                ind += 1;
                continue;
            }else{
                int prev = nums[ind];
                nums[ind] = nums[ct];
                nums[ct] = prev;
                ind += 1;
                ct += 1;
            }
        }
    }
}