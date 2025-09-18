'''A country's defense organization wants to setup a private fiber network to connect all its 
camps around the country which will be disconnected from the INTERNET(world wide web). 
It wants to excluding only one camp, which will be connected to the INTERNET. 
Camps that can be connected to each other via fiber and the associated cable cost to 
connect them is given as an adjacency list representation Alist for all n camp of the company
in the format below.
1 ['camp_1': [(camp_a, cost_1_a), (camp_b, cost_1_b]
2
'camp_2': [(camp_c, cost_2_c), (camp_d, cost_2_d)
3
4
5.
6 'camp_n']: [(camp_x, cost_2_x), (camp_y, cost_2_y)...}
In the above Alist, camp_1 can be connected to camp_a with a cable cost of cost_1_a units 
and to camp_b with cable cost as cost_1_b units, and so on for all the n camps. 
The cable cost two connect any two cities will always be positive.
Write a Python function connectCamps(Alist, exCamp) that accepts the Alist as described above 
and a camp exCamp, returns the minimum cost required to connect all the camps excluding the excamp. 
If the camps cannot be connected after excluding excamp return -1. 
The function will be called to check for the cost excluding each camp one by one so try to make it 
efficient that runs in O((m+n) logn), where m is the number of pairs of camps that can be connected.'''

import heapq

def connectCamps(Alist, ExCamp):
    """
    Calculates the minimum cost to connect all camps excluding a specific ExCamp.

    Args:
        Alist: An adjacency list representation of camps and their connection costs.
               Format: {'camp_name': [(neighbor_camp, cost), ...]}
        ExCamp: The name of the camp to be excluded from the private network.

    Returns:
        The minimum cost required to connect all other camps, or -1 if they cannot
        be connected into a single component.
    """

    all_camps = set(Alist.keys())
    
    # Filter out ExCamp from the set of camps to be connected
    camps_to_connect = all_camps - {ExCamp}

    # If there are 0 or 1 camps to connect, the cost is 0 (already connected)
    if len(camps_to_connect) <= 1:
        return 0
    
    # Initialize variables for Prim's algorithm
    min_cost = 0
    visited = set()
    
    # Priority queue stores (cost, camp_name) tuples, ordered by cost
    pq = []

    # Find a starting camp that is not ExCamp
    start_camp = None
    for camp in camps_to_connect:
        start_camp = camp
        break
    
    if start_camp is None: # Should not happen if len(camps_to_connect) > 1, but for safety
        return 0

    # Start Prim's algorithm from the chosen start_camp
    # Add start_camp to visited and add all its valid edges to the priority queue
    visited.add(start_camp)
    if start_camp in Alist:
        for neighbor, cost in Alist[start_camp]:
            if neighbor != ExCamp: # Don't consider edges to the excluded camp
                heapq.heappush(pq, (cost, neighbor))

    # Prim's algorithm loop
    while pq and len(visited) < len(camps_to_connect):
        cost, current_camp = heapq.heappop(pq)

        # If the camp has already been visited, skip it
        if current_camp in visited:
            continue

        # Add the current camp to visited and accumulate cost
        visited.add(current_camp)
        min_cost += cost

        # Add all valid neighbors of the current_camp to the priority queue
        if current_camp in Alist: # Ensure current_camp has entries in Alist
            for neighbor, edge_cost in Alist[current_camp]:
                if neighbor != ExCamp and neighbor not in visited:
                    heapq.heappush(pq, (edge_cost, neighbor))

    # Check if all camps (excluding ExCamp) were connected
    if len(visited) == len(camps_to_connect):
        return min_cost
    else:
        # Not all required camps could be connected (disconnected graph)
        return -1