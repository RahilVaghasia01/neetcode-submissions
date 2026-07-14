class Solution {
public:
    int appendCharacters(string s, string t) {
        int sp = 0; 
        int tp = 0; 
        int lens = s.size();
        int lent = t.size();
        
        while (sp < lens && tp < lent) {
            if (s[sp] == t[tp]) {
                tp++;
            }
            sp++;
        }
        return lent - tp;
    }
};
