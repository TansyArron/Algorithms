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

def dijkstras(initial_node, destination_node, map_dict, nodes=False, unvisited=False):
	# Assign to every node a tentative distance value. 0 for the starting node
	# and infinity for all others. 
	if not nodes:
		nodes = {key: float('inf') for key in map_dict.keys()}
		nodes[initial_node] = 0
	# Create a set of all unvisited nodes
	if not unvisited:
		unvisited = set(key for key in map_dict.keys())
	
	# Set the initial node as current
	current_node = initial_node
	
	# For the current node, consider all it's unvisited neighbors and calculate their 
	# tentative distances. Compare the tentative distance to the current assigned value
	# and assign the smaller one.
	neighbors = map_dict[current_node]
	print(neighbors)
	current_distance = nodes[current_node]
	for neighbor in neighbors:
		node = neighbor[0]
		new_distance = neighbor[1]
		if node in unvisited and nodes[node] > new_distance + current_distance:
			nodes[node] = new_distance + current_distance 

	# When all neighbors have been considered, mark the current node as visited and remove it 
	# from the set of unvisited nodes.
	unvisited.remove(current_node)
	# If the destination node has been marked visited, or if the smallest tentative distance 
	# among nodes in the unvisited set is infinity(they have no connection to the rest of the graph) 
	# Stop.
	if destination_node not in unvisited:
		return nodes[destination_node]
	# Select the unvisited node that is marked with the  smallest tentative distance and set it 
	# as the new current node.
	unvisited_distances = {node: nodes[node] for node in unvisited}
	min_distance = min(unvisited_distances.values())
	if min_distance != float('inf'):
		current_node = [key for key in unvisited_distances.keys() if unvisited_distances[key] == min_distance][0]
		return dijkstras(current_node, destination_node, map_dict, nodes, unvisited)

print(dijkstras(1, 6, ex_map))