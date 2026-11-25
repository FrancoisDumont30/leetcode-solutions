class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        happy_child = 0
        verif= 0
        g.sort()
        s.sort()
        while verif < len(s) and happy_child < len(g):
            if s[verif] >= g[happy_child] :
                happy_child += 1
                verif += 1
            else :
                verif += 1  
        
        return happy_child
