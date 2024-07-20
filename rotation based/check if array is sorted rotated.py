class Solution:
    def check(self, nums: List[int]) -> bool:
        f=0
        if nums[0]>=nums[len(nums)-1]:
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    f+=1
                    if f>1:
                        return False
        else:
            for i in range(len(nums)-1):
                 if nums[i]>nums[i+1]:
                    return False
        return True            


            
