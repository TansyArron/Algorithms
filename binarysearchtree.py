class Binary_Search_Tree():
	def __init__(self):
		self.root = ''
		self.node_to_children = {}


	def insert(self, item, root='', parent=None):
		if root is '':
			if self.root is '':
				self.root = item
				self.node_to_children[item] = [None, None, None]
				return
			else:
				root = self.root
		if root is None:	
			self.node_to_children[item] = [None, None, parent]
			if parent < item:
				self.update_parent(parent, item, 1)
			else:
				self.update_parent(parent, item, 0)
		elif root > item:
			self.insert(item, self.node_to_children[root][0], root)
		else:
			self.insert(item, self.node_to_children[root][1], root)


	def delete(self, item):
		left, right, parent = self.node_to_children[item]
		if left is None and right is None:
			self.node_to_children.pop(item, None)
			if item < parent:
				self.update_parent(parent, None, 0)
			else:
				self.update_parent(parent, None, 1)
		elif left is None:
			self.update_parent(parent, right, 1)
			self.node_to_children[right][2] = parent
			self.node_to_children.pop(item, None)
		else:
			self.update_parent(parent, left, 0)
			self.node_to_children[left][2] = parent
			self.node_to_children.pop(item, None)
		

	def find(self, item, root=''):
		if root is '':
			root = self.root
			print(root)
			self.find(item, root)
		elif root == item or root is None:
			print('found item or item not in tree')
			print(item, ':', self.node_to_children[root])
		elif root < item:
			root = self.node_to_children[root][1]
			self.find(item, root)
		else:
			print('root more than item')
			root = self.node_to_children[root][0]
			self.find(item, root)


	def update_parent(self, parent, replacement_child, leftrightindex):
		if parent is None:
			pass
		self.node_to_children[parent][leftrightindex] = replacement_child


BST = Binary_Search_Tree()

BST.insert(5)
BST.insert(3)
BST.insert(7)
BST.insert(4)
BST.insert(8)
BST.insert(2)
BST.insert(9)
BST.insert(1)
BST.insert(6)
BST.insert(10)
BST.find(7)
BST.delete(3)
BST.delete(6)

	
