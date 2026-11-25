class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ele1 = nums[:n]
        ele2 = nums[n:]
        ans = []
        for i in range(n) :
            ans.append(ele1[i])
            ans.append(ele2[i])

        return ans
