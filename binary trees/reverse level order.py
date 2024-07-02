def reverseLevelOrder(root):
    
    if root is None:
        return []

    q = deque()
    stack = []
    q.append(root)

    while q:
        node = q.popleft()
        stack.append(node)

        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)

    result = deque()
    while stack:
        node = stack.pop()
        result.append(node.data)

    return result
