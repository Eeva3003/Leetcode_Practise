class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        sum=0    
        if root.left:
            if not root.left.left and not root.left.right:

                sum+=root.left.val
            else:
                sum+=self.sumOfLeftLeaves(root.left) 
        
        sum+=self.sumOfLeftLeaves(root.right) 

        return sum    
