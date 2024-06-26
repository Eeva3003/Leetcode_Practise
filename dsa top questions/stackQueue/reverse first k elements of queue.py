class Solution:
    def modifyQueue(self, q, k):
        if k <= 0 or k > len(q):
            return q  # Return the queue unchanged if k is out of bounds or invalid
        
        stack = []
        
        # Dequeue the first k elements and push them onto a stack
        for _ in range(k):
            stack.append(q.popleft())
        
        # Enqueue elements from the stack back into the queue to reverse their order
        while stack:
            q.append(stack.pop())
        for _ in range(len(q) - k):
            q.append(q.popleft())
        return q
