class Solution {
    public int romanToInt(String s) {
        HashMap<String,Integer> t = new HashMap<String,Integer>();
        HashMap<String,String> m = new HashMap<String,String>();
        t.put("I",1);
        t.put("V",5);
        t.put("X",10);
        t.put("L",50);
        t.put("C",100);
        t.put("D",500);
        t.put("M",1000);
        m.put("IV",";4;");
        m.put("IX",";9;");
        m.put("XC",";90;");
        m.put("XL",";40;");
        m.put("CD",";400;");
        m.put("CM",";900;");
        int res = 0;
        for(Map.Entry<String,String> e: m.entrySet()){
            s = s.replace(e.getKey(),";"+e.getValue()+";");
        }
        String[] sp = s.split(";");
        for(String ms:sp){
            if(ms.length()!=0){
                try{
                    res += Integer.parseInt(ms);
                }catch(NumberFormatException e){
                    for(int i=0;i<ms.length();i++){
                        res += t.get(ms.substring(i,i+1));
                    }
                }
            }
        }
        return res;
    }
}