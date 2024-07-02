class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        if not root:
            return True

        queue = deque([(root, 0)])  # Queue of tuples (node, level)
        leaf_level = -1

        while queue:
            node, level = queue.popleft()
        
            if not node.left and not node.right:  # If it's a leaf node
                if leaf_level == -1:
                    leaf_level = level  # Set the level of the first leaf
                elif leaf_level != level:
                    return False  # Return false if a leaf is not at the same level

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return True
        
