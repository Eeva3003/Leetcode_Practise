class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not postorder:
            return None

        # Dictionary to store the index of each value in inorder traversal
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def build(start, end):
            if start > end:
                return None
            # Last element in postorder is the root of current tree/subtree
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Split the tree into left and right subtrees using the inorder index
            idx = idx_map[root_val]
            
            # Build right subtree before left subtree
            root.right = build(idx + 1, end)
            root.left = build(start, idx - 1)

            return root

        return build(0, len(inorder) - 1)
