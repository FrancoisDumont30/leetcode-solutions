class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(1, length+1) :
            if i in nums :
                nums.remove(i)
            elif i not in nums :
                missing = i
        
        twice = nums[0]
        
        return [twice, missing]
