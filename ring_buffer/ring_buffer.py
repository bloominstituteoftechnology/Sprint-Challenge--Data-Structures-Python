from doubly_linked_list import DoublyLinkedList


class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()

	def append(self, item):
		if len(self.storage) < self.capacity:
			self.storage.append(item)
			self.current = len(self.storage) - 1
			return

		self.current += 1
		if self.current >= self.capacity:
			self.current = 0
		self.storage[self.current] = item

	def get(self):
		return list(self.storage)
		# # Note:  This is the only [] allowed
		# list_buffer_contents = []

		# # TODO: Your code here

		# return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = [None for _ in range(self.capacity)]

	def append(self, item):
		if None in self.storage:
			self.storage.remove(None)
			self.storage.append(item)
			self.current = len(self.storage) - 1
			return

		self.current += 1
		if self.current >= self.capacity:
			self.current = 0
		self.storage[self.current] = item

	def get(self):
		return [el for el in self.storage if el is not None]


class DictRingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = 0
		self.storage = {index: None for index in range(self.capacity)}

	def append(self, item):
		self.storage[self.current] = item
		self.current += 1
		if self.current >= self.capacity:
			self.current = 0

	def get(self):
		result = [None for _ in range(self.capacity)]
		for index, value in self.storage.items():
			result[index] = value
		return [el for el in result if el is not None]
