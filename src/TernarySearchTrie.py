class Node:
  def __init__(self):
    self.value= None
    self.key = None
    self.left = None
    self.right = None
    self.middle = None


class TST:
  def __init__(self):
    self.root = Node()
    self.size = 0

  def size(self):
    return self.size

  def isEmpty(self):
    return (self.size == 0)

  def get(self, key):
    currentWord = key
    currentNode = self.root
    while len(currentWord) > 0:
      if currentWord[0] < currentNode.key:
        if currentNode.left == None:
          return "Not in TST"
        currentNode = currentNode.left
      elif currentWord[0] > currentNode.key:
        if currentNode.right == None:
          return "Not in TST"
        currentNode = currentNode.right
      elif currentWord[0] == currentNode.key:
        if currentNode.middle == None:
          return "Not in TST"
        currentNode = currentNode.middle
        if len(currentWord) == 1:
           return currentNode.value
        currentWord = currentWord[1:]
  
  def put(self, key, value):
    currentWord = key
    currentNode = self.root
    if(currentNode.key == None):
      currentNode.key = currentWord[0]
      nextNode = Node()
      if len(key) > 0:
        nextNode.key = currentWord[1]
      currentNode.middle = nextNode
      currentNode = nextNode
      currentWord = currentWord[1:]
    while len(currentWord) > 0:
      if currentWord[0] < currentNode.key:
        if currentNode.left == None:
          nextNode = Node()
          nextNode.key = currentWord[0]
          currentNode.left = nextNode
          currentNode = nextNode
        else:
          currentNode = currentNode.left
      elif currentWord[0] > currentNode.key:
        if currentNode.right == None:
          nextNode = Node()
          nextNode.key = currentWord[0]
          currentNode.right = nextNode
          currentNode = nextNode
        else:
          currentNode = currentNode.right
      else:
        if currentNode.middle == None:
          nextNode = Node()
          nextNode.key = currentWord[0]
          currentNode.middle = nextNode
          currentNode = nextNode
          if len(currentWord) == 1:
            currentNode.value = value
          currentWord = currentWord[1:]
        else:
          currentNode = currentNode.middle
          if len(currentWord) == 1:
            currentNode.value = value
          currentWord = currentWord[1:]


def makeTST(words):
    tst = TST()
    for word, value in words.items():
        tst.put(word, value)
    return tst

tst = makeTST({"Emil": 10, "Soleymani": 12})
tst.put("Natalie", 12)
tst.put("Natalie", 13)
print(tst.get("Soleymani"))
print(tst.get("Natalie"))
