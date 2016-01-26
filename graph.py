from adjacency_list import adjacency_list
from connection_list import connection_list


class Node(object):
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, node):
        self.neighbors[node.value] = node

    def remove_neighbor(self, node):
        if node.value in self.neighbors.keys():
            del self.neighbors[node.value]

    def is_adjacent(self, node):
        return node in self.neighbors.values()

    # def get_node(self, key):


    def __repr__(self):
        return "<Node %s - %s>" % (self.value, [ neighbor for neighbor in self.neighbors ])



class Graph(object):
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.value] = node

    def remove_node(self, node):
        if node.value in self.nodes.keys():
            del self.nodes[node.value]

    def create_node_by_value(self, value):
        if value in self.nodes.keys():
            return self.nodes[value]
        else:
            node = Node(value)
            self.add_node(node)
            return node

    @classmethod
    def from_adjacency_list(cls, adjacency_list):
        self = cls()
        for node_index, neighbors in enumerate(adjacency_list):
            node = self.create_node_by_value(node_index)
            self.nodes[node_index] = node
            for neighbor_index in neighbors:
                neighbor = self.create_node_by_value(neighbor_index)
                node.add_neighbor(neighbor)
        return self.nodes

    @classmethod
    def from_connection_list(cls, connection_list):
        self = cls()
        for connection in connection_list:
            node = self.create_node_by_value(connection[0])
            neighbor = self.create_node_by_value(connection[1])
            node.add_neighbor(neighbor)
        return self

    def are_connected(self, from_node, to_node):
        pass

    def shortest_path(self, from_node, to_node):
        print(from_node.value)
        explored_nodes = [from_node.value]
        print('explored_nodes', explored_nodes)
        distances = dict.fromkeys(self.nodes.keys(), [float('inf')])
        distances[from_node.value] = 0
        print('distances', distances)
        def pick_next_neighbor():
            '''picks neighbor with lowest distance from beginning
            '''
            picked = float('inf')
            picked_key = None
            for key in distances.keys():
                if distances[key][0] < picked:
                    picked = distances[key][0]
                    picked_key = self.nodes[key]
                    print('picked_key',picked_key)
                else:
                    pass
            return picked_key

        while len(explored_nodes) < len(distances):
            for node in explored_nodes:
                for neighbor in self.nodes[node].neighbors.values():
                    print('neighbor:', neighbor)
                    print('neighbor.value:', neighbor.value)
                    print('distances[neighbor.value]:', distances[neighbor.value])
                    print('distances[neighbor.value][0]:', distances[neighbor.value][0])
                    print('SECOND HALF')
                    print('distances[node]',distances[node])
                    if distances[neighbor.value][0] < (distances[node] + 1):
                        pass
                    else:
                        distances[neighbor.value][0] = distances[node][0] + 1
            explored_nodes.append(pick_next_neighbor())
        return distances[to_node.value]
    def path(self, from_node, to_node):
        from_node.neighbors

    def __repr__(self):
        return repr(self.nodes)


# ag = Graph.from_adjacency_list(adjacency_list)

# print(ag.shortest_path(ag.nodes[1], ag.nodes[8]))
# cg = Graph.from_connection_list(connection_list)
