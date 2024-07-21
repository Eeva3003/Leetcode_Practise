class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return x
        first,last=1,x
        while first<=last:
            mid=first+(last-firts)//2
            if mid==x//mid:
                return mid
            elif mid>x//mid:
                last=mid-1
            else:
                first=mid+1               
        
        return last 
        
