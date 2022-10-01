// Solution 1. A less optimal naive implementation that shows steps
// Time: o(n)
// Memory: o(n)^2

class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        
        HashMap<String, Integer> countS = new HashMap<String, Integer>();
        HashMap<String, Integer> countT = new HashMap<String, Integer>();
        
        for(int i=0; i<s.length(); i++) {
            // Get character at position i
            char char2 = s.charAt(i);
            // Convert char to string
            String c2 = String.valueOf(char2);
            // Java 8 Merge Method
            countS.merge(c2, 1, Integer::sum);  
        }
        
        for(int j=0; j<t.length(); j++) {
            // Get character at position j
            char char3 = t.charAt(j);
            // Convert char to string
            String c3 = String.valueOf(char3);
            // Java 8 Merge Method
            countT.merge(c3, 1, Integer::sum);  
        }
        
    return(countS.equals(countT));
        
    }
}