class Solution {
public:
    bool validPalindrome(string s) {
        int left=0,right = s.length()-1;
        while(left<=right){
            if(s[left]!=s[right]) return(isTrue(s,left+1,right)||isTrue(s,left,right-1));
            left++;
            right--;
        }
        return true;
    }
    bool isTrue(string s,int left, int right){
        while(left<=right){
            if(s[left]!=s[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};