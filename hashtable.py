class Node():
	def __init__(self, key):
		self.previous = None
		self.next = None


class Order():
	def __init__(self):
		self.start = None
		self.end = None


	def add(self, key):
		node = Node(key)
		if self.start == None:
			self.start = node
			self.end = node
			return node
		node.previous = self.end
		node.previous.next = node
		self.end = node
		return node


	def remove(self, node):
		if node.previous:
			node.previous.next = node.next
		if node.next:
			node.next.previous = node.previous
		if not node.next:
			self.end = node.previous


class Hashtable():
	def __init__ (self, length=8):
		self.num_keys = 0
		self.length = length
		self.table = [None] * self.length	
		self.order = Order()


	def add(self, key, hash_num=None):
		if hash_num == None:
			hash_num = abs(hash(key))
		index = hash_num % self.length
		while True:
			if self.table[index] is None or self.table[index] == 'removed item':
				order_info = self.order.add(key)
				self.table[index] = (key, hash_num, order_info)
				self.num_keys += 1
				if self.num_keys > self.length * .6:
					self.resize()
				return
			else:
				index = (index + 1) % self.length


	def remove(self, key):
		entry, index = self.find(key)
		self.order.remove(self.table[index][2])
		self.table[index] = 'removed item'
		self.num_keys -= 1
		print(self.table)
		pass


	def find(self, key):
		hash_num = abs(hash(key))
		index = hash_num % self.length
		while self.table[index] is not None:
			if self.table[index][0] == key:
				return self.table[index], index
			else:
				index = (index + 1) % self.length
		raise KeyError(key)


	def resize(self):
		new_table = Hashtable(self.length*2)
		for i in range(self.length):
			if self.table[i] is not None and self.table[i] != 'removed item':
				key, hash_num, order_info = self.table[i]
				new_table.add(key, hash_num)
		self.table = new_table.table
		return


	def iterate_in_order(self):
		current = self.order.start
		ordered_list = []
		while current != None:
			ordered_list.append(current.key)
			current = current.next
		return ordered_list

