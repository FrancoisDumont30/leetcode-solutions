class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        result = False
        for i in range(len(arr)):
            if len(arr)>= 3 and (i<(len(arr)-2))and (arr[i]%2 != 0) and (arr[i+1]%2 != 0) and (arr[i+2]%2 != 0):
                result = True
            
            else :
                pass

        return result
