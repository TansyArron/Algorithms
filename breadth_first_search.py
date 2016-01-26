from graph import Graph, Node
from adjacency_list import adjacency_list


class ExtendedNode(Node):
  def __init__(self, value):
    super(ExtendedNode, self).__init__(value)
    self.distance = float('inf')
    self.parent = None


class ExtendedGraph(Graph):
  def create_node_by_value(self, value):
        if value in self.nodes.keys():
            return self.nodes[value]
        else:
            node = ExtendedNode(value)
            self.add_node(node)
            return node


def breadth_first_search(graph, start):
  ''' Update the distance of each node in the graph with the distance from
  the start node. Returns a list of all nodes connected to start node.
  '''
  discovered = set()
  queue = []
  queue.append(start)
  while queue:
    current = queue.pop(0)
    for neighbor in current.neighbors.values():
      if neighbor.distance == float('inf') and neighbor not in discovered:
        neighbor.distance = current.distance + 1
        neighbor.parent = current
        queue.append(neighbor)
    discovered.add(current)
  return discovered

graph = ExtendedGraph()
nodes = graph.from_adjacency_list(adjacency_list)


discovered = breadth_first_search(graph, nodes[1])

for node in discovered:
  print node.value