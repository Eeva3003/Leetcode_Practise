#my method 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int: 
        hash1={}
        count=0
        for i in nums:
            if i not in hash1:
                hash1[i]=1
            else:
                hash1[i]+=1
              
        for i in nums:
            
            if k-i in hash1 and hash1[i]>0:
                
                hash1[i]-=1
                if hash1[k-i]>0:
                    
                    count+=1
                    hash1[k-i]-=1
        
        return count             
#better complexity
nums.sort()

        left = 0 
        right = len(nums) - 1
        operation = 0 

        while left < right:
            if ((nums[left] + nums[right]) == k):
                operation += 1
                left +=1 
                right -=1
            elif((nums[left] + nums[right]) < k):
                left += 1
            else:
                right -= 1
        return operation           

        

        
