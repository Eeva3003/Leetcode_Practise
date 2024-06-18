class Solution:
    def removeStars(self, s: str) -> str:
        list1=[]
        for i in s:
            if i!="*":
                list1.append(i)
            else:
                list1.pop()
        return "".join(list1)            
        
