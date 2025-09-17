'''Consider a social network of friends/relatives, most of whom are closely connected. 
Visualize this as a graph where each vertex denotes a person, and if two people know 
each other there is an edge between the vertices denoting them. If persons x and y know 
each other directly, then there is an edge connecting x and y and level of connectivity 
between them is 1. If person x is a friend of person y and person y is friend of person z,
but x is not a friend of z, then the level of connectivity between x and z is 2, and so on. 
The connectivity between people is always two way, i.e. if x directly knows y, 
then y also knows x directly.
Complete the Python function findConnectionLevel(n, Gmat, Px, Py) that takes 4 arguments, 

number of persons n (n persons numbered from 0 to n-1), Gmat an adjacency matrix representation 
of n persons and their connections(if Gmat[x][y] = 1, then person x and y are directly connected), 
two persons Px and Py both numbers, and returns the minimum level of connectivity between Px and Py. 
Return 0 if Px and Py are not connected through anybody in the group.
For example, for the graph below representing 7 persons from 0 to 6 and their connectivity.'''


from collections import deque
class myQueue:
  def __init__(self):
    self.Q = deque()
  
  def deQueue(self):
    return self.Q.popleft()

  def enQueue(self, x):
    return self.Q.append(x)

  def isEmpty(self):
    return False if self.Q else True

def findConnectionLevel(n, Gmat, Px, Py):
  q = myQueue() 
  visited = [False for i in range(n)]
  q.enQueue(Px)
  q.enQueue(-1) #using -1 in queue to distinguish between levels in BFS.
  visited[Px]=True
  level=1;

  while not q.isEmpty():
    v = q.deQueue()
    if (v == -1):
      level+=1
      if (not q.isEmpty()):
        q.enQueue(-1)
      continue
    for i in range(n):
      if(i==Py and Gmat[v][i] == 1):
        return level
      if(Gmat[v][i] and (not visited[i])):
        q.enQueue(i)
        visited[i]=True

  return 0
vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))