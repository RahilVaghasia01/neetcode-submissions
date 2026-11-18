class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s) > len(t)):
            return False
        if(len(s) == 0) :
            return True
        prev_loc = t.find(s[0])
        for i in range(1,len(s)) :
            next_loc = t.find(s[i], prev_loc + 1)
            if next_loc == -1 or next_loc < prev_loc:
                return False
            else :
                prev_loc = next_loc
        return True 