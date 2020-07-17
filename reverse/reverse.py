from pudb import set_trace as st


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return
        next_node = node.get_next()
        if next_node is not None:
            self.reverse_list(next_node, node)
        else:
            self.head = node
        node.set_next(prev)

    def print_list(self):
        current_node = self.head
        while True:
            print(f"{current_node.value} -> ", end="")
            if current_node.get_next() is None:
                print("None")
                break
            current_node = current_node.get_next()

            


if __name__ == "__main__":
    aa = LinkedList()
    aa.add_to_head(1)
    aa.add_to_head(2)
    aa.add_to_head(3)
    aa.add_to_head(4)
    aa.add_to_head(5)
    aa.print_list()
    aa.reverse_list(aa.head, None)
    # aa.reverse_list(aa.head.get_next(), aa.head)
    aa.print_list()