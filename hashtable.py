

class Hashtable():
	def __init__ (self, length=8):
		self.num_keys = 0
		self.length = length
		self.table = [None] * self.length	


	def add(self, key, hash_num=None):
		if hash_num == None:
			hash_num = abs(hash(key))
		index = hash_num % self.length
		while True:
			if self.table[index] is None or self.table[index] == 'removed item':
				self.table[index] = (key, hash_num)
				print(self.table)
				self.num_keys += 1
				if self.num_keys > self.length * .6:
					print('RESIZE')
					self.resize()
				return
			else:
				print("collision at index {}".format(index))
				index = (index + 1) % self.length


	def remove(self, key):
		entry, index = self.find(key)
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
				key, hash_num = self.table[i]
				new_table.add(key, hash_num)
		self.length = new_table.length
		self.table = new_table.table
		return

table = Hashtable()
table.add('first')
table.add('second')
table.find('first')
table.remove('first')
table.add('third')
print(table.table)
table.add('fourth')
print(table.length)
table.add('fifth')
table.add('sixth')
table.add('seventh')
table.add('eighth')
table.add('ninth')
table.add('tenth')
print(table.table)
print(table.num_keys)
print(table.length)