"""
Testing file.
"""

import unittest
from reverse import LinkedList

class LinkedListTests(unittest.TestCase):
    """
    Tests for singly-linked list class, focusing on reversal.
    """
    def setUp(self):
        self.list = LinkedList()

    def test_add_to_head(self):
        """
        Test list insertion.
        """
        self.list.add_to_head(1)
        self.assertEqual(self.list.head.value, 1)
        self.list.add_to_head(2)
        self.assertEqual(self.list.head.value, 2)

    def test_contains(self):
        """
        Test list's built-in search function.
        """
        self.list.add_to_head(1)
        self.list.add_to_head(2)
        self.list.add_to_head(10)
        self.assertTrue(self.list.contains(2))
        self.assertTrue(self.list.contains(10))
        self.assertFalse(self.list.contains(1000))

    def test_empty_reverse(self):
        """
        Reversing an empty list should produce no effect.
        """
        self.list.reverse_list(self.list.head, None)
        self.assertEqual(self.list.head, None)

    def test_single_reverse(self):
        """
        Reversing a one-node list should leave it unchanged.
        """
        self.list.add_to_head(1)
        self.list.reverse_list(self.list.head, None)
        self.assertEqual(self.list.head.value, 1)

    def test_double_reverse(self):
        """
        Tests the reversal of a two-item list.
        """
        self.list.add_to_head(1)
        self.list.add_to_head(2)
        self.list.reverse_list(self.list.head, None)
        self.assertEqual(self.list.head.value, 1)
        self.assertEqual(self.list.head.get_next().value, 2)

    def test_longer_reverse(self):
        """
        Tests the reversal of a longer list.
        """
        cap = 50
        for i in range(cap):
            self.list.add_to_head(i)
        temp = self.list.head
        for i in reversed(range(cap)):
            self.assertEqual(temp.value, i)
            temp = temp.get_next()
        self.list.reverse_list(self.list.head, None)
        temp = self.list.head
        for i in range(cap):
            self.assertEqual(temp.value, i)
            temp = temp.get_next()

if __name__ == '__main__':
    unittest.main()
