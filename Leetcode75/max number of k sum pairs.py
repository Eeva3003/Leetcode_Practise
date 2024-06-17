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

        
