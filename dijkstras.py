from priority_queue import PriorityQueue
from test_data.graphs import ex_map


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