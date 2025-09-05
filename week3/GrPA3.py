'''Complete the below function reverse(root) that will reverse the linked list 
with the first node passed as an argument, and return the first node of the reversed list. 
Each node in the linked list is an object of class Node. Class Node members are described below.

Class Node:

• value - stored value.
• next - points to next node.
• isEmpty() - returns True if linked list is empty, False otherwise.
Note- The list is to be reversed only by changing next pointer of existing nodes. 
No values to be changed and no new nodes to be created.'''

def reverse(root):
  if (root.isEmpty()):
    return root
  temp = root
  prev = None
  while (temp):
    next, temp.next = temp.next, prev
    prev, temp = temp, next
  return prev