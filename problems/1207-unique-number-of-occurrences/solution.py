class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tested = []
        occur = []

        for i in arr:  
            if i not in tested :
                occur.append(arr.count(i))
                tested.append(i)

        occur.sort()
        ans = True
        for i in range(len(occur)-1):
            for j in range(i+1,len(occur)):
                if occur[i] == occur[j]:
                    ans = False
                    return ans
                else :
                    ans == True
        return ans
