'''A courier company XYZ provides courier service between n cities labeled 0 to n-1, 
where customers can send items from any city to any another city. The company follows 
the shortest path to deliver items and charges 5 Rs. per kilometer distance. 
The company wants to develop an inquiry system where customers can get the information 
on the cost and route for their courier.
Write a class XYZ_Courier that accepts a weighted adjacency list Route map for an undirected 
and connected graph at the time of object creation in following format:-

The class has following methods:-
cost (source, destination) that accepts source name and destination name and 
returns minimum cost for delivery.
route(source, destination) that accepts source name and destination name and 
returns the shortest route for delivery in the following format:
[source, placel, place2,....
destination]'''

import collections
import heapq

class XYZ_Courier:
    def __init__(self, route_map_dict):
        """
        Constructor for XYZ_Courier.
        Accepts a pre-built weighted adjacency list (WL) dictionary.

        Args:
            route_map_dict (dict): A dictionary representing the undirected graph.
                                   Format: {source_node: [(dest_node, distance), ...]}
        """
        self._graph = route_map_dict  # The provided WL is already the complete undirected graph
        self.cost_per_km = 5

    def _dijkstra(self, start_node, end_node=None):
        """
        Performs Dijkstra's algorithm to find shortest paths.

        Args:
            start_node (int): The starting node for the pathfinding.
            end_node (int, optional): If specified, Dijkstra's will stop once this node is reached.

        Returns:
            tuple: (distances_map, predecessors_map)
                   distances_map (dict): {node: min_distance_from_start}
                   predecessors_map (dict): {node: previous_node_in_shortest_path}
        """
        # Ensure all nodes mentioned in the graph are included in initial distances/predecessors maps
        # This covers nodes that might only appear as destinations or isolated nodes from the size 'n' input.
        all_nodes = set(self._graph.keys())
        for node_list in self._graph.values():
            for neighbor, _ in node_list:
                all_nodes.add(neighbor)

        distances = {node: float('inf') for node in all_nodes}
        predecessors = {node: None for node in all_nodes}

        # Handle the start_node's initial distance
        if start_node in distances:
            distances[start_node] = 0
        else:
            # If start_node itself is not in the graph (e.g., beyond N or completely isolated),
            # it will remain at inf and won't be processed. This implicitly means it's unreachable.
            pass

        # Priority queue: (distance, node)
        priority_queue = [(0, start_node)] if start_node in distances else [] # Add only if start_node is valid

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If we've already found a shorter path to this node, skip
            if current_distance > distances[current_node]:
                continue

            # Optimization: If we're looking for a specific end_node and have reached it
            if end_node is not None and current_node == end_node:
                break

            for neighbor, weight in self._graph.get(current_node, []): # Use .get to handle nodes with no outgoing edges
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, predecessors

    def cost(self, source, destination):
        """
        Calculates the minimum cost for delivery between source and destination.

        Args:
            source (int): The index of the source city.
            destination (int): The index of the destination city.

        Returns:
            int or str: The minimum delivery cost (integer), or "inf" if unreachable.
        """
        # Collect all unique nodes to correctly check if source/destination exist in the graph
        all_nodes = set(self._graph.keys())
        for node_list in self._graph.values():
            for neighbor, _ in node_list:
                all_nodes.add(neighbor)

        # Handle cases where source or destination nodes might not exist in the graph (e.g., invalid indices)
        if source not in all_nodes or destination not in all_nodes:
            return "inf" # Return string "inf" as per expected output for unreachable/invalid nodes

        distances, _ = self._dijkstra(source, destination)
        min_distance = distances.get(destination, float('inf'))

        if min_distance == float('inf'):
            return "inf" # Return string "inf" if destination is unreachable
        else:
            return int(min_distance * self.cost_per_km) # Return integer cost

    def route(self, source, destination):
        """
        Returns the shortest route for delivery between source and destination.

        Args:
            source (int): The index of the source city.
            destination (int): The index of the destination city.

        Returns:
            list: A list of city indices representing the shortest path.
                  Returns an empty list if destination is unreachable or inputs are invalid.
        """
        # Collect all unique nodes to correctly check if source/destination exist in the graph
        all_nodes = set(self._graph.keys())
        for node_list in self._graph.values():
            for neighbor, _ in node_list:
                all_nodes.add(neighbor)

        # Handle cases where source or destination nodes might not exist in the graph
        if source not in all_nodes or destination not in all_nodes:
            return [] # Return empty list for unreachable/invalid nodes

        distances, predecessors = self._dijkstra(source, destination)

        # Check if destination is reachable
        if distances.get(destination, float('inf')) == float('inf'):
            return [] # Return empty list if destination is unreachable

        # Reconstruct the path by backtracking from the destination to the source
        path = []
        current = destination
        
        # Ensure 'current' is valid and exists in the predecessors map.
        # This loop correctly reconstructs the path if one exists.
        while current is not None and current in predecessors:
            path.append(current)
            current = predecessors[current]
        
        # After loop, if path is empty or its last element is not the source,
        # it means path reconstruction failed or source was not reachable.
        # This case should ideally be caught by 'distances.get(...) == float('inf')' above,
        # but this provides an extra layer for edge cases (e.g., a node disconnected from source, but connected from dest)
        if not path or path[-1] != source:
            # Handle special case: source == destination.
            # If path is empty, and source and destination are the same, path should be [source].
            if source == destination:
                return [source]
            return [] # Path could not be fully reconstructed to source, or source not reachable

        # Path is built in reverse, so reverse it to get source -> ... -> destination
        return path[::-1]


# --- BOILERPLATE CODE (AS PROVIDED BY USER) ---
if __name__ == "__main__":
    # Reads the total number of cities (n)
    size = int(input())

    # Reads the list/tuple of edge tuples (e.g., "((0,1,10), (0,2,50))")
    edges = eval(input()) # eval() is used to parse the string into a Python object

    # Reads the source and destination city indices
    s = int(input())
    d = int(input())

    # Initializes the Weighted List (WL) / Adjacency List for the graph
    WL = {}
    for i in range(size):
        WL[i] = [] # Ensures all 'size' cities have an entry, even if isolated

    # Populates the WL dictionary with edges for an UNDIRECTED graph
    for ed in edges: # ed is expected to be a tuple (source, destination, distance)
        WL[ed[0]].append((ed[1], ed[2])) # Add edge from ed[0] to ed[1]
        WL[ed[1]].append((ed[0], ed[2])) # Add the reverse edge from ed[1] to ed[0]

    # Create an instance of XYZ_Courier, passing the pre-built WL
    C = XYZ_Courier(WL)

    # Call the cost and route methods, and print their returned values
    print(C.cost(s, d))
    print(C.route(s, d))
size = int(input())
edges = eval(input())
s=int(input())
d=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
C = XYZ_Courier(WL)
print(C.cost(s,d))
print(C.route(s,d))