'''Consider a system of n water tanks on a hill, connected via m pipes. 
Water can flow through these pipes only in one direction. We have a source of water 
that can be connected to only one of these water tanks. We need to find if there exists 
a master tank such that all the tanks in this group can be filled by connecting the 
water source to this master tank. The tanks are numbered from 1 to n.
Write a Python function findMasterTank (tanks, pipes) that accepts arguments tanks 
which is a list of tanks, and pipes which is a list of tuples that represents connectivity 
through pipes, between tanks. Each tuple (i,j) in pipes represents a pipe such that, 
water can flow from tank i to tank j but not vice versa. Your function should find 
a master tank and return the number representing it, else should return 0 if no master tank 
exists in the system. If there are more than one master tanks return any one of them. 
Try to implement an algorithm that executes in linear time (O(n+m)).
For e.g. In the graph GT below representing pipe connectivity between 4 water tanks, 
tank 1 is the only master tank. For this your function should return 1.'''

from collections import deque
class myStack:
  def __init__(self):
    self.stack = deque()
  
  def pop(self):
    return self.stack.pop()
  
  def push(self, x):
    return self.stack.append(x)

  def isEmpty(self):
    return False if self.stack else True

# Run depth first search starting from vertex t and mark all nodes that are visited.
def runDFSForTankT(tanks, GList, t, visited):
  s = myStack()
  s.push(t)
  visited[t] = True

  while not s.isEmpty():
    i = s.pop()
    for p in GList[i]:
      if not visited[p]:
        s.push(p)
        visited[p] = True;

# Brute force approach is to do a DFS for all vertices and check if all other vertices can be reached.
# Time complexity for this approach will be O(n(n+m)). 
# Below function finds the master tank in O(n+m) time complexity. Here v is number of vertices and e is number of edges.
def findMasterTank(tanks, pipes):
  # Create an adjacency list for graph representing the system of pipes and tanks.
  GList = {}
  for i in tanks:
    GList[i]=[]
  for (i,j) in pipes:
    GList[i].append(j)

  # Mark every tank not visited.
  visited = {t:False for t in tanks}
  
  lastVisited = tanks[0] 
  # Traverse the tanks through depth first search method and keep track of last visited tank.
  for t in tanks:
    if not visited[t]:
      runDFSForTankT(tanks, GList, t, visited)
      lastVisited = t

  # Check if this last visited tank has paths to all other tanks in the system by doing another depth first search.
  visited = {t:False for t in tanks}
  runDFSForTankT(tanks, GList, lastVisited, visited)

  # Check visited to verify if all tanks are visited.
  for v in visited:
    if not visited[v]:
      return 0
  return lastVisited

  # Although we are calling DFS multiple times in a loop, the visited marking is common between all these calls. This ensures that we will traverse tanks only once, hence running the solution in linear time.



v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))