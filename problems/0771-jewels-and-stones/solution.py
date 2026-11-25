class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        
        for item in jewels :
            ans += stones.count(item)
        return ans
