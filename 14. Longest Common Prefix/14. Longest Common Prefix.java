class Solution {
    public String longestCommonPrefix(String[] strs) {
        int minLength = Integer.MAX_VALUE;
        for(int i=0;i<strs.length;i++){
            minLength = Math.min(minLength,strs[i].length());
        }
        if(minLength==Integer.MAX_VALUE){
            return("");
        }
        String res="";
        for(int j=0;j<minLength;j++){
            String start = strs[0].substring(j,j+1);
            for(int i=1;i<strs.length;i++){
                if(!strs[i].substring(j,j+1).equals(start)){
                    return res;
                }
            }
            res += start;
        }
        return(res);
    }
}