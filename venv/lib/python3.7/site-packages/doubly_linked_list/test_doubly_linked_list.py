import unittest

from doubly_linked_list import DoublyLinkedList

def list_move_to_head(l, i):
	l.insert(0, l.pop(i))
	
def alternate_insertion_type(dll, up_to, start_with_head=True):
	"This will insert items from 0 to up_to, alternating between"
	"inserting to the head and tail. If starts_with_head is true,"
	"the alternations will start with insertions to the head, "
	"else the tail."
	
	if start_with_head:
		type_one = dll.addToHead
		type_two = dll.addToTail
	else:
		type_one = dll.addToTail
		type_two = dll.addToHead
		
	for i in xrange(up_to):
		if i % 2 == 0:
			type_one(i)
		else:
			type_two(i)

class TestDoublyLinkedList(unittest.TestCase):

	def setUp(self):
		pass		
		
	def test_creation(self):
		l = DoublyLinkedList()
		self.assertIsInstance(l, DoublyLinkedList)
		self.assertIs(l.size, 0)
	
	def test_addToHead(self):
		l = DoublyLinkedList()
		for i in xrange(4):
			self.assertIs(l.size, i)
			l.addToHead(i)
			self.assertEqual(list(l), range(i, -1, -1))
			
	def test_addToTail(self):
		l = DoublyLinkedList()
		for i in xrange(4):
			self.assertIs(l.size, i)
			l.addToTail(i)
			self.assertEqual(list(l), range(0, i+1))
			
	def test_AddToHead_and_addToTail(self):
		l = DoublyLinkedList()
		sanity = []
		for i in xrange(8):
			if i % 2 == 0:
				l.addToHead(i)
				sanity = [i] + sanity
			else:
				l.addToTail(i)
				sanity.append(i)
			self.assertEqual(list(l), sanity)
		
		l = DoublyLinkedList()
		sanity = []
		for i in xrange(8):
			if i % 2 == 1:
				l.addToHead(i)
				sanity = [i] + sanity
			else:
				l.addToTail(i)
				sanity.append(i)
			self.assertEqual(list(l), sanity)
			
	def test_moveToHead(self):
		l = DoublyLinkedList()
		sanity = []
		for i in xrange(8):
			if i % 2 == 0:
				l.addToHead(i)
				sanity = [i] + sanity
			else:
				l.addToTail(i)
				sanity.append(i)
			self.assertEqual(list(l), sanity)
			
			original_dll = l.copy()
			original_sanity = sanity[::]
			for j in xrange(i):
				#Move each item to the head once
				l.moveToHead(l.getNodeByIndex(j))
				list_move_to_head(sanity, j)
				try:
					self.assertEqual(list(l), sanity)
				except:
					import code; code.interact(local=locals())
			l = original_dll
			sanity = original_sanity
		
		l = DoublyLinkedList()
		sanity = []
		for i in xrange(8):
			if i % 2 == 1:
				l.addToHead(i)
				sanity = [i] + sanity
			else:
				l.addToTail(i)
				sanity.append(i)
			self.assertEqual(list(l), sanity)
			
			original_dll = l.copy()
			original_sanity = sanity[::]
			for j in xrange(i):
				#Move each item to the head once
				l.moveToHead(l.getNodeByIndex(j))
				list_move_to_head(sanity, j)
				self.assertEqual(list(l), sanity)
			l = original_dll
			sanity = original_sanity
	
	def test_constructor(self):
		l = range(10)
		dll = DoublyLinkedList(l)
		self.assertEqual(l, dll)
	
	def test_copy(self):
		dll = DoublyLinkedList(range(10))
		dll2 = dll.copy()
		self.assertEqual(dll, dll2)
		self.assertTrue(dll is not dll2)
		
	def test_eq(self):
		dll = DoublyLinkedList(range(10))
		dll2 = DoublyLinkedList()
		for i in xrange(10-1):
			dll2.addToTail(i)
			self.assertFalse(dll == dll2)
		dll2.addToTail(i+1)
		self.assertTrue(dll == dll2)

	def test_getitem(self):
		dll = DoublyLinkedList(range(10))
		for i in xrange(len(dll)):
			self.assertEqual(i, dll[i])
			
	def test_removeTail(self):
		dll = DoublyLinkedList(range(10))
		sanity = range(10)
		for i in xrange(10):
			dll.removeTail()
			sanity.pop(-1)
			self.assertEqual(dll, sanity)
			
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestDoublyLinkedList)
	unittest.TextTestRunner(verbosity=2).run(suite)