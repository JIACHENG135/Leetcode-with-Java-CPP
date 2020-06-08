class Solution {
    public boolean isPalindrome(int x) {
        char[] s = Integer.toString(x).toCharArray();
        for(int i=0;i<s.length;i++){
            if(s[i]!=s[s.length-1-i]){
                return false;
            }
        }
        return true;
    }
}