class Node:
  def __init__(self):
    self.key = None
    self.value = None
    self.parent = None
    self.children = {}


class Trie:
  def __init__(self):
    self.root = Node()

  def put(self, key, value):
    currentNode = self.root
    currentWord = key 
    while len(currentWord) > 0:
      if currentWord[0] in currentNode.children:
        if len(currentWord) == 1:
          currentNode.children[currentWord[0]].value = value
        currentNode = currentNode.children[currentWord[0]]
        currentWord = currentWord[1:]
      else:
        nextNode = Node()
        nextNode.key = currentWord[0]
        nextNode.parent = currentNode
        if len(currentWord) == 1:
          nextNode.value = value
        currentNode.children[currentWord[0]] = nextNode
        currentNode = nextNode
        currentWord = currentWord[1:]

  def get(self, word):
    currentWord = word
    currentNode = self.root
    while len(currentWord) > 0:
      print(currentWord[0])
      if currentWord[0] in currentNode.children:
        currntNode = currentNode.children[currentWord[0]]
        currentWord = currentWord[1:]
      else:
        return "Not in trie"
    if currentNode.value == None:
      return "None"
    return currentNode.value

  def delete(self, word):
    currentWord = word
    currentNode = self.root
    while len(currentWord) > 1:
      if currentWord[0] in currentNode.children:
        currentNode = currentNode.children[currentWord[0]]
        currentWord = currentWord[1:]
      else:
        return None
    currentNode = currentNode.children[currentWord[0]]
    val = currentNode.value
    currentNode.value = None
    while currentNode.value == None and len(currentNode.children) == 0:
      parentNode = currentNode.parent
      parentNode.children[currentWord[0]] = None
      currentNode = parentNode
    return val
  
  def printAllNodes(self):
        nodes = [self.root]
        while len(nodes) > 0:
            for letter in nodes[0].children:
                if not nodes[0].children[letter] == None:
                  nodes.append(nodes[0].children[letter])
            print(nodes.pop(0).key)


def makeTrie(words):
    trie = Trie()
    for word, value in words.items():
        trie.put(word, value)
    return trie

trie = makeTrie({"emil": 10, "earrings": 4, "eat": 7, "she": 7, "sells": 8, "sea": 19, "shells": 12, "by": 3, "the": 5, "shore": 7})
print(trie.get("emil"))
print(trie.get("the"))
trie.printAllNodes()
