class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        
        dicts1 = dict()
        dicts2 = dict()
        
        for i in s:
            if i in dicts1.keys():
                dicts1[i] += 1
            else:
                dicts1[i] = 1
        for i in t:
            if i in dicts2.keys():
                dicts2[i] += 1
            else:
                dicts2[i] = 1
        
        if dicts1 == dicts2:
            return True
        return False