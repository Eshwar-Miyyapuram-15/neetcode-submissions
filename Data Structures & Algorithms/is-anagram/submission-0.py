class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            cS={}
            cT={}
            for ch in s:
                cS[ch]=cS.get(ch,0)+1
            for ch in t:
                cT[ch]=cT.get(ch,0)+1
            if cS==cT:
                return True
        return False
        