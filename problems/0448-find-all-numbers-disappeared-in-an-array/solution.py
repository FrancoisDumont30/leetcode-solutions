class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = len(nums)
        nums.sort()
        nums = set(nums)
        ans = []
        for i in range(1, x+1):
            if i not in nums:
                ans.append(i)

        return ans
