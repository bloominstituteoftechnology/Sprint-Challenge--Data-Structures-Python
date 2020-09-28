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
        current = node
        prev = prev
        # print("---START--")
        # if current:  
        #     print(current.value)
        # else:
        #     print("CURRENT = none")
        # if prev:
        #     print(prev.value)
        # else:
        #     print("PREV = none")
        # if current.get_next():
        #     print(current.get_next().value)
        # else:
        #     print("GET NEXT = NONE")
        # print("---END--")

        if current == None and prev == None:
            print("OK")
            self.head = None
            self.next_node = None
            return
            

        if current.get_next() != None:
            # recursively reverse the linked list
            if current == self.head:
                # print("FIRST")
                # we need to not set the previous property
                # can possibly store the current property in a temporary property in
                # order to set it's next property to none
                temp = current.get_next()
                current.next_node = None
                # print("----")
                # print(current.next_node)
                return self.reverse_list(temp, current)

            # elif current.get_next == None:
            #     self.head = current
            #     self.head.next_node = prev

            else:
                print("----")
                temporary = current.get_next()
                current.next_node = prev

                return self.reverse_list(temporary, current)

        else:
            #when you reach the last node do something like set the head and previous properties
            if prev:
                self.head = current
                self.head.next_node = prev

            elif prev == None and current:
                self.head = current
                self.next_node = None





        # while current:
        #     if current.next_node != None:
        #         print()
        #         # set each nodes next property to its former previous while looping through
        #         print(current.value)

        #     current = current.next_node
            
        #     else:
        #         # here we will do something for the last node to make it the head
        #         # when we reach the end of the list we will set the last nodes next property
        #         # to it's previous and set it as the tail.
        #         print(current.value)