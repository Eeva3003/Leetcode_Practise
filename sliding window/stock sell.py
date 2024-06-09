#sol1
l=0
        r=0
        maxp=0
        while r<len(prices):
            if prices[l]<prices[r]:
                maxp=max(maxp,prices[r]-prices[l])
            else:
                l=r
            r+=1    
        return maxp
#sol2
 i, j = 0, 0
        m = 0

        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            m = max(m, prices[j]-prices[i])
            j += 1

        return m
      

