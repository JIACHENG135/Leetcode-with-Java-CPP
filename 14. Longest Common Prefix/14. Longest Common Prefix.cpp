class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0) return "";
        int minLength = INT_MAX;
        string res = "";
        for(int i=0;i<strs.size();i++){
            if(minLength>strs[i].length()) minLength = strs[i].length();
        }
        for(int i=0;i<minLength;i++){
            char start = strs[0][i];
            for(int j=0;j<strs.size();j++){
                if(strs[j][i]!=start){
                    // cout << strs[i][j] << start;
                    return res;
                }
            }
            res += start;
        }
        return res;
    }
};