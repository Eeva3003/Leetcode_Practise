class Solution:
    def toSumTree(self, root) :
        if root is None:
            return 0

        # Recursively convert left and right subtrees
        left_sum = self.toSumTree(root.left)
        right_sum = self.toSumTree(root.right)

        # Save the current node value
        old_value = root.data

        # Update the node value to be the sum of left and right subtrees
        root.data = left_sum + right_sum

        # Return the sum of values under this subtree including the old value
        return root.data + old_value
