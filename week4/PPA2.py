'''Complete the Python function findAllPaths to find all possible paths from the source vertex to destination vertex in a directed graph.
Function findAllPaths (vertices, gList, source, destination) takes vertices as a list of vertices, 
glist a dictionary that is an adjacency List representation of graph edges, source vertex, 
destination vertex, and returns a list of all paths from source to destination. 
The return value will be a List of Lists, where every path is a sequence of vertices as a List. 
Return an empty list if no path exists from 'source' to 'destination'.'''

# Vertices are expected to be labelled as single letter or single digit 

# Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort()  
  return res

def findAllPaths(vertices, gList, source, destination):
    """
    Finds all possible paths from the source vertex to destination vertex in a directed graph.

    Args:
        vertices: A list of vertices.
        gList: A dictionary representing the adjacency list of the graph edges.
               (e.g., {'A': ['B', 'C'], 'B': ['D'], ...})
        source: The starting vertex.
        destination: The target vertex.

    Returns:
        A list of lists, where each inner list is a sequence of vertices representing a path
        from source to destination. Returns an empty list if no path exists.
    """
    all_paths = [] # To store all found paths
    
    # This helper function performs the DFS to find paths
    # current_path: stores the path from source to current_vertex
    # visited_on_path: a set to keep track of visited nodes IN THE CURRENT PATH
    #                  to prevent cycles within a single path.
    def dfs_find_paths(current_vertex, current_path, visited_on_path):
        # Add the current vertex to the path and mark as visited for this path
        current_path.append(current_vertex)
        visited_on_path.add(current_vertex)

        # Base Case: If we reached the destination, add a copy of the current path to all_paths
        if current_vertex == destination:
            all_paths.append(list(current_path))
        else:
            # Explore neighbors
            if current_vertex in gList: # Ensure the current_vertex has neighbors in the graph
                for neighbor in gList[current_vertex]:
                    if neighbor not in visited_on_path: # Avoid cycles within this path
                        dfs_find_paths(neighbor, current_path, visited_on_path)
        
        # Backtrack: Remove the current vertex from the path and unmark it.
        # This allows it to be part of other paths later.
        visited_on_path.remove(current_vertex)
        current_path.pop()

    # Start the DFS from the source vertex
    dfs_find_paths(source, [], set())
    
    return all_paths

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
  # Adjusted to handle potential empty input lines for adjacency lists
  # `input().split(" ")` might return `['']` for an empty line, need to filter it.
  neighbors_str = input().split(" ")
  Alist[i] = [item for item in neighbors_str if item != '']

source = input()
dest = input()

# Call the findAllPaths function
result_paths = findAllPaths(v, Alist, source, dest)

# Arrange and print the result as per the problem's requirement
print(ArrangeResult(result_paths))
#Vertices are expected to be labelled as single letter or single digit 

#Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
  Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))