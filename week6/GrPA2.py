'''Write a Python function maxLessThan(root, K), that accepts the root node of the binary search tree 
and a number K and returns the maximum number less than or equal to K in the tree. 
If K is the less than every number in the tree return None . Each node in the tree 
is an object of class Tree , and the tree will have at least one node.'''

class Tree:
  #constructor
  def __init__(self, initval=None):
    self.value = initval
    if self.value:
      self.left = Tree()
      self.right = Tree()
    else:
      self.left = self.right = None
    return
  
  #Only empty node has value None
  def isempty(self):
    return(self.value == None)
  
  #Leaf nodes have both children empty
  def isleaf(self):
    return(self.value != None and self.left.isempty() and self.right.isempty())
  
#insert element to BST
def insertToBST(root, x):
  # Tree should have atleast one element.
  temp = root
  while (not temp.isempty()):
    if (x < temp.value):
      temp = temp.left
    else:
      temp = temp.right

  temp.value = x
  temp.left = Tree()
  temp.right = Tree()
def insertToBST(root, x):
    # Tree should have atleast one element.
    temp = root
    while (not temp.isempty()):
        if (x < temp.value):
            temp = temp.left
        else:
            temp = temp.right

    temp.value = x
    temp.left = Tree()
    temp.right = Tree()

# Not a member of the class Tree.
def maxLessThan(root, K):
    """
    Finds the maximum number in a Binary Search Tree (BST) that is less than or equal to K.

    Args:
        root: The root node of the BST (an object of class Tree).
        K: The number to compare against.

    Returns:
        The maximum number less than or equal to K, or None if no such number exists.
    """
    
    result = None
    current_node = root

    while not current_node.isempty(): # Continue as long as the current node is not empty
        if current_node.value == K:
            return current_node.value
        elif current_node.value < K:
            # This value is a candidate. Try to find a larger one in the right subtree.
            result = current_node.value
            current_node = current_node.right
        else: # current_node.value > K
            # This value is too large. Look in the left subtree for a smaller candidate.
            current_node = current_node.left
            
    return result
L = [int(item) for item in input().split(" ")]
x = int(input())
root = Tree(L[0])
for item in L[1:]:
  insertToBST(root, item)

print(maxLessThan(root, x))