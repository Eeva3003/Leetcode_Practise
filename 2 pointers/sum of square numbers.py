#brute force approach
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        square=set()
        for i in range(int(sqrt(c))+1):
            square.add(i*i)
        a=0
        while a*a<=c:
            target=c-a*a
            if target in square:
                return True
            a+=1
        return False            
 #optimal solution
  left,right=0,int(sqrt(c))

        while left<=right:
            total=left*left+right*right
            if total<c:
                left+=1
            elif total > c:
                right-=1
            else:
                return True
