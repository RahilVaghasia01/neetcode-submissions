class Solution {
    public void reverseString(char[] s) {
        int startP = 0;
        int endP = s.length - 1;
        while (startP < endP) {
            char temp = s[startP];
            s[startP] = s[endP];
            s[endP] = temp;
            startP++;
            endP--;
        }
    }
}