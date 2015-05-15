class Node(object):
	def __init__(self):
		self.previous = None
		self.next = None


class Order(object):
	def __init__(self):
		self.start = None
		self.end = None


	def __iter__(self):
		current = self.start
		while current != None:
			yield current.key
			current = current.next


	def add(self):
		node = Node()
		if self.start == None:
			self.start = node
			self.end = node
			return node
		node.previous = self.end
		node.previous.next = node
		self.end = node
		return node


	def remove(self, node):
		if node.previous is None:
			self.start = node.next
		else:
			node.previous.next = node.next
		if node.next is None:
			self.end = node.previous
		else:
			node.next.previous = node.previous
		

class Hashtable(object):
	def __init__ (self, length=8):
		self.num_keys = 0
		self.length = length
		self.table = [None] * self.length	
		self.order = Order()
		self._tombstone = object()


	def add(self, key, hash_num=None):
		if hash_num == None:
			hash_num = abs(hash(key))
		index = hash_num % self.length
		try:
			self.find(key)
			return
		except KeyError as e:
			pass

		while True:
			if self.table[index] is None or self.table[index] == 'removed item':

				order_info = self.order.add()
				self.table[index] = (key, hash_num, order_info)
				self.num_keys += 1
				if self.num_keys > self.length * .6:
					self.resize()
				return
			else:
				index = (index + 1) % self.length


	def remove(self, key):
		entry, index = self.find(key)
		self.order.remove(entry[2])
		self.table[index] = 'removed item'
		self.num_keys -= 1


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
		self.length = new_table.length


	def iterate_in_order(self):
		current = self.order.start
		while current != None:
			yield current.key
			current = current.next

if __name__ == '__main__':
	table = Hashtable()
	table.add('first')
	assert table.order.start == table.order.end, 'Order start or end is wrong'
	table.add('second')
	# table.remove('first')
	table.find('first')
	table.add('third')
	table.add('fourth')
	table.add('fifth')
	table.add('sixth')
	table.add('seventh')
	assert table.length == 16, 'Failed to resize correctly. size is {}'.format(table.length)

