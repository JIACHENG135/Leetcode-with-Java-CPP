class Solution {
    public boolean validPalindrome(String s) {
        int start = 0;
        int end = s.length()-1;
        while(start<=end){
            if(s.substring(start,start+1).equals(s.substring(end,end+1))){
                start += 1;
                end -= 1;
            }else{
                return(isTrue(s,start+1,end)||isTrue(s,start,end-1));
            }
        }
        return true;
    }
    public boolean isTrue(String s, Integer start, Integer end){
        while(start<=end){
            if(s.substring(start,start+1).equals(s.substring(end,end+1))){
                start += 1;
                end -= 1;
            }else{
                return false;
            }
        }
        return true;
    }
}