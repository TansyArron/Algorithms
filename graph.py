from node import Node


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

    def __repr__(self):
        return repr(self.nodes)

