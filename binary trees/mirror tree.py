def mirrorify(root, mirror):
 
    if (root == None) :
        mirror = None
        return mirror
     
    # Create new mirror node 
    # from original tree node
    mirror = createNode(root.val)
    mirror.right = mirrorify(root.left, 
                           ((mirror).right))
    mirror.left = mirrorify(root.right, 
                          ((mirror).left))
    return mirror
