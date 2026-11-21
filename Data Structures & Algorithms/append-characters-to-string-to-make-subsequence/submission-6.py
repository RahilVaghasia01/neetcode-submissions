class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp = 0
        tp = 0
        while sp < len(s) and tp < len(t) :
            idx = s.find(t[tp], sp)
            if idx != -1:
                sp = idx + 1
                tp += 1
            else:
                break
                
        return len(t) - tp