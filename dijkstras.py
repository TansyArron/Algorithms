from math import floor

# Example map from Wikipedia Dijkstras algorithm.
# Node: [(node, distance)]

ex_map = {
	1: [(6, 14), (3, 9), (2, 7)],
	2: [(1, 7), (3, 10), (4, 15)],
	3: [(1, 9), (2, 10), (4, 11), (6, 2)],
	4: [(2, 15), (3, 11), (5, 6)],
	5: [(4, 6), (6, 9)],
	6: [(1, 14), (3, 2), (5, 9)],
}

class PriorityQueue():
	def __init__(self, distances):
		self.distances = distances
		self.nodes = []
		self.empty = True

	def add(self, node):
		self.nodes.append(node)
		self.empty = False
		node_index = len(self.nodes) - 1	
		self.move_up(node_index)

	def move_up(self, index):
		parent = self.get_parent(index)
		if not parent:
			pass
		elif self.distances[self.nodes[parent]] < self.distances[self.nodes[index]]:
			temp = self.nodes[parent]
			self.nodes[parent] = self.nodes[index]
			self.nodes[index] = temp
			self.move_up(parent)

	def move_down(self, index):
		children = self.get_children(index)
		if not children:
			pass
		else:
			for child in children:
				if self.distances[self.nodes[child]] < self.distances[self.nodes[index]]:
					temp = self.nodes[child]
					self.nodes[child] = self.nodes[index]
					self.nodes[index] = temp
					self.move_down(child)
					break

	
	def get_next(self):
		if len(self.nodes) < 2:
			self.empty = True
		distace_list = [self.distances[node] for node in self.nodes]
		next = self.nodes[0]
		self.nodes[0] = self.nodes.pop()
		self.move_down(0)
		return next

	def get_parent(self, index):
		parent = floor((index - 1) // 2)
		if parent >= 0:
			return parent
		else:
			return None

	def get_children(self, index):
		index_1 = index * 2 + 1
		index_2 = (index * 2 + 2)
		if index_2 < len(self.nodes):
			if self.distances[self.nodes[index_1]] < self.distances[self.nodes[index_2]]:
				return (index_1, index_2)
			else:
				return (index_2, index_1)
		elif index_1 < len(self.nodes):
			return (index_1, )
		else:
			return None


def dijkstras(initial_node, destination_node, edge_set_by_node):

	distances = {key: float('inf') for key in edge_set_by_node.keys()}
	distances[initial_node] = 0
	current_node = initial_node
	visited = set()
	to_visit = PriorityQueue(distances)
	to_visit.add(current_node)

	while not to_visit.empty and destination_node not in visited:
		neighbors = edge_set_by_node[current_node]
		current_distance = distances[current_node]
		for neighbor in neighbors:
			node = neighbor[0]
			new_distance = current_distance + neighbor[1]
			if node not in visited and distances[node] > new_distance:
				distances[node] = new_distance
				if node not in to_visit.nodes:
					to_visit.add(node)
		visited.add(current_node)
		current_node = to_visit.get_next()
	return distances[destination_node]


print(dijkstras(1, 6, ex_map))