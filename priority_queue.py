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
    parent = (index - 1) // 2
    if parent >= 0:
      return parent
    else:
      return None

  def get_children(self, index):
    index_1 = index * 2 + 1
    index_2 = index * 2 + 2
    if index_2 < len(self.nodes):
      if self.distances[self.nodes[index_1]] < self.distances[self.nodes[index_2]]:
        return (index_1, index_2)
      else:
        return (index_2, index_1)
    elif index_1 < len(self.nodes):
      return (index_1, )
    else:
      return None