
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        frequency = {}
        result = []

        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            if frequency[num] >= len(result):
                result.append([])
            
            result[frequency[num]].append(num)
            frequency[num] += 1
        
        return result
