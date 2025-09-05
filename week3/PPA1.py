'''A doubly linked list is a linked data structure that consists of two header nodes 
that point to the first and last position in a sequence of linked records. 
Each node in the sequence contains three fields: One data field and two link fields 
(references to the previous and to the next node in the sequence of nodes) and. 
So, it can be traversed in both directions.
For the given class doubly_linked_list, create two methods:
insert_end(data): that accepts an integer data and inserts it into the list at the last position.
delete_end(): Delete one element of the list from the last position.
Note- Use given linked list structure to implementation. 
Write both operations (insert_end and delete_end) with O(1) time.'''

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
class doubly_linked_list:
  def __init__(self):
    self.head = None
    self.last = None

  def insert_end(self, data):
    """
    Inserts a new node with the given data at the end of the doubly linked list.
    Achieves O(1) time complexity by directly using the 'last' pointer.
    """
    new_node = Node(data)

    if self.last is None:  # Case 1: List is currently empty
      self.head = new_node
      self.last = new_node
    else:  # Case 2: List has one or more nodes
      self.last.next = new_node  # Link current last node to new_node
      new_node.prev = self.last  # Link new_node back to current last node
      self.last = new_node      # Update 'last' pointer to new_node

  def delete_end(self):
    """
    Deletes the element from the last position of the doubly linked list.
    Achieves O(1) time complexity by directly using the 'last' pointer.
    """
    if self.last is None:  # Case 1: List is empty, nothing to delete
      return

    if self.head == self.last:  # Case 2: Only one element in the list
      self.head = None
      self.last = None
    else:  # Case 3: More than one element in the list
      self.last = self.last.prev  # Move 'last' pointer to the second-to-last node
      # The old last node is now effectively orphaned and will be garbage collected.
      if self.last is not None: # Ensure self.last is not None before accessing .next
        self.last.next = None # Sever the link from the new last node to the old last node
      else: # This condition might occur if the list became empty after moving self.last, for safety
        self.head = None