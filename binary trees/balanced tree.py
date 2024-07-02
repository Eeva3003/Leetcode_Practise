def check_balanced_and_height(node):
            if not node:
                return 0  # An empty tree is balanced and has height 0

            left_height = check_balanced_and_height(node.left)
            if left_height == -1:  # Not balanced
                return -1

            right_height = check_balanced_and_height(node.right)
            if right_height == -1:  # Not balanced
                return -1

            if abs(left_height - right_height) > 1:
                return -1  # Not balanced

            return 1 + max(left_height, right_height)

        return check_balanced_and_height(root) != -1
