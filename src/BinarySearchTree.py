class Node:
  def __init__(self):
    self.key = None
    self.value = None 
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None
    self.size = 0

  def insert(self, key, value):
    if self.root == None:
      n = Node()
      n.key = key
      n.value = value
      self.root = n
      self.size += 1
    else:
      self.insert_recursive(self.root, key, value, False, None)
      
  def insert_recursive(self, root, key, value, left, parent):
    if root == None:
      n = Node()
      n.key = key
      n.value = value
      root = n
      if left:
        parent.left = root
      else:
        parent.right = root
      self.size += 1
    if key < root.key:
      self.insert_recursive(root.left, key, value, True, root)
    elif key > root.key:
      self.insert_recursive(root.right, key, value, False, root)
    else:
      root.value = value

  def search(self, key):
    if self.size == 0:
      return "Empty Tree"
    return self.search_recursive(self.root, key)

  def search_recursive(self, node, key):
    if node == None:
      return "Search Miss"
    # print(node.key)
    if key < node.key:
      return self.search_recursive(node.left, key)
    elif key > node.key:
      return self.search_recursive(node.right, key)
    else:
      return node.value

tree = BST()
tree.insert("Emil", 1)
tree.insert("Soleymani", 3)
tree.insert("Natalia", 2)
tree.insert("Ghazarian", 4)
tree.insert("Ghazarian", 5)
print(tree.search("Soleymani"))
print(tree.search("Natalia"))
print(tree.search("Ghazarian"))
print(tree.search("Daron"))
