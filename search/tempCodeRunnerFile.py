queue = [self]
    # visited is our cb function

    while queue:
        node = queue.pop(0)
        if node.value:
            cb(node.value)
            if node.right is not None:
                if node.left is not None:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    queue.append(node.right)