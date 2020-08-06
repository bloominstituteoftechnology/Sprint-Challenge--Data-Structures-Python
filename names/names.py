import time

from collections import Counter
start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


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

    def __repr__(self):
        crrnt = self.head
        while crrnt:
            f'{crrnt}'
            crrnt = crrnt.get_next()

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

# # ************************************************************************
# # 11.15 seconds ==> 64 duplicates
# # 2 linked lists

# ll1= LinkedList()
# ll2= LinkedList()


# for name in names_1:
#     ll1.add_to_head(name)

# for name in names_2:
#     ll2.add_to_head(name)

# def commonNodes(hd1,hd2):
#     c1=ll1.head
#     c2=ll2.head
#     count=0


#     while c1:
#         while c2:
#             if c1.value==c2.value:
#                 global duplicates
#                 count+=1
#                 duplicates.append(c1.value)


#             c2=c2.next_node
#         c1=c1.next_node
#         c2=ll2.head

#     # return (f'dups {duplicates},count {count}')

#     # return print(f'c1=>{c1.value} || c2=>{c2.value}')

# commonNodes(ll1,ll2)
# # ************************************************************************#
# ************************************************************************
# ************************************************************************
# referenced this solution
# https://www.geeksforgeeks.org/find-the-common-nodes-in-two-singly-linked-list/
# 0.0339 seconds ==> 64 duplicates
# 2 linked lists & 1 set

ll1= LinkedList()
ll2= LinkedList()

for name in names_1:
    ll1.add_to_head(name)

for name in names_2:
    ll2.add_to_head(name)

def commonNodesSet(hd1,hd2):
    c1=ll1.head
    c2=ll2.head
    count=0
    map_=set()


    while c1:
        map_.add(c1.value)
        c1=c1.next_node
    while c2:

        if c2.value in map_:

            global duplicates
            count+=1
            duplicates.append(c2.value)


        c2=c2.next_node


    return (f'dups {duplicates},count {count}')

    # return print(f'c1=>{c1.value} || c2=>{c2.value}')

print(commonNodesSet(ll1,ll2))
# ************************************************************************#
# ************************************************************************

# print(f'c1=>{ll1.head.value}')
# duplicates= [duplicates.append(name) for name in names_2 if ll1.contains(name) ]

# for name in names_2:
#     if ll1.contains(name):
#         duplicates.append(name)
# duplicates.append('tucker')
# ************************************************************************************************   |    |
# *****************************************************************************************fastest   \,/  \,/

# create a set() from names_1
# create a linkedlist from names_2
# if names_2 is in names_1set add to list duplicates

# .0265secs => 64 duplicates

# list1set = set()
# for name in names_1:
#     list1set.add(name)

# list2 = LinkedList()
# for name in names_2:
#     list2.add_to_head(name)
# crrnt = list2.head
# while crrnt:
#     if crrnt.value in list1set:
#         print(crrnt.value)
#         duplicates.append(crrnt.value)
#     crrnt = crrnt.next_node


# *****************************************************************************************fastest ^^^  ^^^


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
## this is O(n**2)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# ******************** |    |  ***************************************************************************
# *******************  \,/  \,/ ***************************************************************************

# add the lists together
# use the count
# if count =2+ append to the list

# 7.8929s==> 247  duplicates? negative

# names_3=names_1 +(names_2)

# for name in names_3:
#     if names_3.count(name)>1:
#         duplicates.append(name)


# add the lists together
# use the collections.Counter()
# if count =2+ append to the list

# 0.014 secs => 123 duplicates

# names_3=(names_1 +names_2)
# n3count = Counter(names_3)
# for name in n3count:
#     if n3count[name]>1:
#         duplicates.append(name)

# *********************        /`\   /`\   ************************************************************************
# *********************         |     |    ************************************************************************
# names3=[name for name in names_3 if names_3.count(name)>1)]

# # option2
# # convert to 2 sets
# use set.interaction creates  new set of the duplicates
# 0.00899 secs
# 64 duplicates...

# set_1=set(names_1)
# set_2=set(names_2)
# duplicates= set_1.intersection(set_2)


# ************************************************************************
# ************************************************************************
# #option3 use the collections.Counter() builtin tool

# .032000secs => .01799 secs  ===> 123 duplicates

# from collections import Counter


# names_3=(names_1 +names_2)

# dup=Counter(names_3)

# for d in dup:
#     if dup[d] > 1:
#         duplicates.append(d)


# ************************************************************************
# ************************************************************************




# Structure of a linked list node
# class Node:
#     def __init__(self):
#         self.data = 0
#         self.next = None

# Function to common nodes which have
# # same value node(s) both list
# set1=set()
# set1=[set1.add(listItem) for listItem in names_1]
# set1=[set1.add(listItem) for listItem in names_1]


# ************************************************************************
# referenced this solution
# https://www.geeksforgeeks.org/find-the-common-nodes-in-two-singly-linked-list/
# 31seconds 🙅🏻‍♀️👎🏻 ==> 64 duplicates
# 2 linked lists

# ll1 = LinkedList()
# ll2 = LinkedList()

# for name in names_1:
#     ll1.add_to_head(name)

# for name in names_2:
#     ll2.add_to_head(name)


# def commonNodesSet(ll1, ll2):
#     c2 = ll2.head
#     count = 0

#     while c2:

#         if ll1.contains( c2.value):

#             global duplicates
#             count += 1
#             duplicates.append(c2.value)

#         c2 = c2.next_node

# commonNodesSet(ll1,ll2)

# def countCommonNodes(head1, head2):

#     # List A
#     current1 = head1

#     # List B
#     current2 = head2

#     # Set count = 0
#     count = 0

#     # Create unordered_set
#     map_=set()

#     # Traverse list A till the end of list
#     while (current1 != None) :

#         # Add list data in map_
#         map_.add(current1.data)

#         # Increase current pointer of list A
#         current1 = current1.next

#     while (current2 != None) :

#         # Traverse list B till the end of list
#         # if data match then increase count
#         if ((current2.data) in map_):
#             count = count + 1

#         # Increase current pointer of list B
#         current2 = current2.next

#     # Return count
#     return count

# # Utility function to add a node at the beginning
# def push(head_ref,new_data):
#     new_node = Node()
#     new_node.data = new_data
#     new_node.next = head_ref
#     head_ref = new_node
#     return head_ref

# # Utility function to print a linked list
# def printList(head):
#     while (head != None) :
#         print(head.data, end = " ")
#         head = head.next

# # Driver program to test above functions
# head1 = None
# head2 = None

# # Create following linked list
# # List A = 3 . 4 . 12 . 10 . 17
# head1 = push(head1, 17)
# head1 = push(head1, 10)
# head1 = push(head1, 12)
# head1 = push(head1, 4)
# head1 = push(head1, 3)

# # List B = 10 . 4 . 8 . 575 . 34 . 12
# head2 = push(head2, 12)
# head2 = push(head2, 34)
# head2 = push(head2, 575)
# head2 = push(head2, 8)
# head2 = push(head2, 4)
# head2 = push(head2, 10)

# # Print list A
# print("Given Linked List A: ")
# printList(head1)

# # Print list B
# print( "\nGiven Linked List B: ")
# printList(head2)

# # Call function for count common node
# count = countCommonNodes(head1, head2)

# # Print number of common node in both list
# print("\nNumber of common node in both list is = " , count)

# # # This code is contributed by Arnab Kundu
# # Output:
# # Given Linked List A:
# # 3 4 12 10 17
# # Given Linked List B:
# # 10 4 8 575 34 12
# # Number of common node in both list is = 3
# Time Complexity: O(N)
# Space Complexity: O(N)

















end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")