class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res=[]

        q=collections.deque()
        q.append(root)

        while q:
            level=[]
            l=len(q)
            for i in range(l):
                v=q.popleft()
                if v:
                    level.append(v.val)
                    q.append(v.left)
                    q.append(v.right)

            if level:
                res.append(level)
        return res        
        
