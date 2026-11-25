class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        ans = []
        for i in range(1, n+1):
            s.append(i)
            ans.append('Push')
        
            if i not in target :
                s.remove(i)
                ans.append('Pop')

            if s == target :
                break
        
        return ans
