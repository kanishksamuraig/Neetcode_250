
class Solution {
    int count(String s,char c){
        int count=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)==c){
                count++;
            }
        }
        return count;
    }
    public boolean isAnagram(String s, String t) {
        
        if(s.length()!=t.length()){
            return false;
        }
        for(int i=0;i<s.length();i++){
            if(count(s,s.charAt(i))!=count(t,s.charAt(i))){
                return false;
            }
        }
        return true;
        /*
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
       */
     
    
    }
}
