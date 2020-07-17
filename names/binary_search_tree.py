class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

    def insert(self, value):
        def search_tree(node):
            if value < node.value:
                if node.left is None:
                    node.left = BSTNode(value)
                    return True
                else:
                    return search_tree(node.left)
            else:
                if node.right is None:
                    node.right = BSTNode(value)
                    return True
                else:
                    return search_tree(node.right)
        return search_tree(self)

    def contains(self, target):
        current_node = self
        while current_node:
            if target == current_node.value:
                return True
            elif target < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False