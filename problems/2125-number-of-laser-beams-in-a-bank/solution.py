class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        # find the number of security devices, exclude empty floor
        dev = []
        for i in range (len(bank)):
            if bank[i].count("1") != 0 :
                dev.append((bank[i].count("1")))
        
        # calculate : between 2 floors : 
        # lasers = devices (floor1) * devices (floor2) 
        ans = 0
        for n in range(len(dev)-1):
            ans += ((dev[n]) * (dev[(n+1)]))

        return ans
