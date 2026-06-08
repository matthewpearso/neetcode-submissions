class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        if (s == null || t == null){
            return false;
        }

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        
        for(int i = 0; i < s.length(); i++){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            if (!sMap.containsKey(sChar)){
                sMap.put(sChar, 1);
            }
            else{
                int sCurrentVal = sMap.get(sChar);
                sMap.put(sChar, sCurrentVal + 1);
            }
            if (!tMap.containsKey(tChar)){
                tMap.put(tChar, 1);
            }
            else{
                int tCurrentVal = tMap.get(tChar);
                tMap.put(tChar, tCurrentVal + 1);
            }
        }
        if (sMap.equals(tMap)){
            return true;
        }
        else{
            return false;
        }
    }
}
