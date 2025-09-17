'''A taxi driver of an online cab service provider wants to go back to his home after 
dropping a customer. He wants to reduce the total cost (required for fuel, toll tax, etc.) 
to reach home by picking some customers. He checks the routes online. 
So, there are some routes available from his current location to his home location 
where he can earn money by picking some customers.
Write a function min_cost(route_map, source, destination) that accepts a weighted adjacency list 
route map for a directed and connected graph of n vertices (labeled from 0 to n-1) 
in the following format:-

Note- cost between two stops represents Expenditure (on fuel, toll tax, etc) 
Earning so it may be negative. Assume that no negative weight cycle exists in the graph.
You are also given two integers source representing the current location of the taxi driver 
and destination representing the home location of the taxi driver. 
The function should returns the minimum cost route in the format 
(minimum_cost, [source, next stop, next stop.... destination]) from source to destination.'''

import collections

def min_cost(route_map, source, destination):
    """
    Calculates the minimum cost and route for the taxi driver,
    handling potentially negative edge weights using Bellman-Ford algorithm.
    Assumes no negative weight cycles exist in the graph.

    Args:
        route_map (dict): A weighted adjacency list for a directed graph,
                          {source_index: [(destination_index, cost), ...]}.
                          Costs can be negative.
        source (int): The starting city index.
        destination (int): The home city index.

    Returns:
        tuple: (minimum_cost, [route_list])
               minimum_cost (int or str "inf"): The calculated minimum cost.
                                                   Returns "inf" if destination is unreachable.
               route_list (list): A list of city indices representing the path.
                                  Returns an empty list if destination is unreachable.
    """

    all_nodes = list(route_map.keys())
    num_vertices = len(all_nodes)

    distances = {node: float('inf') for node in all_nodes}
    predecessors = {node: None for node in all_nodes}

    if source not in distances:
        return ("inf", []) # Changed to "inf" string for consistency

    distances[source] = 0

    for _ in range(num_vertices - 1):
        relaxed_in_this_pass = False
        for u in all_nodes:
            if distances[u] == float('inf'):
                continue

            for v, weight in route_map.get(u, []):
                # Ensure v is in distances, initializing if not already there (e.g. for isolated nodes)
                if v not in distances:
                    distances[v] = float('inf')
                    predecessors[v] = None
                
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
                    relaxed_in_this_pass = True
        if not relaxed_in_this_pass:
            break

    final_cost_val = distances.get(destination, float('inf'))

    if final_cost_val == float('inf'):
        return ("inf", []) # Return "inf" as a string directly in the tuple

    # --- Reconstruct the path ---
    path = []
    current = destination
    while current is not None and current in predecessors:
        path.append(current)
        if current == source:
            break
        current = predecessors[current]
    
    # Handle specific cases for path reconstruction
    if source == destination:
        return (0, [source])

    if not path or path[-1] != source:
        return ("inf", []) # Return "inf" if path cannot be fully reconstructed to source

    return (int(final_cost_val), path[::-1]) # Ensure cost is int when returned in tuple

# --- GIVEN BOILERPLATE CODE (EXACTLY AS PROVIDED) ---
if __name__ == "__main__":
    size = int(input())
    edges = eval(input())
    s = int(input())
    d = int(input())
    WL = {}
    for i in range(size):
        WL[i] = []
    for ed in edges: #for create list for directed graph
        WL[ed[0]].append((ed[1],ed[2]))
    
    # This print statement will print the tuple returned by min_cost directly.
    print(min_cost(WL,s,d))

size = int(input())
edges = eval(input())
s = int(input())
d = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for directed graph
    WL[ed[0]].append((ed[1],ed[2]))
print(min_cost(WL,s,d))