class Node():
	def __init__(self, value):
		self.value = value
		self.children = {}
		self.end = False


class WordIterator(object):
	def __init__(self, root):
		self.root = root
		self.stack = []
		self.stack.append((root, min(root.children), ''))
		

	def __iter__(self):
		return self


	def __next__(self):
		if not self.stack:
			raise StopIteration
		
		while True:
			parent_node, current_key, prefix = self.stack.pop()
			current_node = parent_node.children[current_key]
			if current_key < max(parent_node.children.keys()):
				next_child = self.get_next_child(parent_node, current_key)
				self.stack.append((parent_node, next_child, prefix))
			prefix = prefix + current_key
			if current_node.children:
				self.stack.append((current_node, min(current_node.children.keys()), prefix))
			if current_node.end:
				return prefix


	def get_next_child(self, parent, key):
		keys = sorted(parent.children.keys())
		key_index = keys.index(key)
		return keys[key_index + 1]
		

class Tree():
	def __init__(self):
		self.root = Node('')


	def insert(self, word):
		word = word.lower()
		current_node = self.root
		for letter in word:
			if not letter in current_node.children:
				current_node.children[letter] = Node(letter)
			current_node = current_node.children[letter]
		current_node.end = True


	def find(self, word):
		current_node = self.root
		for letter in word:
			if letter in current_node.children:
				current_node = current_node.children[letter]
			else:
				return False
		return True
		
	def __iter__(self):
		return WordIterator(self.root)

	def word_iterator(self, node=None, prefix=None):
		if node is None:
			node = self.root
		if prefix is None:
			prefix = ''
		
		stack = [(node, prefix)]
		print(stack)
		while stack:
			node, prefix = stack.pop()
			prefix += node.value
			for key in sorted(node.children.keys(), reverse=True):
				child = node.children[key]
				stack.append((child, prefix))
			if node.end:
				yield prefix

	def word_iterator_recursive(self, node=None, prefix=None):
		if node is None:
			node = self.root
		if prefix is None:
			prefix = ''
		prefix += node.value
		if node.end:
			yield prefix
		for key in sorted(node.children.keys()):
			yield from self.word_iterator_recursive(node.children[key], prefix)
				

dictionary = Tree()
with open('words.txt', 'r') as f:
	for line in f:
		dictionary.insert(line.strip())

for word in dictionary:
	print(word)