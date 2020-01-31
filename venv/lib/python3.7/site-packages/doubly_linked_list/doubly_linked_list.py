class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
		
class DoublyLinkedList(object):
	def __init__(self, iterable=None):
		self.head = None
		self.tail = None
		self.size = 0
		
		if iterable is not None:
			for i in iterable:
				self.addToTail(i)
				
	def addToTail(self, data):
		node = Node(data)
		if self.tail is None:
			self.head = node
			self.tail = node
			node.next = None
			node.prev = None
		else:
			self.tail.next = node
			node.prev = self.tail
			node.next = None
			self.tail = node
		self.size += 1
	def addToHead(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
			node.next = None
			node.prev = None
		else:
			self.head.prev = node
			node.next = self.head
			node.prev = None
			self.head = node
		self.size += 1
	def removeTail(self):
		if self.tail is None:
			return
		temp = self.tail
		if self.tail.prev is not None:
			self.tail = self.tail.prev
			self.tail.next = None
		else:
			self.head = None
			self.tail = None
		del temp
		self.size -= 1
		
	def moveToHead(self, node):
		"""
		Move some node that's already in the list to the head. The method 
		assumes the node is in the list - no check is made. Proper use is in
		the user's hands. The head and everything between the item being 
		moved to the head gets shifted one to the right.
		"""
		if self.head is node:
			return
			
		if self.tail is node:
			#We know node.prev isn't None since node isn't the head
			self.tail = node.prev
		else:
			node.next.prev = node.prev
			
		node.prev.next = node.next
		
			
		self.head.prev = node
		node.next = self.head
		node.prev = None
		self.head = node
	
	def copy(self, other_attrs_to_copy=[]):
		"Make a new linked list whose nodes contain the same data."
		"Assumes attributes being copied from nodes are immutible."
		cur = self.head
		new_dll = DoublyLinkedList()
		while cur is not None:
			new_dll.addToTail(cur.data)
			for attr in other_attrs_to_copy:
				a = getattr(cur, attr)
				setattr(new_dll.tail, attr, a)
			cur = cur.next
		return new_dll
	
	def __iter__(self):
		cur = self.head
		while cur is not None:
			yield cur.data
			cur = cur.next
	
	def __len__(self):
		return self.size
		
	def __eq__(self, other):
		if len(self) != len(other):
			return False
		for a, b in zip(self, other):
			if a != b:
				return False
		return True
	
	def __ne__(self, other):
		return not self.__eq__(other)
		
	def __getitem__(self, index):
		if index >= len(self):
			raise IndexError("There are only %s items in this list. The index of the item "
							 "you asked for is %s " % (self.size, index))
		cur = self.head
		i = 0
		while cur is not None:
			if i == index:
				return cur.data
			cur = cur.next
			i += 1
		raise IndexError("There are only %s items in this list. The index of the item "
						 "you asked for is %s " % (self.size, index))
	
	def getNodeByIndex(self, index):
		cur = self.head
		i = 0
		while cur is not None:
			if i == index:
				return cur
			cur = cur.next
			i += 1
		raise IndexError("There are only %s items in this list. The index of the item "
						 "you asked for is %s " % (self.size, index))
	
	def __setitem__(self, index, val):
		self.getNodeByIndex(index).data = val
				
	def __repr__(self):
		return str(list(self))
	
	def display(self):
		temp = self.head
		i = 0
		while temp is not None:
			print '*'*80
			print 'i:', i
			print 'temp', temp
			print 'data:', temp.data
			print 'prev:', temp.prev
			print 'next', temp.next
			temp = temp.next
			i += 1