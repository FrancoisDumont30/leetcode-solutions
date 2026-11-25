class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maxi = len(nums)
        for i in range(0, maxi-1) :
            for j in range(i+1, maxi):
                if nums[i] + nums[j] == target :
                    return [i, j]
