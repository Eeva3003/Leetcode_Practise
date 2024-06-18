class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxz=0
        cnt=0
        l=0
        for r in range(len(nums)):
            cnt+=1 
            if nums[r]==0:
                maxz+=1
                if maxz>k:
                    cnt-=1
                    
