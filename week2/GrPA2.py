'''Complete the python function find Largest(L) below, 
which accepts a list L of unique numbers, that are sorted(ascending) and rotated n times, 
where n is unknown, and returns the largest number in list L. 
Rotating list [2, 4, 5, 7, 8] one time gives us list [8, 2, 4, 5, 7], and 
rotating the second time gives list [7, 8, 2, 4, 5] and so on. Try to give an O(log n) solution. 
Hint: One of the O(log n) solutions can be implemented using binary search and 
using 'first or last' element to know, the direction of searching further.
# input<L>: List L sorted and rotated.
# out: Return the largest number in list L.
def findLargest (L):
# Your code goes here
Sample input:
7, 8, 2, 4, 5
Sample output:
8'''

def findLargest(L):
  left = 0
  s = len(L)
  right = s-1
  
  # If list has only one element, that is the max.
  if (s==1):
    return L[0]
    
  while (left<=right):
    mid=(left+right)//2
    
    # if mid is at last index, next element to compare will be at index 0
    if (mid == s-1):
      nextToMid = 0
    else:
      nextToMid = mid+1

    if (L[mid] > L[nextToMid]):
      return L[mid]
    elif (L[mid] < L[0]):
      # our element is in left of mid
      right = mid-1
    else:
      # our element is in right of mid
      left = mid+1