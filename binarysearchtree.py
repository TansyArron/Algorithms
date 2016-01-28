# IF RUNNING PYTHON 2.x CHANGE 

class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def has_children(self):
		if self.left or self.right:
			return True
		else:
			return False

class Iterator():
	def __init__(self, root):
		self.root = root
		self.stack = []
		self.chase_left(self.root)

	def __iter__(self):
		return self

	def __next__(self):
		if not self.stack:
			raise StopIteration
		current_node = self.stack.pop()
		if current_node.right:
			self.chase_left(current_node.right)
		return current_node

	def chase_left(self, node):
		while node.left:
			self.stack.append(node)
			node = node.left
		self.stack.append(node)


class Tree():

	def __init__(self):
		self.root = None

	def __iter__(self):
		return Iterator(self.root)

	def insert(self, value):
		if self.root is None:                      
			self.root = Node(value)
			return
		sub_tree = self.root
		while True:
			if value < sub_tree.value:
				if not sub_tree.left:
					sub_tree.left = Node(value)
					return
				else: 
					sub_tree = sub_tree.left
			if value > sub_tree.value:
				if not sub_tree.right:
					sub_tree.right = Node(value)
					return
				else:
					sub_tree = sub_tree.right

	def remove_root(self, node):
		# No children
		if not node.has_children():
			self.root = None
			return
		# One child
		elif node.left and not node.right:
			self.root = node.left
			return
		elif node.right and not node.left:
			self.root = node.right
			return
		# Two children and appropriate GrandChildren
		elif node.left.right:
			node.value = node.left.right.value
			return self.remove(node.left.right, node.left)
		elif node.right.left:
			node.value = node.right.left.value
			return self.remove(node.right.left, node.right)
		# Two children and no appropriate grandchildren
		else:
			node.value = node.left.value
			return self.remove(node.left, node)

	def remove(self, node, parent=None):
		# Check there is a tree
		if self.root is None:
			return
		# If no parent is provided, start at root
		if parent is None:
			parent = self.root
		# If the node to be removed is root, got to special case function.
		if node == self.root:
			return self.remove_root(node)

		sub_tree = parent
		while True:
			if sub_tree.value < node.value:
				if sub_tree.right == node:
					# if node has no children, remove pointer to node.
					if not node.has_children():
						sub_tree.right = None
						return

					# if node has only one child, sub_tree.right points to that child.

					elif node.left and not node.right:
						sub_tree.right = node.left
						return
					elif node.right and not node.left:
						sub_tree.right = node.right
						return

					# if node has a largest smallest grandchild or a smallest largest
					# grandchild, replace node.value with the value of the grandchild,
					# remove the grandchild.

					elif node.left.right:
						sub_tree.right.value = node.left.right.value
						return remove(node.left.right, node.left)
					elif node.right.left:
						sub_tree.right.value = node.right.left.value
						return remove(node.right.left)
					
					else:
						node.value = node.left.value
						remove(node.left, sub_tree)
				else:
					sub_tree = sub_tree.right
			else:
				# sub_tree.value > node.value:
				if sub_tree.left == node:
					# node has no children. Remove pointer
					if not node.has_children():
						sub_tree.left = None
						return

					# node has one child. sub_tree.left points to child.
					elif node.left and not node.right:
						sub_tree.left = node.left
						return
					elif node.right and not node.left:
						sub_tree.left = node.right
						return

					# node has two children.
					# node has a smallest, largest or largest, smallest grand child
					elif node.left.right:
						sub_tree.left.value = node.left.right.value
						return remove(node.left.right, node.left)
					elif node.right.left:
						sub_tree.left.value = node.right.left.value
						return remove(node.right.left, node.right)
					
					# node has two children but no appropriate grandchildren
					else:
						node.value = node.right.value
						remove(node.right, sub_tree)
				else:
					sub_tree = sub_tree.left

	def find(self, value):
		sub_tree = self.root
		while sub_tree.value != value:
			if value < sub_tree.value:
				if not sub_tree.left:
					print("{} is not in tree".format(value))
					return
				else:
					sub_tree = sub_tree.left
			elif value > sub_tree.value:
				if not sub_tree.right:
					print("{} is not in tree".format(value))
					return
				else:
					sub_tree = sub_tree.right
		return sub_tree


tree = Tree()
with open('./test_data/100.txt', 'r') as f:
	for line in f:
		print('inserting:',line)
		tree.insert(int(line.strip()))

for num in tree:
	print(num.value)
		


