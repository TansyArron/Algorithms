from graph import Graph
from adjacency_list import adjacency_list

def depth_first_search(graph, start):
  ''' Given a graph and a start node in the graph, return all nodes
  reachable from the start node. 
  '''
  stack = []
  discovered = set()
  stack.append(start)
  while len(stack) > 0:
    current = stack.pop()
    discovered.add(current)
    for neighbor in current.neighbors.values():
      if neighbor not in discovered:
        stack.append(neighbor)
  return discovered

graph = Graph()
nodes = graph.from_adjacency_list(adjacency_list)


discovered = depth_first_search(graph, nodes[1])

for node in discovered:
  print node.value