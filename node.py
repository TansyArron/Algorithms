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

    def __repr__(self):
        return "<Node %s - %s>" % (self.value, [ neighbor for neighbor in self.neighbors ])