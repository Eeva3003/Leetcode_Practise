class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxz=0
        cnt=0
        res=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                maxz+=1
            if maxz>k:
                if nums[l]==0:
                    maxz-=1
                l+=1
            cnt=r-l+1        
            
            res=max(res,cnt)    
        return res    
                        



            
        
