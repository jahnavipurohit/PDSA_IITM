'''Given an undirected graph G, write a Python function to compute the number of connected components. 
A set of nodes form a connected component in an undirected graph if there exists a path 
between every pair of nodes in this set.
Write a Python function findComponents_undirectedGraph (vertices, edges), 
that accepts a list of vertices and a list of tuples that represent edges, and 
returns the number of connected components in the graph formed by vertices and edges. 
Each tuple (i,j) in edges represents an edge between vertices i and j.
For a completely connected graph there is only one connected component, 
hence the function should return 1
For the below graph, G1, the number of connected components is 3. 
So the function should return 3.'''

from collections import deque

def findComponents_undirectedGraph(vertices, edges):
    """
    Computes the number of connected components in an undirected graph.

    Args:
        vertices: A list of vertices (e.g., [0, 1, 2, 3]).
        edges: A list of tuples representing edges (e.g., [(0, 1), (2, 3)]).

    Returns:
        The number of connected components in the graph.
    """
    # 1. Build the adjacency list representation of the graph
    adj_list = {v: [] for v in vertices}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u) # Since it's an undirected graph

    # 2. Keep track of visited vertices
    visited = {v: False for v in vertices}

    # 3. Counter for connected components
    num_components = 0

    # 4. Iterate through each vertex
    for vertex in vertices:
        if not visited[vertex]:
            # Found a new unvisited vertex, start a new component traversal
            num_components += 1
            
            # Perform BFS to find all nodes in this component
            queue = deque([vertex])
            visited[vertex] = True

            while queue:
                current_node = queue.popleft()
                for neighbor in adj_list[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    
    return num_components