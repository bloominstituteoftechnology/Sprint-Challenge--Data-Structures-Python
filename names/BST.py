class BSTNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insertValue(self, value):

		if value < self.value:

			if self.left:

				self.left.insertValue(value)

			else:

				self.left = BSTNode(value)

		else: 

			if self.right:

				self.right.insertValue(value)

			else:

				self.right = BSTNode(value)

	def containsTarget(self, target):

		if target == self.value:

			return True
		elif target < self.value and self.left:

			return self.left.containsTarget(target)

		elif target > self.value and self.right:

			return self.right.containsTarget(target)



