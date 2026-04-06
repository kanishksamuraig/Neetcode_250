
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        
        char[] charsb=s.toCharArray();
        char[] charst=t.toCharArray();
        Arrays.sort(charsb);
        Arrays.sort(charst);
        for(int i=0;i<s.length();i++){
            if(charsb[i]!=charst[i]){
                return false;
            }
        }
        return true;
        
    }
}
