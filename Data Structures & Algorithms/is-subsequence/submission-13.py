class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        scount = 0
        for tele in t :
            if s[scount] == tele :
                scount += 1
                if scount == len(s) :
                    break 
        if scount == len(s) :
            return True
        else :
            return False